#!/bin/bash
set -e

# Start OpenRefine in the background and redirect logs
echo "Starting OpenRefine..."
$OPENREFINE_HOME/refine -i 0.0.0.0 -p 3333 -m 1400M > /app/openrefine/openrefine.log 2>&1 &

# Wait for OpenRefine to become available
echo "Waiting for OpenRefine to start..."
until curl -s "http://localhost:3333/command/core/get-version" | grep -q '"version"'; do
    sleep 2
done
echo "OpenRefine is available."

# Start FastAPI
echo "Starting FastAPI..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8000