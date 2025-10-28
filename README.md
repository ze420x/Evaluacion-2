🗺️ Calculador de Rutas con GraphHopper

Este programa calcula rutas entre dos ubicaciones usando la API de GraphHopper.  
Muestra la distancia, el tiempo estimado y las instrucciones paso a paso del viaje.  

------------------------------------------------------------

📦 Requisitos:

✅ Tener instalado Python 3  
✅ Instalar la librería requests con el comando:  
pip install requests  

------------------------------------------------------------

⚙️ Configuración:

1️⃣ Crear una cuenta en https://www.graphhopper.com  
2️⃣ Obtener una API key (token)  
3️⃣ Abrir el archivo del código y reemplazar la línea:
key = "TU_API_KEY_AQUI"
por tu clave real.  

------------------------------------------------------------

🚀 Ejecución:

1️⃣ Guardar el código en un archivo llamado rutas_graphhopper.py  
2️⃣ Abrir una terminal o consola en la carpeta donde está el archivo  
3️⃣ Ejecutar el programa con:
python rutas_graphhopper.py  

------------------------------------------------------------

🧭 Uso del programa:

- Elegir un perfil de vehículo: car 🚗, bike 🚴 o foot 🚶  
- Escribir la ubicación de inicio  
- Escribir la ubicación de destino  
- El programa mostrará:
  📏 La distancia total  
  ⏱️ El tiempo estimado  
  🗒️ Las instrucciones paso a paso  

👉 Para salir del programa, escribir S o Salir. Para salir en cualquier momento.  

------------------------------------------------------------

🧩 Ejemplo de salida:

Direcciones desde Madrid, España hasta Barcelona, España en car  
Distancia: 620.50 km  
Duración: 06:10:00  
Instrucciones:
- Sal en dirección norte por Calle Mayor (0.10 km)
- Gira a la derecha hacia A-2 (10.00 km)
...

------------------------------------------------------------

💡 Notas:

- Si no se elige un perfil válido, se usará car 🚗 por defecto.  
- Es necesario tener conexión a Internet 🌐 para que funcione la API.  


