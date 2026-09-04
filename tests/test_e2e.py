def test_E2E001_register_process_and_trace_case(client):
    """End-to-end scenario: register -> update -> retrieve -> audit."""
    case = {'case_number': '30001-2026', 'subject': 'E2E judicial workflow'}
    assert client.post('/cases', headers={'X-Role': 'ANALYST', 'X-User': 'e2e-user'}, json=case).status_code == 201
    assert client.patch('/cases/30001-2026/status', headers={'X-Role': 'ANALYST', 'X-User': 'e2e-user'}, json={
        'status': 'IN_ANALYSIS'
    }).status_code == 200
    retrieved = client.get('/cases/30001-2026', headers={'X-Role': 'CLERK'})
    assert retrieved.status_code == 200
    assert retrieved.json()['status'] == 'IN_ANALYSIS'
    audit = client.get('/cases/30001-2026/audit', headers={'X-Role': 'ANALYST'})
    assert audit.status_code == 200
    assert len(audit.json()) >= 2
