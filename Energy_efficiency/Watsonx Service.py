import requests
from typing import Dict, Any

class WatsonxService:
    """
    Servizio per gestire l'integrazione con IBM Watsonx.ai e Watsonx.data.
    """

    def __init__(self, api_key: str, endpoint: str):
        """
        Inizializza il servizio WatsonxService.

        :param api_key: Chiave API per autenticazione con Watsonx.
        :param endpoint: Endpoint base per Watsonx API.
        """
        self.api_key = api_key
        self.endpoint = endpoint
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def send_request(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Metodo generico per inviare richieste a Watsonx.

        :param path: Percorso specifico dell'API.
        :param payload: Dati da inviare con la richiesta.
        :return: Risposta JSON decodificata.
        """
        url = f"{self.endpoint}/{path}"

        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Errore nella richiesta a Watsonx: {e}")

    def optimize_energy(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Invia i dati di input a Watsonx.ai per l'ottimizzazione energetica.

        :param input_data: Dati di input per il modello di ottimizzazione energetica.
        :return: Risultati dell'ottimizzazione.
        """
        path = "ai/energy/optimize"
        return self.send_request(path, input_data)

    def query_dataset(self, query: str) -> Dict[str, Any]:
        """
        Esegue una query su Watsonx.data per recuperare informazioni.

        :param query: Query SQL o specifica per Watsonx.data.
        :return: Risultati della query.
        """
        path = "data/query"
        payload = {"query": query}
        return self.send_request(path, payload)

# Esempio di utilizzo
if __name__ == "__main__":
    # Configurazione iniziale
    api_key = "your_api_key_here"
    endpoint = "https://api.watsonx.example.com"

    # Inizializzazione del servizio
    watson_service = WatsonxService(api_key, endpoint)

    # Esempio di ottimizzazione energetica
    input_data = {
        "building_id": "123",
        "energy_usage": [
            {"timestamp": "2024-12-01T00:00:00Z", "usage": 120},
            {"timestamp": "2024-12-01T01:00:00Z", "usage": 110}
        ],
        "target_savings": 15
    }

    try:
        result = watson_service.optimize_energy(input_data)
        print("Risultato ottimizzazione:", result)
    except Exception as e:
        print("Errore:", e)

    # Esempio di query su Watsonx.data
    query = "SELECT * FROM energy_consumption WHERE building_id = '123'"
    try:
        query_result = watson_service.query_dataset(query)
        print("Risultati query:", query_result)
    except Exception as e:
        print("Errore:", e)
