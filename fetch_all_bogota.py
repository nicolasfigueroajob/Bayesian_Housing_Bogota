
import requests
import csv
import os
import time

def fetch_all_bogota():
    base_url = "https://www.datos.gov.co/resource/7y2j-43cv.json"
    csv_file = "data/bogota_full_data.csv"
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    
    # Campo oficial de todas las columnas posibles
    fieldnames = [
        'pk', 'matricula', 'fecha_radica_texto', 'fecha_apertura_texto', 
        'year_radica', 'orip', 'divipola', 'departamento', 'municipio', 
        'tipo_predio_zona', 'categoria_ruralidad_2024', 'num_anotacion', 
        'estado_folio', 'folios_derivados', 'dinamica_2024', 'cod_natujur', 
        'nombre_natujur', 'numero_catastral', 'numero_catastral_antiguo', 
        'documento_justificativo', 'count_a', 'count_de', 'predios_nuevos', 
        'tiene_valor', 'tiene_mas_de_un_valor', 'valor'
    ]
    
    where_condition = "departamento = 'BOGOTÁ D.C.'"
    limit_per_request = 20000 
    
    offset = 0
    if os.path.exists(csv_file):
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                lines = sum(1 for line in f)
                if lines > 1:
                    offset = lines - 1
                    print(f"Detectado archivo previo. Reanudando desde offset: {offset}")
        except Exception:
            pass

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    
    print(f"Iniciando descarga masiva de datos para Bogotá D.C...")
    print(f"Meta aproximada: 4.065.812 registros.")
    
    total_downloaded = offset
    mode = 'a' if offset > 0 else 'w'

    try:
        with open(csv_file, mode, newline='', encoding='utf-8') as f:
            # Usamos restval='' y extrasaction='ignore' para mayor robustez
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames, restval='', extrasaction='ignore')
            
            if mode == 'w':
                dict_writer.writeheader()

            while True:
                params = {
                    "$where": where_condition,
                    "$limit": limit_per_request,
                    "$offset": offset,
                    "$order": "pk" 
                }
                
                start_time = time.time()
                try:
                    response = requests.get(base_url, params=params, headers=headers, timeout=60)
                except requests.exceptions.Timeout:
                    print("\nTimeout. Reintentando...")
                    time.sleep(5)
                    continue
                
                if response.status_code != 200:
                    print(f"\nError {response.status_code}: {response.text}")
                    if response.status_code >= 500:
                        time.sleep(10)
                        continue
                    break
                
                data = response.json()
                if not data:
                    print("\nNo hay más datos disponibles.")
                    break
                
                dict_writer.writerows(data)
                
                batch_size = len(data)
                total_downloaded += batch_size
                offset += batch_size
                
                elapsed = time.time() - start_time
                progress = (total_downloaded / 4065812) * 100
                print(f"\rDescargados: {total_downloaded:,} [{progress:.2f}%] | Velocidad: {batch_size/elapsed:.1f} rec/s", end="", flush=True)
                
                if batch_size < limit_per_request:
                    break
                
                time.sleep(0.3) 
                
        print(f"\n\n¡PROCESO COMPLETADO!")
        print(f"Total final: {total_downloaded:,} registros.")
        print(f"Archivo actualizado en: {csv_file}")
        
    except KeyboardInterrupt:
        print("\n\nDescarga pausada por el usuario.")
    except Exception as e:
        print(f"\n\nError durante la descarga: {e}")

if __name__ == "__main__":
    fetch_all_bogota()
