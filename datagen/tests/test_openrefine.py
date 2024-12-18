# tests/test_openrefine.py

from src.services.openrefine_service import create_project_from_csv, apply_operations, export_project
import os

def test_create_project_from_csv():
    project_id = create_project_from_csv("tests/test_data.csv")
    assert project_id is not None

def test_apply_operations():
    project_id = create_project_from_csv("tests/test_data.csv")
    assert project_id is not None
    operations = {
        "operations": [
            {
                "op": "core/text-transform",
                "description": "Transform values in cells",
                "engineConfig": {
                    "facets": [],
                    "mode": "row-based"
                },
                "columnName": "name",
                "expression": "value.replace('example', 'sample')",
                "onError": "keep-original",
                "repeat": False,
                "repeatCount": 10
            }
        ]
    }
    result = apply_operations(project_id, operations)
    assert result is not None

def test_export_project():
    project_id = create_project_from_csv("tests/test_data.csv")
    assert project_id is not None
    cleaned_file = export_project(project_id, format='csv')
    assert cleaned_file is not None
    assert os.path.exists(cleaned_file)
    # Pulizia del file esportato
    os.remove(cleaned_file)