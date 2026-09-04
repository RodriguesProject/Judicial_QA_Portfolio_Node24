# Regression Strategy

Regression focuses on core user journeys that could be affected by changes to case lifecycle, permissions or audit functionality.

### Smoke subset
- Create case
- Read case
- Update status as authorized role

### Full regression
- Validation failures
- Duplicate protection
- Access control
- Status persistence
- Audit trail
- End-to-end flow

The automated suite can be run with `pytest -q` on every pull request through GitHub Actions.
