# Micro-Service: Internal Operations Automation Engine (FastAPI)

[![Continuous Integration](https://github.com/sigilmancer/fastapi-customer-success-service/tree/main/.github/workflows)](https://github.com/sigilmancer/fastapi-customer-success-service/tree/main/.github/workflows)

A lightweight, asynchronous internal service built with **Python (FastAPI)** and **Pydantic** designed to showcase modern, type-safe API automation workflows for internal customer success operations.

```text
[Internal Dashboard UI] ──► API Route ──► [Async Triage Engine] ──► Automated Routing Directive
```

---

## CI/CD & Automated DevOps

This repository is backed by a custom **GitHub Actions** continuous integration workflow:
1.  **Automated Cloud Testing:** Every push or pull request to the `main` branch spins up an isolated Ubuntu runner, sets up a Python 3.11 environment, installs dependencies, and runs the entire integration test suite automatically.
2.  **Failsafe Bug Tracking:** If a test assertion fails in the cloud, a native GitHub CLI (`gh`) automation step triggers instantly—automatically opening an alert issue on the repository dashboard, log-dumping the failure details, and assigning it directly to the author for quick triage.

---

## Testing & Quality Assurance

The project includes an integration test suite built with **Pytest** and FastAPI's native **TestClient** (powered by HTTPX) to evaluate the API lifecycle completely in-memory without network port leakage.

### Run Tests Locally:
```bash
python -m pytest -v
```

---

## How It's Built

This project focuses on asynchronous performance and strict type safety:
*   **Fast Async Routing:** Uses Python's native async/await with Uvicorn, allowing it to handle heavy external I/O tasks smoothly without blocking the main thread.
*   **Type-Safe Validation:** Uses Pydantic to catch, clean, and validate incoming payloads before any operational logic runs.
*   **Decoupled Dependency Injection:** Uses FastAPI's built-in dependency injection to manage JWT authentication tokens across protected endpoints cleanly.
*   **Automatic API Docs:** Generates interactive OpenAPI/Swagger docs out of the box, making it simple to test routes and collaborate with other teams.

---

## Tech Stack & Deployment Envelope

*   **Runtime:** Python (v3.11)
*   **Framework:** FastAPI
*   **Validation:** Pydantic (v2)
*   **HTTP Client:** HTTPX
*   **ASGI Server:** Uvicorn

---

## Running Locally

1. **Activate the local environment & install dependencies:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
2. **Launch the local ASGI worker instance:**
   ```powershell
   uvicorn main:app --reload
   ```
3. **Access the Interactive Test Portal:** Navigate directly to `http://127.0.0.1:8000` in your browser to test and execute live triage payloads using the built-in Swagger UI.

---

## Future Roadmap & Scalability

*   **Move to Live LLMs:** Replace the current keyword-matching triage logic with live, asynchronous calls to the OpenAI or Anthropic SDKs (using streaming responses to keep latency low).
*   **Database Integration:** Add an async database layer (PostgreSQL with SQLAlchemy/Asyncpg) to log triage history and track performance metrics.
*   **Horizontal Scaling:** Containerise the service with Docker and set up a multi-worker Uvicorn configuration to handle higher traffic volumes under load.
