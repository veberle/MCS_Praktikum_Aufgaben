# MCS Praktikum

Moin, in diesem Repository findest du Aufgaben, die schrittweise aufeinander aufgebaut sind.
Ziel ist es eine eigene Anwendung zu entwickeln. Die Challenges sollen dabei helfen die notwendigen Kenntnisse nach und nach aufzubauen um die gestelle Gesamtaufgabe zu meistern.
Dazu gibt es einenen imaginären Kunden, der Anforderungen stellt. Das Projekt soll iterativ, genau wie ein echtes Projekt gemeinsam mit diesen Kunden zusammen umgesetzt werden. 

## Die Gesamtaufgabe

Herr X ist Betreiber eines Verbraucher Informationsdienstes mit dem Namen MCS - MegaConsumserService und möchte seine Plattform um eine Webanwendung für eine standortbasierte Suche erweitern.

### Hintergrund

In Deutschland gibt es etwa 15.000 Tankstellen, die jeweils zu unterschiedlichen Firmen gehöeren. Von internationalen Megakonzeren wie SHELL, ESSO, ARAL hin bis zu inhabergeführten kleinen privaten Tankstellen ist alles
auf dem Markt vertreten. In Deutschland ist zudem der Markt besonders hart umkämpft, alle 2-5 Minuten geben die großen Konzerne ihren Tankstellen neue Preise vor.
Der Rest muss reagieren um nicht abgehängt zu werden. Dies führt zu unzähligen Preisbewegungen am Tag.

Rechtlich gibt es vom Gesetzgeber die Auflage, dass alle Tankstellen ihre Preise bei Änderung innerhalb von 15 Minuten an die Markttranzparenzschnittstelle senden müssen.
Mittels dieser kann die Kartellbehörde den Wettbewerb überwachen und kontrollieren.

Für die Verbraucher_in ist dies natürlich alles viel zu komplizert. Deshalb dürfen vom Gesetzgeber geprüfte Verbraucher Informationsdienste ebenfalls diese Daten abgreifen um sie bestmöglichst aufbereiten der Konsument_in anzubieten. Somit kann jede Konsument_in sich selbst informieren und entscheiden, wo und wann sie zu welchem Preis tanken möchte.

Die Firma MegaConsumserService möchte deshalb eine Webanwendung entwickeln lassen, bei der die günstigsten Preise in der Nähe ermittelt und angezeigt werden.

## Challenges

### Challenge 1 - Die Daten sichten

Hier geht es darum erst einmal überhaupt sich mit den Daten verttraut zu machen und erste Analysen vorzunehmen.

### Challenge 2 - Daten verknüpfen

Bei dieser Challenge müssen Statationsdaten und Preisbewegungen verküpft werden um sich die Marktsituation anzuschauen.

### Challenge 3 - Geo-Daten

Jede Tankstelle besitzt einen Standort, der als Geoposition interpretiert werden kann. In Challenge 3 geht es darum diese Daten auszuwerten und als Grundlage für Berechnungen zu verwenden.

### Challenge 4 - Das Backend

Da wir alle Informationen zusammen haben, geht es jetzt ans Eingemachte. In Challenge 4 wird ein Webservice entwickelt, der die Tankstellen mit den günstigsten Preisen in der Nähe sucht.

### Challenge 5 - Das Frontend

Mit den Daten aus dem Backend wird in dieser Challenge ein Backend entwickelt, das es Konsument_innen erlaubt selbst zu suchen und diese Daten anzuschauen.

### Challenge 6 - Geo Karte

Diese Challenge nutzt die Daten aus dem Backend und stellt sie auf einer Geo-Karte mit entsprechenden Logos dar. Jede Tankstelle hat ein Popup, was die Preise des Tages anzeigt.

## Technoliogien

Als Technologien werden die folgenden Frameworks und Programmiersprachen genutzt:

### Backend

Für die Challenges und das Backend wird Python als Programmiersprache genutzt. Zum Einsatz kommen zudem Pandas und GeoPandas als Hilfe für das Datamining und FastApi für die Webservice-Schnittstelle.

### Frontend

Die Oberfläche wird mittels HTML/CSS und JavaScript umgesetzt. Zur Hilfe wird JQuery und Bootstrap verwendet. 
Für Geo-Karten wird Leaflet genutzt.

## Installation

Für die Verwaltung der Python Version und der Abhängigkeiten verwenden wir [Mini Conda](https://docs.conda.io/en/latest/miniconda.html).

*Achtung:* Bei der Installation darauf achten, dass Miniconda dem Pfad hinzugefügt wird!

Anschließend kann man ein Terminal (Powershell, Bash, CMD, etc) öffnen und dort "conda info" eingeben. Wenn die Installation erfolgreich war, scheint jetzt eine Infoanzeige über die Installation.

### Umgebung einrichten

Für dieses Projekt erstellen wir ein eigenes Environment in dem alle Bibliotheken installiert werden.

conda create -n praktikum
conda activate praktikum

### Jupyter Notebook installieren

Dieses Projekt nutzt Jupyter Notebooks um wichtige Inhalte zu vermitteln. Die Installation erfolgt so:

conda install -c conda-forge notebook
conda install -c conda-forge ipykernel

### Bibliotheken installieren

Damit die erstlichen Bibliotheken installiert werden, müssen die folgenden Befehle ausgeführt werden:

conda install -c conda-forge pandas
conda install -c conda-forge geopandas
conda install -c conda-forge orjson
conda install -c conda-forge uvicorn
conda install -c conda-forge fastapi

### Weiteres

Weite hilfreiche Tips gibt es im [CheatShee](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
