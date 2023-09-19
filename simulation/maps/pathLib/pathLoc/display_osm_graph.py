#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""This example shows you how to download Openstreetmap data and convert those data to a networkx directional graph.
"""

import pathlib
import sys

import matplotlib.pyplot as plt
import networkx as nx
import OSMParser as osmp

root_folder = pathlib.Path(__file__).parent / '..'
root_folder = root_folder.resolve()

sys.path.append(root_folder.as_posix())


# Prepare paths
data_folder = root_folder / 'data'

temp_folder = data_folder / 'temp'
local_osm_file = data_folder / 'mapxml.map'
# local_nxg_file = data_folder / 'edge.edgelist'
local_graph_file = data_folder / 'graphmap.gexf'
output_shp_folder = data_folder / 'output_shp'

# Download OSM file
osm_map_file_content = osmp.download_osm(left=51.3407, bottom=35.7831, right=51.3680, top=35.7994, cache=False,
                                         cacheTempDir=temp_folder.as_posix())

# Convert OSM file to networkx graph
graph = osmp.read_osm(osm_map_file_content)
# graph = osmp.read_osm(local_osm_file.as_posix(), is_xml_string=False)
# Display graph on matplotlib figure
nx.draw(graph)
plt.show()
G = graph
# nx.write_edgelist(G, local_nxg_file)
nx.write_gexf(G, local_graph_file)
# You could also store the osm response to a file for further processing
with open(local_osm_file.as_posix(), 'w', encoding='utf-8') as f:
    f.write(osm_map_file_content)
