# Conversor UTM a Coordenadas Geográficas

Conversor coordenadas UTM (Sistema de Coordenadas Universal Transversal) a coordenadas geográficas (latitud y longitud) en el sistema de referencia ETRS89.

## Requisitos

- Python 3
- Paquete `pyproj` (puedes instalarlo con `pip install pyproj`)

## Uso


```bash
python utm_to_latlon.py horizontal vertical zone [-gmaps]
```

## Ejemplo

```bash
$ python utm_to_latlon.py 448253 5410150 31 -gmaps
Input UTM Coordinates:
Horizontal: 448253
Vertical: 5410150
Zone: 31

Output Latitude and Longitude:
48.842165, 2.294742

Opening coordinates in Google Maps...
```