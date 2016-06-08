# Development log, extended

## Precincts map
[precinct boundaries source](http://www1.nyc.gov/site/planning/data-maps/open-data/districts-download-metadata.page)

#### Install topojson:
sudo npm install -g topojson

#### Shapefile to topojson:
topojson -o assets/datum/precincts.topojson -- rawData/precincts.geojson
