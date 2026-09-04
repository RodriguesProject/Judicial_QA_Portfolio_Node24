# Risk Matrix

| Risk | Impact | Probability | Rating | Mitigation / Test Coverage |
|---|---:|---:|---:|---|
| Unauthorized modification of case data | 5 | 3 | 15 — High | Role/permission negative tests |
| Missing audit trail | 5 | 2 | 10 — High | Integration + audit assertions |
| Invalid or incomplete case data | 4 | 3 | 12 — High | Validation / negative tests |
| Regression breaks core registration | 4 | 3 | 12 — High | Regression suite |
| Slow response under repeated local calls | 3 | 2 | 6 — Medium | Lightweight performance script |
