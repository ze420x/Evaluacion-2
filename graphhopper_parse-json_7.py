import requests
import urllib.parse

# URL base para Graphhopper
route_url = "https://graphhopper.com/api/1/route?"
key = "38526905-94fd-48fd-bd07-fc6438ac63a9"  # <-- tu token aquí


def geocoding(location, key):
    """Función para convertir una ubicación en coordenadas (lat/lng)."""
    while location == "":
        location = input("Por favor, ingresa la ubicación nuevamente: ")

    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]

        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")

        if len(state) != 0 and len(country) != 0:
            new_loc = f"{name}, {state}, {country}"
        elif len(country) != 0:
            new_loc = f"{name}, {country}"
        else:
            new_loc = name

        print(f"URL del API de geocodificación para {new_loc} (Tipo: {value})\n{url}")
    else:
        lat = "null"
        lng = "null"
        new_loc = location
        if json_status != 200:
            print(f"Error en geocodificación: {json_data.get('message', 'Error desconocido')}")

    return json_status, lat, lng, new_loc


# Programa principal
while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Perfiles de vehículo disponibles en Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("car (auto), bike (bicicleta), foot (a pie)")
    print("+++++++++++++++++++++++++++++++++++++++++++++")

    profile = ["car", "bike", "foot"]
    vehicle = input("Ingrese un perfil de vehículo de la lista anterior: ").lower()

    if vehicle in ["s", "salir"]:
        print("Saliendo del programa...")
        break
    elif vehicle not in profile:
        vehicle = "car"
        print("No se ingresó un perfil válido. Se usará el perfil por defecto: auto.")

    loc1 = input("Ubicación de inicio: ")
    if loc1.lower() in ["s", "salir"]:
        print("Saliendo del programa...")
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destino: ")
    if loc2.lower() in ["s", "salir"]:
        print("Saliendo del programa...")
        break
    dest = geocoding(loc2, key)

    print("=================================================")

    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        # Añadimos locale=es para obtener direcciones en español
        params = {"key": key, "vehicle": vehicle, "locale": "es"}
        paths_url = route_url + urllib.parse.urlencode(params) + op + dp

        response = requests.get(paths_url)
        paths_status = response.status_code
        paths_data = response.json()

        print(f"Estado del API de rutas: {paths_status}\nURL del API:\n{paths_url}")
        print("=================================================")
        print(f"Direcciones desde {orig[3]} hasta {dest[3]} en {vehicle}")
        print("=================================================")

        if paths_status == 200:
            distancia_km = (paths_data["paths"][0]["distance"]) / 1000
            distancia_mi = distancia_km / 1.61
            tiempo_ms = paths_data["paths"][0]["time"]
            horas = int(tiempo_ms / 1000 / 60 / 60)
            minutos = int((tiempo_ms / 1000 / 60) % 60)
            segundos = int((tiempo_ms / 1000) % 60)

            print(f"Distancia recorrida: {distancia_mi:.2f} millas / {distancia_km:.2f} km")
            print(f"Duración del viaje: {horas:02d}:{minutos:02d}:{segundos:02d}")
            print("=================================================")
            print("Narrativa del viaje (instrucciones paso a paso):")
            print("=================================================")

            for step in paths_data["paths"][0]["instructions"]:
                texto = step["text"]
                distancia = step["distance"] / 1000
                print(f"{texto} ({distancia:.2f} km / {distancia/1.61:.2f} millas)")

            print("=============================================")
        else:
            print(f"Error: {paths_data.get('message', 'No se pudo calcular la ruta')}")
            print("*************************************************")
    else:
        print("No se pudo realizar la geocodificación de una o ambas ubicaciones.")
