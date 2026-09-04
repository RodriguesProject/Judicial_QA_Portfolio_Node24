def test_REG001_case_creation_remains_available_after_status_change(client):
    """Regression: core registration remains functional after another workflow is exercised."""
    client.post('/cases', headers={'X-Role': 'ANALYST'}, json={'case_number': '40001-2026', 'subject': 'Regression'})
    client.patch('/cases/40001-2026/status', headers={'X-Role': 'ANALYST'}, json={'status': 'CLOSED'})
    response = client.post('/cases', headers={'X-Role': 'CLERK'}, json={'case_number': '40002-2026', 'subject': 'New case'})
    assert response.status_code == 201
