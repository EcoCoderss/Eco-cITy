import unittest
from unittest.mock import patch, Mock
from models.energy_analysis import EnergyAnalysis
from agents.energy_optimizer_agent import EnergyOptimizerAgent

class TestEnergyAnalysis(unittest.TestCase):
    """
    Classe di test per la funzionalità di analisi energetica
    e ottimizzazione dell'energia.
    """

    def setUp(self):
        """
        Configurazione iniziale per ogni test. Inizializza
        un'istanza di EnergyAnalysis e mocka l'agente di ottimizzazione.
        """
        self.energy_analysis = EnergyAnalysis()
        self.sample_data = {
            "building_id": "B123",
            "energy_consumption": 1200,
            "area": 300,
            "occupancy": 50
        }
        self.optimizer_agent = Mock(spec=EnergyOptimizerAgent)

    @patch("models.energy_analysis.EnergyAnalysis.fetch_data")
    def test_fetch_data(self, mock_fetch_data):
        """
        Testa il metodo fetch_data per verificare che i dati siano
        caricati correttamente.
        """
        mock_fetch_data.return_value = [self.sample_data]
        result = self.energy_analysis.fetch_data("mock_source")

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["building_id"], "B123")

    def test_calculate_efficiency(self):
        """
        Testa il metodo calculate_efficiency per verificare che
        l'efficienza energetica venga calcolata correttamente.
        """
        efficiency = self.energy_analysis.calculate_efficiency(self.sample_data)

        expected_efficiency = self.sample_data["energy_consumption"] / (
            self.sample_data["area"] * self.sample_data["occupancy"]
        )

        self.assertAlmostEqual(efficiency, expected_efficiency)

    def test_optimize_energy(self):
        """
        Testa il metodo optimize_energy per verificare che l'ottimizzazione
        venga eseguita correttamente utilizzando l'agente.
        """
        self.optimizer_agent.optimize.return_value = {
            "optimized_consumption": 1000,
            "recommendations": ["Installare pannelli solari", "Sostituire lampadine"]
        }

        result = self.energy_analysis.optimize_energy(self.sample_data, self.optimizer_agent)

        self.optimizer_agent.optimize.assert_called_once_with(self.sample_data)
        self.assertEqual(result["optimized_consumption"], 1000)
        self.assertIn("Installare pannelli solari", result["recommendations"])

if __name__ == "__main__":
    unittest.main()
