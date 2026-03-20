
import requests
import json
import csv
import os
import time

def fetch_all_bogota():
    base_url = "https://www.datos.gov.co/resource/7y2j-43cv.json"
    
    # Configuramos los archivos de salida
    json_file = "data/bogota_full_data.json"
    csv_file = "data/bogota_full_data.csv"
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    
    # Filtro base
    where_condition = "departamento = 'BOGOTÁ D.C.'"
    limit_per_request = 50000
    offset = 0
    total_downloaded = 0
    header_written = False
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"Iniciando descarga masiva de datos para Bogotá D.C...")
    
    try:
        # Abrimos el archivo CSV para escritura directa por bloques
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            while True:
                params = {
                    "$where": where_condition,
                    "$limit": limit_per_request,
                    "$offset": offset,
                    "$order": "pk" # Ordenar para que el offset sea consistente
                }
                
                print(f"Descargando lote: Offset {offset}...")
                response = requests.get(base_url, params=params, headers=headers)
                
                if response.status_code != 200:
                    print(f"Error en respuesta: {response.status_code}")
                    break
                
                data = response.json()
                if not data:
                    print("No hay más datos.")
                    break
                
                # Obtener todas las llaves posibles del primer lote para el header
                if not header_written:
                    # En el primer lote buscamos la unión de llaves por si acaso
                    keys = set()
                    for r in data: keys.update(r.keys())
                    keys = sorted(list(keys))
                    dict_writer = csv.DictWriter(f, fieldnames=keys)
                    dict_writer.writeheader()
                    header_written = True
                
                # Escribir registros
                dict_writer.writerows(data)
                
                batch_size = len(data)
                total_downloaded += batch_size
                print(f"Descargados {total_downloaded} registros...")
                
                if batch_size < limit_per_request:
                    # Llegamos al final
                    break
                    
                offset += limit_per_request
                # Pequeña pausa para no saturar al servidor
                time.sleep(0.1)
                
        print(f"\nÉXITO: Se han descargado {total_downloaded} registros totales.")
        print(f"Archivo guardado en: {csv_file}")
        
    except Exception as e:
        print(f"Error durante la descarga: {e}")

if __name__ == "__main__":
    fetch_all_bogota()
