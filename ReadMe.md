# Micro-Service: Internal Operations Automation Engine (FastAPI)

A lightweight, asynchronous internal service built with **Python (FastAPI)** and **Pydantic** designed to showcase modern, type-safe API automation workflows for internal customer success operations.

[Internal Dashboard UI] ──► API Route ──► [Async Triage Engine] ──► Automated Routing Directive

## How It's Built

This project focuses on asynchronous performance and strict type safety:

Fast Async Routing:   

*   **Fast Async Routing:** Uses Python's native async/await with Uvicorn, allowing it to handle heavy external I/O tasks smoothly without blocking the main thread.
*   **Type-Safe Validation:** Uses Pydantic to catch, clean, and validate incoming payloads before any operational logic runs.
*   **Decoupled Dependency Injection:** Uses FastAPI's built-in dependency injection to manage JWT authentication tokens across protected endpoints cleanly.
*   **Automatic API Docs:** Generates interactive OpenAPI/Swagger docs out of the box, making it simple to test routes and collaborate with other teams.

## Tech Stack & Deployment Envelope

*   **Runtime:** Python (v3.10+)
*   **Framework:** FastAPI
*   **Validation:** Pydantic (v2)
*   **HTTP client:** HTTPX
*   **ASGI Server:** Uvicorn

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

## Future Roadmap & Scalability
* **Move to Live LLMs:** Replace the current keyword-matching triage logic with live, asynchronous calls to the OpenAI or Anthropic SDKs (using streaming responses to keep latency low).
* **Database Integration:** Add an async database layer (PostgreSQL with SQLAlchemy/Asyncpg) to log triage history and track performance metrics.
* **Horizontal Scaling:** Containerise the service with Docker and set up a multi-worker Uvicorn configuration to handle higher traffic volumes under load.


