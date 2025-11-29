# CI/CD for FastAPI example

This repository contains a minimal FastAPI app in `main.py` and a simple CI/CD setup using GitHub Actions.

What I added:
- `requirements.txt` — Python deps required to run and test the app.
- `Dockerfile` — builds a container image that runs `uvicorn main:app`.
- `.github/workflows/ci-cd.yml` — workflow that runs tests on push/pull requests; builds and optionally pushes a Docker image when pushing to `main` (requires Docker Hub secrets).
- `tests/test_main.py` — a minimal unit test for the `Item` pydantic model.

Run locally

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

2. Run the app locally:

```powershell
uvicorn main:app --reload
```

3. Run tests:

```powershell
pytest -q
```

Enable Docker Hub publish in GitHub Actions

1. Go to your GitHub repo Settings → Secrets → Actions and add two secrets:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN` (use a Docker Hub access token or password)

2. Push to the `main` branch — the workflow will build and push the image to `DOCKERHUB_USERNAME/ci-cd:latest`.

If you want a different registry or tag naming, edit `.github/workflows/ci-cd.yml` accordingly.
