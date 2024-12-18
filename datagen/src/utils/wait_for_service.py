import time
import requests
from requests.exceptions import ConnectionError

def wait_for_openrefine(host: str = "localhost", port: int = 3333, timeout: int = 30):
    url = f"http://{host}:{port}/command/core/status?wt=json"
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200 and '"ok":true' in response.text.lower():
                print("OpenRefine è disponibile.")
                break
        except ConnectionError:
            pass
        
        if time.time() - start_time > timeout:
            raise TimeoutError(f"OpenRefine non è disponibile su {host}:{port} dopo {timeout} secondi.")
        
        print("Attendo che OpenRefine si avvii...")
        time.sleep(2)