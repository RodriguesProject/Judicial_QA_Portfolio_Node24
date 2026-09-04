def test_INT001_status_update_persists_and_creates_audit_event(client):
    """FR-003 + FR-004: status update is persisted and traceable through audit data."""
    client.post('/cases', headers={'X-Role': 'ANALYST', 'X-User': 'analyst1'}, json={
        'case_number': '20001-2026', 'subject': 'Integration flow'
    })
    update = client.patch('/cases/20001-2026/status', headers={'X-Role': 'ANALYST', 'X-User': 'analyst1'}, json={
        'status': 'IN_ANALYSIS'
    })
    assert update.status_code == 200
    assert update.json()['status'] == 'IN_ANALYSIS'

    audit = client.get('/cases/20001-2026/audit', headers={'X-Role': 'ANALYST'})
    assert audit.status_code == 200
    assert audit.json()[-1]['action'] == 'UPDATE_STATUS'
    assert audit.json()[-1]['to'] == 'IN_ANALYSIS'
