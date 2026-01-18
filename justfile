ENTRYPOINT := justfile_directory() + "/app/main.py"

dev:
    python3 -m fastapi dev {{ ENTRYPOINT }}

run:
    python3 -m fastapi run {{ ENTRYPOINT }}

test:
    curl -s http://localhost:8000/api/v1/password/30 | jq -r '.password'
