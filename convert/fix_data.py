#!/usr/bin/env python3

#data fixing script
#
#as you can imagine, the data entries may contain some semi-correct
#values, which we need to adapt. this is done in this file.


def fix_data(data):
	"""
	updates given input with modifications.

	input: empiresdat object, vanilla, fully read.
	output: empiresdat object, fixed.
	"""

	###
	# Terrain fixes
	###

	#remove terrains with slp_id == -1
	#we'll need them again in the future, with fixed slp ids
	slp_ge0 = lambda x: x.slp_id >= 0
	data.terrain.terrains = list(filter(slp_ge0, data.terrain.terrains))

	#assign correct blending modes
	#key:   dat file stored mode
	#value: corrected mode
	blendmode_map = {
		#identical modes: [0,1,7,8], [4,6]
		0: 1, #dirt, grass, palm_desert
		1: 3, #farms
		2: 2, #beach
		3: 0, #water
		4: 1, #shallows
		5: 4, #roads
		6: 5, #ice
		7: 6, #snow
		8: 4, #no terrain has it, but the mode exists..
	}
	for terrain in data.terrain.terrains:
		terrain.blend_mode = blendmode_map[terrain.blend_mode]

	#set correct terrain ids
	for idx, terrain in enumerate(data.terrain.terrains):
		terrain.terrain_id = idx

	return data