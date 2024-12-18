from fastapi import APIRouter, UploadFile, File, HTTPException
from src.services.validation_service import validate_event_data
from src.services.openrefine_service import create_project_from_csv, apply_operations, export_project
from src.models.event_model import EventData
import os

router = APIRouter()

@router.post("/validate/")
def validate(data: EventData):
    validation_result = validate_event_data(data)
    return validation_result

@router.post("/clean-data/")
def clean_data(file: UploadFile = File(...)):
    try:
        file_path = f"temp/{file.filename}"
        if not os.path.exists('temp'):
            os.makedirs('temp')

        with open(file_path, 'wb') as f:
            f.write(file.file.read())

        # Creare progetto su OpenRefine
        project_id = create_project_from_csv(file_path)

        # Applicare operazioni (esempio: operazioni di pulizia di base)
        operations = {
            "operations": [
                {
                    "op": "core/mass-edit",
                    "description": "Replace 'abc' with '123'",
                    "engineConfig": {"mode": "row-based", "facets": []},
                    "columnName": "nome_colonna",
                    "expression": "value.replace('abc', '123')",
                    "edits": [
                        {
                            "fromClause": {"type": "string", "value": "abc"},
                            "to": "123"
                        }
                    ]
                }
            ]
        }
        apply_operations(project_id, operations)

        # Esportare il progetto pulito
        cleaned_file_path = export_project(project_id, format='csv')

        # Pulizia del file temporaneo
        os.remove(file_path)

        return {"status": "success", "cleaned_file": cleaned_file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))