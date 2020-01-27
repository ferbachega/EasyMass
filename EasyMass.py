#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  EasyMass.py
#  
#  Copyright 2020 Rafa <rafa@Frost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



import matplotlib
import numpy as np
from pprint import pprint

import sys
print sys.argv
args = sys.argv

print args

#'''
def parser_tags (args):
	""" Function doc """
	
	if '-idx' in args:
		idx  = True
	else: 
		idx = False
	
	if '-vmax' in args:
		index = args.index('-vmax')
		vmax  = int(args[index+1])
	else:
		vmax  = 200

	if '-vmin' in args:
		index = args.index('-vmin')
		vmin  = int(args[index+1])
	else:
		vmin  = 0

	if '-cmap' in args:
		index = args.index('-cmap')
		cmap  = args[index+1]
	else:
		cmap  = 'jet'




	if '-shading' in args:
		index =  args.index('-shading')
		shading = args[index+1]
	else:
		shading  = 'gouraud'



	if '-lspacing' in args:
		index = args.index('-lspacing')
		lspacing = int(args[index+1])
	else:
		lspacing = 20
	
	if '-lcolor' in args:
		index = args.index('-lcolor')
		lcolor= args[index+1]
	else:
		lcolor  =  'k'
	
	
	if '-fontsize' in args:
		index = args.index('-fontsize')
		fontsize = int(args[index+1])
	else:
		fontsize  =  14
	
	
	
	
	if '-i' in args:
		index = args.index('-i')
		log_file  = args[index+1]
	else:
		log_file  = None
	
	
	input_parm = {'vmax'     :vmax    , 
				  'vmin'     :vmin    , 
				  'cmap'     :cmap    , 
				  'shading'  :shading , 
				  'lspacing' :lspacing, 
				  'lcolor'   :lcolor  , 
				  'fontsize' :fontsize,
				  'log_file' :log_file,
				  'idx'      :idx
				  } 
	
	
	return input_parm
#'''

File = open(args[1], 'r')

massZ_list  = []
signal_list = []
fwhm_list   = []



for line in File:
	line2 = line.split()
	massZ_list .append(float(line2[0]))
	signal_list.append(float(line2[1]))
	fwhm_list  .append(float(line2[2]))


np_massZ_list  = np.array(massZ_list )
np_signal_list = np.array(signal_list)
np_fwhm_list   = np.array(fwhm_list  )

massZ_max   = np_massZ_list.max()
massZ_min   = np_massZ_list.min()
signal_max  = np_signal_list.max()


for i in range (np_massZ_list.size):
	print massZ_list[i], signal_list[i]



index = signal_list.index(signal_max)

print index , np_massZ_list[index], np_fwhm_list[index], np_signal_list[index]














































