import folium

#Start Plot Point in Center of Voluisa County
map_osm = folium.Map(location=[29.036211, -81.289173], zoom_start=10, max_zoom=15, tiles='Mapbox Control Room')

#FHCP Staff Offices

map_osm.circle_marker(location=[29.20305,-81.057048], popup = 'FHCP Daytona Beach 320 Suite D', radius=500,line_color='#0080FF',fill_color='#0080FF', fill_opacity=1)
map_osm.circle_marker(location=[29.114485,-81.023956], popup = 'Advanced Urgent Care', radius=500,line_color='#0080FF',fill_color='#0080FF', fill_opacity=1)
map_osm.circle_marker(location=[28.99609,-80.909191], popup = 'FHCP Edgewater Clinic', radius=500,line_color='#0080FF',fill_color='#0080FF', fill_opacity=1)
map_osm.circle_marker(location=[29.2688716,-81.0798526], popup = 'FHCP Ormond Beach', radius=500,line_color='#0080FF',fill_color='#0080FF', fill_opacity=1)
map_osm.circle_marker(location=[28.905444,-81.287455], popup = 'FHCP Orange City', radius=500,line_color='#0080FF',fill_color='#0080FF', fill_opacity=1)
map_osm.circle_marker(location=[29.0416151,-81.3245865], popup = 'FHCP Deland', radius=500,line_color='#0080FF',fill_color='#0080FF', fill_opacity=1)



#Create Patient Level Markers
map_osm.circle_marker(location=[29.036211, -81.289173], radius=10,line_color='#00000',fill_color='#FF0000', fill_opacity=.25)



map_osm.create_map(path='osm.html')