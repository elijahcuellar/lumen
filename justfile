dev:
    python3 -m fastapi dev {{ justfile_directory() }}/main.py

run:
    python3 -m fastapi run {{ justfile_directory() }}/main.py

test:
    curl -s http://localhost:8000/api/v1/password/30 | jq -r '.password'
