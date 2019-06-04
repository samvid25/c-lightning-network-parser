import json
import networkx as nx
from lightning import LightningRpc
import subprocess

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

import_graph()
