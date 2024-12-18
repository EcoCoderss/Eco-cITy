# src/pipelines/orchestrator.py

from services.transfer_service import DataTransferService
from pipelines.data_pipeline import validate_mysql_data, clean_mysql_data
from pipelines.export_pipeline import export_to_json

def retrieve_data_from_mysql(mysql_config):
    # Implementa la funzione per estrarre i dati da MySQL
    # Restituisci i dati come lista di dizionari
    data = []  # Simulazione dell'estrazione dei dati
    return data

def orchestrate_datagen_workflow(access_path, mysql_config, output_path):
    # Step 1: Trasferisci dati da Access a MySQL
    transfer_service = DataTransferService(access_path, mysql_config)
    transfer_service.transfer_all_tables()
    transfer_service.close_connections()

    # Step 2: Recupera e valida i dati
    data = retrieve_data_from_mysql(mysql_config)
    validated_data = validate_mysql_data(data)

    # Step 3: Pulizia dei dati
    cleaned_data = clean_mysql_data(validated_data)

    # Step 4: Esportazione
    export_to_json(cleaned_data, output_path)

    print("Workflow completato.")