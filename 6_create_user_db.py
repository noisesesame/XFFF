#!/usr/bin/env python

import os
import random

dd = raw_input("  all user number > ")

d = "{"

f = "{"


for i in range(0, int(dd)+1):

	d += "'user" + str(i) + "': {"

	d += "'web1':'n',"
	d += "'web2':'n',"
	d += "'web3':'n',"
	d += "'web4':'n',"
	d += "'web5':'n',"
	d += "'web6':'n',"

	d += "'rev1':'n',"
	d += "'rev2':'n',"
	d += "'rev3':'n',"

	d += "'for1':'n',"
	d += "'for2':'n',"
	d += "'for3':'n',"
	d += "'for4':'n',"
	d += "'for5':'n',"

	d += "'sys1':'n',"

	d += "'pt':'0'"

	if i == int(dd):

		d += "}}"
		
	else:

		d += "},"





for i in range(0, int(dd)+1):


	pp = ""
	pp2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

	for p in range(1,40):

		pp += random.choice(pp2)	

	f += "'user" + str(i) + "':'" 

	f += pp + "'"

	if i == int(dd):

		f += "}"

	else:

		f += ","
	


q = open("info_id.db","w")
q.write(str(d))
q.close()


q = open("id.db","w")
q.write(str(f))
q.close()

q = open("session.db","w")
q.write("{}")
q.close()







