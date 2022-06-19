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
async def read_root(longitude: float, latitude: float):
    # TODO implementieren
    
    # Ergebnis als Index Dictonary zurückgeben
    return ergebnis.to_dict('records')
