import requests
import time
import os

def create_project_from_csv(csv_file_path, max_retries=5, wait=2):
    url = "http://localhost:3333/command/core/create-project-from-upload?wt=json"
    for attempt in range(max_retries):
        try:
            with open(csv_file_path, 'rb') as f:
                files = {'file': f}
                data = {'project-name': 'DataCleaningProject'}
                response = requests.post(url, files=files, data=data)
                print("Status Code:", response.status_code)
                print("Response Text:", response.text)
                if response.status_code == 200:
                    response_json = response.json()
                    project_id = response_json.get('projectId')
                    if project_id:
                        return project_id
                    else:
                        raise KeyError("La risposta dell'API non contiene 'projectId'")
                else:
                    raise RuntimeError(f"Errore durante la creazione del progetto: {response.status_code}")
        except requests.exceptions.ConnectionError:
            if attempt < max_retries - 1:
                time.sleep(wait)
                continue
            else:
                raise ConnectionError("Impossibile connettersi a OpenRefine su localhost:3333")

def apply_operations(project_id, operations):
    url = f"http://localhost:3333/command/core/apply-operations?project={project_id}&wt=json"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=operations)
    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"Errore durante l'applicazione delle operazioni: {response.status_code}")

def export_project(project_id, format='csv'):
    url = f"http://localhost:3333/command/core/export-rows/{project_id}.{format}?wt=json"
    response = requests.get(url)
    if response.status_code == 200:
        file_name = f"cleaned_data.{format}"
        with open(file_name, 'wb') as f:
            f.write(response.content)
        return file_name
    else:
        raise RuntimeError(f"Errore durante l'esportazione del progetto: {response.status_code}")