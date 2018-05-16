from pymongo import MongoClient
import pprint

client = MongoClient('34.219.47.108', 27017)
db = client.sampleDB
#db.sampleDB.insert_one(
#            {"item": "snjv",
#                     "qty": 10,
#                          "tags": ["nthng"],
#                               "size": {"h": 128, "w": 135.5, "uom": "ucm"}})
#
# Get the sampleDB database
for a in db.sampleDB.find({"item": "canvas"}):

    pprint.pprint(a)
