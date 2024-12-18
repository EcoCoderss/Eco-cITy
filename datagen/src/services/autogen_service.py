# src/services/autogen_service.py

from src.services.ifc_service import process_ifc_file

class MockAgent:
    def __init__(self, role):
        self.role = role

def orchestrate_agents(file_path):
    # Definisci i ruoli degli agenti
    data_scientist = MockAgent(role="data_scientist")
    data_engineer = MockAgent(role="data_engineer")

    # Funzione per processare il file IFC
    def process_ifc_task():
        processed_file_path = process_ifc_file(file_path)
        return processed_file_path

    # Simula l'esecuzione dei task
    tasks = [
        {"agent": data_scientist, "description": "EDA"},
        {"agent": data_engineer, "description": "Process IFC", "function": process_ifc_task}
    ]

    results = [task["function"]() for task in tasks if "function" in task]
    return results