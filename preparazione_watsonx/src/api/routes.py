from fastapi import APIRouter, HTTPException
from src.services.watsonx_service import prepare_and_send_data, store_results
from src.models.watsonx_model import WatsonXData

router = APIRouter()

@router.post("/send-to-watsonx/")
def send_to_watsonx(data: WatsonXData):
    try:
        result = prepare_and_send_data(data)
        store_results(result)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))