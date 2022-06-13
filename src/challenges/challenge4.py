# FastApi einbinden für REST-Services
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
# JSON Serialisierung
import orjson
# Pangas zur Daten-Anaylse
import pandas as pd
# GeoPandas für geometrische Funktionen
import geopandas
# Für geometrische Berechnungen
from shapely.geometry import Point
import math 

####
## Rückgabe für Anfrage, wird automatisch in JSON serialisiert
###
class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    ### 
    ## Wird aufgerufen, wenn die Antwort zurück gegeben wird
    ###
    def render(self, content) -> bytes:
        return orjson.dumps(content)

# Einen Router erzeugen, damit man zwei bereiche der Anwendung (Frontend, Backend) im Pfad trennen kann
router = APIRouter()
# Definition des Backends
api_app = FastAPI(title="die Schnittstelle", default_response_class=ORJSONResponse)
api_app.include_router(router)
# Definition der Oberfläche
app = FastAPI(title="die Oberfläche")
app.mount('/api', api_app)
app.mount('/', StaticFiles(directory="../../static", html=True), name="static")


###
## Diese Funktion nimmt Longitude und Latitude entgegen und findet Bewegungsdaten, die in der Nähe liegen.
## Es werden 30 Einträge zurück gegeben.
###
@api_app.get("/entfernung")
async def read_root(longitude, latitude):
    stationsdaten = pd.read_csv (r'../../daten/2022-06-11-stations.csv')
    geodaten = geopandas.GeoDataFrame(stationsdaten, geometry=geopandas.points_from_xy(stationsdaten.longitude, stationsdaten.latitude, crs='epsg:4326'))

    mcs = geopandas.GeoDataFrame(geometry=[Point(float(longitude), float(latitude))], crs='epsg:4326')
    mcs = mcs.to_crs('EPSG:31469')
    umgewandelt = geodaten.to_crs('EPSG:31469')
    umgewandelt['entfernung'] = umgewandelt.geometry.apply(lambda g: math.floor(mcs.distance(g)))

    preisinformationen = pd.read_csv(r'../../daten/2022-06-11-prices.csv')
    preisinformationen = preisinformationen.groupby('station_uuid').mean()
    bewegungsdaten = pd.merge(preisinformationen, umgewandelt, left_on='station_uuid', right_on='uuid')
    bewegungsdaten = bewegungsdaten.sort_values(by=['entfernung'], ascending=True)
    ergebnis = bewegungsdaten.head(30)

    # Umwandeln des Indexes auf String, da der JSON-Serialisierer es so haben möchte ...
    ergebnis.index = ergebnis.index.map(str)
    # Ergebnis als Index Dictonary zurückgeben
    return ergebnis.to_dict('index')
