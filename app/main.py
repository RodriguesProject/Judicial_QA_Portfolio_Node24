from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(title="Judicial Information System - QA Portfolio", version="1.0.0")

cases = {}
audit_log = []

class CaseCreate(BaseModel):
    case_number: str = Field(min_length=5, max_length=30)
    subject: str = Field(min_length=3, max_length=200)
    status: Literal["REGISTERED", "IN_ANALYSIS", "CLOSED"] = "REGISTERED"

class StatusUpdate(BaseModel):
    status: Literal["REGISTERED", "IN_ANALYSIS", "CLOSED"]

ROLE_PERMISSIONS = {
    "CLERK": {"create", "read"},
    "ANALYST": {"create", "read", "update_status"},
    "ADMIN": {"create", "read", "update_status"},
}

def require_role(role: str, action: str):
    if action not in ROLE_PERMISSIONS.get(role, set()):
        raise HTTPException(status_code=403, detail="Insufficient permission")

@app.post("/cases", status_code=201)
def create_case(payload: CaseCreate, x_role: str = Header("CLERK"), x_user: str = Header("anonymous")):
    require_role(x_role, "create")
    if payload.case_number in cases:
        raise HTTPException(status_code=409, detail="Case already exists")
    cases[payload.case_number] = payload.model_dump()
    audit_log.append({"user": x_user, "action": "CREATE_CASE", "case": payload.case_number})
    return cases[payload.case_number]

@app.get("/cases/{case_number}")
def get_case(case_number: str, x_role: str = Header("CLERK")):
    require_role(x_role, "read")
    if case_number not in cases:
        raise HTTPException(status_code=404, detail="Case not found")
    return cases[case_number]

@app.patch("/cases/{case_number}/status")
def update_status(case_number: str, payload: StatusUpdate, x_role: str = Header("CLERK"), x_user: str = Header("anonymous")):
    require_role(x_role, "update_status")
    if case_number not in cases:
        raise HTTPException(status_code=404, detail="Case not found")
    old_status = cases[case_number]["status"]
    cases[case_number]["status"] = payload.status
    audit_log.append({
        "user": x_user,
        "action": "UPDATE_STATUS",
        "case": case_number,
        "from": old_status,
        "to": payload.status,
    })
    return cases[case_number]

@app.get("/cases/{case_number}/audit")
def get_audit(case_number: str, x_role: str = Header("ANALYST")):
    require_role(x_role, "read")
    if case_number not in cases:
        raise HTTPException(status_code=404, detail="Case not found")
    return [entry for entry in audit_log if entry["case"] == case_number]

@app.post("/reset", include_in_schema=False)
def reset_data(x_role: str = Header("ADMIN")):
    if x_role != "ADMIN":
        raise HTTPException(status_code=403, detail="Insufficient permission")
    cases.clear()
    audit_log.clear()
    return {"reset": True}
