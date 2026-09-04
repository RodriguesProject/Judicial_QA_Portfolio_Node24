def test_TC001_register_valid_case(client):
    """FR-001 / TC-001: valid case registration succeeds."""
    response = client.post('/cases', headers={'X-Role': 'CLERK', 'X-User': 'thiago'}, json={
        'case_number': '00001-2026', 'subject': 'Judicial case', 'status': 'REGISTERED'
    })
    assert response.status_code == 201
    assert response.json()['case_number'] == '00001-2026'


def test_TC002_missing_required_field_is_rejected(client):
    """FR-002 / TC-002: missing mandatory subject is rejected."""
    response = client.post('/cases', headers={'X-Role': 'CLERK'}, json={'case_number': '00002-2026'})
    assert response.status_code == 422


def test_TC003_duplicate_case_is_rejected(client):
    """Data integrity: duplicate case numbers are not accepted."""
    payload = {'case_number': '00003-2026', 'subject': 'Duplicate control'}
    first = client.post('/cases', headers={'X-Role': 'CLERK'}, json=payload)
    second = client.post('/cases', headers={'X-Role': 'CLERK'}, json=payload)
    assert first.status_code == 201
    assert second.status_code == 409


def test_TC004_unknown_case_returns_404(client):
    """Negative functional test: unknown case cannot be retrieved."""
    response = client.get('/cases/DOES-NOT-EXIST', headers={'X-Role': 'CLERK'})
    assert response.status_code == 404
