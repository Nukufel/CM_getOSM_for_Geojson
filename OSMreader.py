import geopandas as gpd
import osmnx as ox
import json

boundary_geojson = gpd.read_file('boundary.geojson')

point = 47.22347, 8.81724
dist = 1000
radius = ox.features_from_point(point, {'building': True, 'room': True, 'door': True, 'indoor': True, 'amenity': True, 'sport': True, 'tourism': True, 'fauntain': True, 'leisure': True}, dist=dist)

radius_map = radius.map(lambda x: str(x) if isinstance(x, list) else x)

map_final = gpd.clip(radius_map, boundary_geojson)

map_final.to_file("C:\\Users\\niklas.vogel\\Projects\\PythonProjects\\CM_getOSM_for_Geojson\\output.geojson", driver="GeoJSON")


geojson_file_path = 'output.geojson'

with open(geojson_file_path, 'r') as geojson_file:
    myGeoJSON = json.load(geojson_file)

for feature in myGeoJSON["features"]:
    obj = feature["properties"]
    keys_to_delete = []
    for key, attrValue in obj.items():
        if not attrValue:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del obj[key]

output_geojson_file_path = 'output.geojson'

with open(output_geojson_file_path, 'w') as output_geojson_file:
    json.dump(myGeoJSON, output_geojson_file, indent=2, ensure_ascii=False)


#47.22347/8.81724 mid