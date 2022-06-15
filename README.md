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
