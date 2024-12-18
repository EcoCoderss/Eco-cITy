import logging
from typing import Dict, Any

from services.watsonx_service import WatsonXService

# Configura il logger per il debug
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class EnergyOptimizerAgent:
    """
    Classe per gestire le richieste di ottimizzazione energetica.
    Si connette a Watsonx.ai per eseguire analisi e suggerimenti.
    """

    def __init__(self, watsonx_service: WatsonXService):
        """
        Inizializza l'agente con un servizio Watsonx configurato.

        :param watsonx_service: Istanza di WatsonXService per connettersi all'API di Watsonx.ai
        """
        self.watsonx_service = watsonx_service
        logger.info("EnergyOptimizerAgent inizializzato.")

    def optimize_energy(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ottimizza il consumo energetico utilizzando Watsonx.ai.

        :param input_data: Dati di input per l'ottimizzazione energetica.
        :return: Risultati dell'ottimizzazione energetica.
        """
        try:
            logger.debug("Inizio ottimizzazione energetica con dati: %s", input_data)

            # Validazione dei dati
            if not self._validate_input(input_data):
                raise ValueError("Dati di input non validi.")

            # Invoca il modello AI tramite Watsonx.ai
            results = self.watsonx_service.run_model("energy_optimization", input_data)
            logger.debug("Risultati ottenuti: %s", results)

            return results

        except Exception as e:
            logger.error("Errore durante l'ottimizzazione energetica: %s", str(e))
            raise

    def _validate_input(self, input_data: Dict[str, Any]) -> bool:
        """
        Valida i dati di input per l'ottimizzazione energetica.

        :param input_data: Dati di input da validare.
        :return: True se i dati sono validi, False altrimenti.
        """
        required_keys = ["building_id", "energy_usage", "temperature"]
        for key in required_keys:
            if key not in input_data:
                logger.warning("Chiave mancante: %s", key)
                return False
        return True

# Esempio di utilizzo
if __name__ == "__main__":
    # Configura il servizio Watsonx
    watsonx_service = WatsonXService(api_key="YOUR_API_KEY", endpoint="https://api.watsonx.ai")

    # Inizializza l'agente
    agent = EnergyOptimizerAgent(watsonx_service)

    # Dati di esempio
    sample_data = {
        "building_id": "12345",
        "energy_usage": 5000,  # Consumo energetico in kWh
        "temperature": 22      # Temperatura media in gradi Celsius
    }

    # Ottimizza il consumo energetico
    try:
        optimization_results = agent.optimize_energy(sample_data)
        logger.info("Risultati dell'ottimizzazione: %s", optimization_results)
    except Exception as e:
        logger.error("Errore durante l'esecuzione dell'agente: %s", str(e))
