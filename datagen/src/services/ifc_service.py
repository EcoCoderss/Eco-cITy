# src/services/ifc_service.py

import ifcopenshell
import os

def process_ifc_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File non trovato: {file_path}")
    try:
        ifc_file = ifcopenshell.open(file_path)
    except Exception as e:
        raise RuntimeError(f"Errore durante l'apertura del file IFC: {e}")

    processed_file_path = file_path.replace(".ifc", "_processed.ifc")
    ifc_file.write(processed_file_path)

    return processed_file_path