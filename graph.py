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
	print (graph.edges())

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

import_graph()
base_fee_hist()
delay_hist()
