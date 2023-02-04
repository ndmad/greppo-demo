from greppo import app
import geopandas as gpd

app.base_layer(
    name="CartoDB Light",
    visible=True,
    url="https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}@2x.png",
    subdomains=None,
    attribution='&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
)

buildings_gdf = gpd.read_file("./data/buildings.geojson")

app.overlay_layer(
    buildings_gdf,
    name="Buildings",
    description="Buildings in a neighbourhood in Amsterdam",
    style={"fillColor": "#F87979"},
    visible=True,
)