#!/usr/bin/env python

from ast import literal_eval
import sys

f = open("info_id.db","r")

info_id = f.read()

f.close()

f = open("id.db","r")

id_db = f.read()

f.close()

info_id = literal_eval(info_id)

id_db = literal_eval(id_db)

print "\n\n\n" * 30

search_id = sys.argv[1]

print "\n\n\n" * 30

print "  [ " + search_id + " ]  "

print "\n\n"

print "  passwd  =  " + str(id_db[search_id])

print "\n"

print "  WEB_1    :    " + str(info_id[search_id]["web1"])
print "  WEB_2    :    " + str(info_id[search_id]["web2"])
print "  WEB_3    :    " + str(info_id[search_id]["web3"])
print "  WEB_4    :    " + str(info_id[search_id]["web4"])
print "  WEB_5    :    " + str(info_id[search_id]["web5"])
print "  WEB_6    :    " + str(info_id[search_id]["web6"])

print "  REV_1    :    " + str(info_id[search_id]["rev1"])
print "  REV_2    :    " + str(info_id[search_id]["rev2"])
print "  REV_3    :    " + str(info_id[search_id]["rev3"])

print "  FOR_1    :    " + str(info_id[search_id]["for1"])
print "  FOR_2    :    " + str(info_id[search_id]["for2"])
print "  FOR_3    :    " + str(info_id[search_id]["for3"])
print "  FOR_4    :    " + str(info_id[search_id]["for4"])
print "  FOR_5    :    " + str(info_id[search_id]["for5"])

print "  SYS_1    :    " + str(info_id[search_id]["sys1"])

print "\n"

print "  point  =  " + str(info_id[search_id]["pt"])

print "\n"


