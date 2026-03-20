
import requests
import json
import os

def fetch_bogota_data():
    # URL del recurso en datos.gov.co
    # El usuario proporcionó https://www.datos.gov.co/api/v3/views/7y2j-43cv/query.json
    # La forma estándar de consultar la API es a través del endpoint de recurso (.json):
    base_url = "https://www.datos.gov.co/resource/7y2j-43cv.json"
    
    # Filtramos por Bogotá D.C.
    # Según nuestra exploración, el valor exacto es "BOGOTÁ D.C."
    params = {
        "$where": "departamento = 'BOGOTÁ D.C.'",
        "$limit": 1000  # Traemos una muestra de 1000 registros
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"Conectando a la API para filtrar datos de Bogotá D.C...")
    
    try:
        response = requests.get(base_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            count = len(data)
            print(f"Éxito! Se recuperaron {count} registros para Bogotá D.C.")
            
            # Guardamos los datos en formato JSON
            json_file = "data/bogota_displacement_data.json"
            os.makedirs(os.path.dirname(json_file), exist_ok=True)
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Guardamos los datos en formato CSV
            csv_file = "data/bogota_displacement_data.csv"
            if count > 0:
                import csv
                # Obtenemos la unión de todas las llaves posibles
                keys = set()
                for record in data:
                    keys.update(record.keys())
                keys = sorted(list(keys))
                
                with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                    dict_writer = csv.DictWriter(f, fieldnames=keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(data)
            
            print(f"Los datos se han guardado en:")
            print(f"  - {json_file}")
            print(f"  - {csv_file}")
            
            # Mostrar los primeros 2 registros como ejemplo
            if count > 0:
                print("\nEjemplo de los primeros 2 registros:")
                print(json.dumps(data[:2], indent=2, ensure_ascii=False))
        else:
            print(f"Error al conectar con la API. Código de estado: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    fetch_bogota_data()
