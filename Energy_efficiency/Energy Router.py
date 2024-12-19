from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.energy_analysis import EnergyRequest, EnergyResponse, ErrorResponse
from services.watsonx_service import WatsonxService

# Inizializzazione del router per il modulo di ottimizzazione energetica
router = APIRouter(
    prefix="/energy",
    tags=["Energy Efficiency"],
    responses={404: {"description": "Not Found"}},
)

# Istanza del servizio Watsonx per la gestione delle richieste AI
watsonx_service = WatsonxService()

@router.post("/optimize", response_model=EnergyResponse, responses={
    400: {"model": ErrorResponse, "description": "Bad Request"},
    500: {"model": ErrorResponse, "description": "Internal Server Error"},
})
def optimize_energy(request: EnergyRequest):
    """
    Endpoint per ottimizzare il consumo energetico.

    Parametri:
    - `request`: Dati in input per il modello AI di ottimizzazione energetica.

    Risposta:
    - Dati ottimizzati per il consumo energetico.
    """
    try:
        # Validazione dei dati di input (gestita automaticamente da Pydantic)
        optimized_data = watsonx_service.optimize(request)
        return EnergyResponse(
            status="success",
            optimized_values=optimized_data,
            details="Ottimizzazione completata con successo."
        )
    except ValueError as e:
        # Gestione di errori specifici dei dati
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        # Gestione di errori generici o interni
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Errore interno al server. Contattare il supporto."
        )

@router.get("/status", response_model=dict)
def get_service_status():
    """
    Endpoint per verificare lo stato del servizio.

    Risposta:
    - Stato del servizio e dettagli sulla disponibilità.
    """
    return {
        "status": "ok",
        "service": "Watsonx Energy Optimization",
        "details": "Il servizio è operativo."
    }
