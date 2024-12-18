from pydantic import BaseModel, Field
from typing import List, Optional

class EnergyDataPoint(BaseModel):
    """
    Rappresenta un singolo punto di dati per l'analisi energetica.
    """
    building_id: int = Field(..., description="ID univoco dell'edificio")
    energy_usage: float = Field(..., description="Consumo energetico in kWh")
    temperature: float = Field(..., description="Temperatura esterna in gradi Celsius")
    timestamp: str = Field(..., description="Data e ora del campionamento")

class OptimizationResult(BaseModel):
    """
    Rappresenta il risultato del processo di ottimizzazione.
    """
    building_id: int = Field(..., description="ID univoco dell'edificio")
    recommended_energy_usage: float = Field(..., description="Consumo energetico raccomandato in kWh")
    potential_savings: float = Field(..., description="Risparmio stimato in percentuale")
    optimization_notes: Optional[str] = Field(None, description="Note aggiuntive sull'ottimizzazione")

class EnergyAnalysisRequest(BaseModel):
    """
    Struttura per le richieste di analisi energetica.
    """
    data_points: List[EnergyDataPoint] = Field(..., description="Elenco dei punti dati per l'analisi")
    analysis_type: str = Field(
        ..., description="Tipo di analisi richiesta, ad esempio 'consumption' o 'efficiency'"
    )

class EnergyAnalysisResponse(BaseModel):
    """
    Struttura per la risposta dell'analisi energetica.
    """
    analysis_summary: str = Field(..., description="Sintesi dei risultati dell'analisi")
    optimizations: List[OptimizationResult] = Field(
        ..., description="Elenco dei risultati di ottimizzazione"
    )
    total_potential_savings: float = Field(
        ..., description="Risparmio totale stimato in percentuale"
    )

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione di dati fittizi per test
    data_point = EnergyDataPoint(
        building_id=1,
        energy_usage=500.0,
        temperature=25.0,
        timestamp="2024-12-18T10:00:00Z",
    )

    request = EnergyAnalysisRequest(
        data_points=[data_point],
        analysis_type="consumption",
    )

    print(request.json(indent=4))
