# Back-End-Development-Pictures

IBM Python Backend capstone-compatible Flask Pictures microservice, matching the training endpoint naming and event fields.

## Quick start

```bash
python -m pip install -r requirements.txt
python -m pytest -v tests/test_api.py
python app.py
```

Default port `5000`. Routes: `GET /health`, `GET /count`, `GET /picture`, `GET /picture/<id>`, `POST /picture`, `PUT /picture/<id>`, `DELETE /picture/<id>`.

- `GET /count` returns `{"length":10}` initially.
- `POST` returns 201, duplicate id returns 302.
- Successful `DELETE` returns 204.

The 11-test suite follows the IBM exercise checkpoints. It must be executed to produce genuine PyTest output; the source files themselves are not proof that it passed.
