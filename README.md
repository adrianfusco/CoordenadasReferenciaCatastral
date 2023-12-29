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

## Caso de Uso

Podemos usarlo para obtener las coordenadas en Google Maps en base a una referencia catastral [Sede Electrónica del Catastro](https://www1.sedecatastro.gob.es/cycbieninmueble/ovcbusqueda.aspx).

Introducimos Referencia Catastral -> Datos -> CONSULTA DESCRIPTIVA Y GRÁFICA -> Obtenemos las coordenadas X e Y y el huso. Con ello podemos proveer al script los argumentos horizontal, vertical y zone.