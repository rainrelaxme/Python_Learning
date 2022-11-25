# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第16章 下载数据

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    eq_data = json.load(f)

eq_dicts = eq_data['features']

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in eq_dicts:
    try:
        mag = eq_dict["properties"]["mag"]
        lon = eq_dict["geometry"]["coordinates"][0]
        lat = eq_dict["geometry"]["coordinates"][1]
        title = eq_dict["properties"]["title"]
    except Exception as result:
        print("Error information is: ", result)
    else:
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_text.append(title)
    # finally:
    #     print("执行完成，无论正确与否")

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': "Viridis",
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')