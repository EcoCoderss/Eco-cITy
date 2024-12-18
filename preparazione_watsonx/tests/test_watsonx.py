from src.services.watsonx_service import prepare_and_send_data, store_results

def test_prepare_and_send_data():
    data = {
        # Dati di esempio per il test
    }
    result = prepare_and_send_data(data)
    assert result is not None

def test_store_results():
    result = {
        # Risultati di esempio per il test
    }
    store_results(result)
    # Aggiungi asserzioni per verificare che i risultati siano stati archiviati correttamente