from pymongo import Connection

conn = Connection()

db = conn['iBM-Brian-Michael']

print db.collection_names()
