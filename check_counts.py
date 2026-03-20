
import requests
import json

def check_compraventa_count():
    base_url = "https://www.datos.gov.co/resource/7y2j-43cv.json"
    
    params = {
        "$select": "count(*)",
        "$where": "departamento = 'BOGOTÁ D.C.' AND nombre_natujur = 'COMPRAVENTA'"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code == 200:
            count = response.json()[0]['count']
            print(f"Número total de registros de COMPRAVENTA en Bogotá D.C.: {count}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_compraventa_count()
