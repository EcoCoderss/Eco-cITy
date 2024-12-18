# tests/test_autogen.py

from src.services.autogen_service import orchestrate_agents
import os

def test_orchestrate_agents():
    file_path = "tests/test_data.ifc"
    assert os.path.exists(file_path), f"File IFC non trovato: {file_path}"
    results = orchestrate_agents(file_path)
    assert results is not None
    assert len(results) == 1