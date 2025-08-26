@echo off
echo Initializing database with initial data...
cd backend
uv run python -m api_server.initial_data
echo Database initialization complete!
pause