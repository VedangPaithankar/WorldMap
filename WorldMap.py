import folium
import pandas

WorldMap = folium.Map(location=[21.5937,78.9629], zoom_start=5, tiles = "Stamen Terrain")
vol_data = pandas.read_excel("AKvolclatlong.xlsx", sheet_name=0)
con_data = pandas.read_excel("world_map.xlsx", sheet_name=0)

feature_group_population=folium.FeatureGroup(name="Population")
feature_group_volcano=folium.FeatureGroup(name="Volcano")
feature_group_country=folium.FeatureGroup(name="Country")


feature_group_population.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red' }))


con_lat = list(con_data["latitude"])
con_lon = list(con_data["longitude"])
con_nam = list(con_data["country"])
vol_lat = list(vol_data["Latitude"])
vol_lon = list(vol_data["Longitude"])
vol_nam = list(vol_data["Volcano"])


for i in range (0,len(vol_lat)):
    feature_group_volcano.add_child(folium.CircleMarker(location=[vol_lat[i],vol_lon[i]], popup=vol_nam[i],
    radius=4, fill=True, color='red', fill_opacity=0.6))
    feature_group_country.add_child(folium.CircleMarker(location=[con_lat[i],con_lon[i]], popup=con_nam[i],
    radius=4, fill=True, color='blue', fill_opacity=0.6))

WorldMap.add_child(feature_group_population)
WorldMap.add_child(feature_group_volcano)
WorldMap.add_child(feature_group_country)
WorldMap.add_child(folium.LayerControl())

WorldMap.save("WorldMap.html")