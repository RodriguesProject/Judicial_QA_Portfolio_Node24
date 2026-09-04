# Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| FR-001 | Authorized users can register a judicial case | High | Valid mandatory data creates a unique case |
| FR-002 | Mandatory fields are validated | High | Missing/invalid mandatory data is rejected |
| FR-003 | Authorized users can change case status | High | Permitted role can update; new state is persisted |
| FR-004 | Relevant changes are auditable | High | Audit record contains user, action and case; status transition records old/new state |
| FR-005 | Restricted operations require authorization | Critical | Unauthorized role receives a denial and data remains unchanged |
