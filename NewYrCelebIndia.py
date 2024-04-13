# Viz 1 dated:4/13/2014

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import shapefile as shp
from shapely.geometry import Point
sns.set_style('whitegrid')

fp = r'myFiles/india_st.shp'
map_df = gpd.read_file(fp) 
map_df_copy = gpd.read_file(fp)
map_df.head()

# Define New Year celebration locations with their coordinates and names
celebrations = {
    'New Delhi': (77.1025, 28.7041),
    'BAISAKHI\n [Punjab]':(75.3412,31.1471),
    'Bihu \n[North East]':(93.2473,25.5736),
    'GUDI PADWA \n [Mumbai]': (72.8777, 19.0760),
    'UGADI \n [Karnataka]': (75.7139, 15.3173),
    'POHELA Boishak \n [Kolkata]': (88.3639, 22.5726),
    'PUTHANDU \n [Chennai]': (80.2707, 13.0827),
    '[Andra Pradesh]':(79.7400,15.9129),
    'VISHU \n [Kerala]':(76.6413,10.1632)
}
# Create a GeoDataFrame for the celebration locations
from shapely.geometry import Point
df_celebrations = gpd.GeoDataFrame({
    'City': celebrations.keys(),
    'geometry': [Point(xy) for xy in celebrations.values()]
}, crs="EPSG:4326")

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
map_df.plot(ax=ax, color='lightgrey')  # plot the map
df_celebrations.plot(ax=ax, marker='*', color='orange', markersize=30)  # plot the points

# Adding city labels
for city, point in celebrations.items():
    if city=='VISHU \n [Kerala]':
       ax.text(point[0], point[1], city, fontsize=11, ha='left',style ='italic',color="green")
    else:
       ax.text(point[0], point[1], city, fontsize=10, ha='left',style ='italic',color="blue")


#print(celebrations.items())
ax.set_title('New Year Celebrations in India',color='r')
plt.show()
