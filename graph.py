import json
import networkx as nx
from lightning import LightningRpc
import subprocess
import matplotlib.pyplot as plt

graph = nx.DiGraph()

# Importing the listchannel output
def import_graph():
	#subprocess.call('lightning-cli listchannels > graph.json')
	with open('graph.json', 'r') as f:
		channel_dump = json.load(f)
	
	# Giving each node an unique integer (for convenience)	
	#l = []
	#for channel in channel_dump["channels"]:
	#	l.append(channel["source"])
	#	l.append(channel["destination"])
	#d = dict([(y,x+1) for x,y in enumerate(sorted(set(l)))])

	for channel in channel_dump["channels"]:
		graph.add_edge(channel["source"], channel["destination"], satoshis=channel["satoshis"], base_fee_millisatoshi=channel["base_fee_millisatoshi"], fee_per_millionth=channel["fee_per_millionth"], delay=channel["delay"], short_channel_id=channel["short_channel_id"])
	#print (graph.edges())

def base_fee_hist():
	base_fee_list = []
	for u, v, bf in graph.edges(data='base_fee_millisatoshi'):
		base_fee_list.append(bf)
	plt.hist(base_fee_list)
	plt.show()

def delay_hist():
	delay_list = []
	for u, v, d in graph.edges(data='delay'):
		delay_list.append(d)
	plt.hist(delay_list)
	plt.show()


def get_paths():
	'''
	#all simple paths
	print("all simple paths:\n")
	for path in nx.all_simple_paths(graph, source='0315a5746114ab9f3e8f0a3f2f73153ef1e4a8fb58daa54fa97c9603dfab989a30', target='03d21e56a377f8db14a3e67f893c9e9301a6c3a79db276f8c98fe35b1c8c095ed9'):
		print(path)
	'''
	#all shortest paths	
	print("all shortest paths:\n")
	for path in nx.all_shortest_paths(graph, source='0315a5746114ab9f3e8f0a3f2f73153ef1e4a8fb58daa54fa97c9603dfab989a30', target='03d21e56a377f8db14a3e67f893c9e9301a6c3a79db276f8c98fe35b1c8c095ed9'):
		print(path)
	
	#shortest path
	print("shortest path:\n")
	for path in nx.shortest_path(graph, source='0315a5746114ab9f3e8f0a3f2f73153ef1e4a8fb58daa54fa97c9603dfab989a30', target='03d21e56a377f8db14a3e67f893c9e9301a6c3a79db276f8c98fe35b1c8c095ed9'):
		print(path)

import_graph()
base_fee_hist()
delay_hist()
get_paths()
