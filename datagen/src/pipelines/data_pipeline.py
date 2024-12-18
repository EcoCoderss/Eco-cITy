from services.ifc_service import read_ifc
from services.access_service import read_access
from services.csv_service import read_csv
from services.crewai_service import clean_with_crewai
from services.openrefine_service import clean_with_openrefine

def orchestrate_pipeline(file_path, file_type, project_name):
    # Step 1: Acquisizione
    if file_type == "ifc":
        raw_data = read_ifc(file_path)
    elif file_type == "access":
        raw_data = read_access(file_path)
    elif file_type == "csv":
        raw_data = read_csv(file_path)
    else:
        raise ValueError("Tipo di file non supportato")

    # Step 2: Pulizia automatica
    cleaned_data = clean_with_crewai(raw_data)

    # Step 3: Pulizia manuale (OpenRefine)
    final_data = clean_with_openrefine(cleaned_data, project_name)

    return final_data
