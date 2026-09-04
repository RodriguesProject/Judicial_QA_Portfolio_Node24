def test_SEC001_clerk_cannot_change_status(client):
    """FR-005 / TC-004: least-privilege rule blocks unauthorized status change."""
    client.post('/cases', headers={'X-Role': 'CLERK'}, json={'case_number': '10001-2026', 'subject': 'Access control'})
    response = client.patch('/cases/10001-2026/status', headers={'X-Role': 'CLERK'}, json={'status': 'IN_ANALYSIS'})
    assert response.status_code == 403


def test_SEC002_unknown_role_cannot_read(client):
    response = client.get('/cases/10001-2026', headers={'X-Role': 'GUEST'})
    assert response.status_code == 403


def test_SEC003_admin_can_reset_data(client):
    response = client.post('/reset', headers={'X-Role': 'ADMIN'})
    assert response.status_code == 200
