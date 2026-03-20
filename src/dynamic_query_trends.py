
import requests
import json

def get_bogota_trends():
    base_url = "https://www.datos.gov.co/resource/7y2j-43cv.json"
    
    # Consulta Dinámica SoQL:
    # 1. Filtramos por Bogotá, actos de COMPRAVENTA y que tengan valor registrado.
    # 2. Agrupamos por año de radicación.
    # 3. Calculamos el conteo y el valor promedio del mercado.
    params = {
        "$select": "year_radica, count(*), avg(valor)",
        "$where": "departamento = 'BOGOTÁ D.C.' AND nombre_natujur = 'COMPRAVENTA' AND tiene_valor = '1'",
        "$group": "year_radica",
        "$order": "year_radica DESC"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    print(f"📊 Ejecutando consulta dinámica directamente en la API de datos.gov.co...")
    
    try:
        response = requests.get(base_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print("\n📈 Tendencias de COMPRAVENTA en Bogotá D.C. (Datos filtrados dinámicamente):")
            print("-" * 65)
            print(f"{'Año':<10} | {'Conteo':<10} | {'Valor Promedio (COP)':<20}")
            print("-" * 65)
            
            for row in data:
                year = row.get('year_radica', 'N/A')
                count = row.get('count', '0')
                avg_val = float(row.get('avg_valor', 0))
                print(f"{year:<10} | {count:<10} | {avg_val:,.2f}")
            
            print("-" * 65)
            print("Éxito: Consulta realizada sin descargar la base masiva.")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    get_bogota_trends()
