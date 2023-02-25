import pymongo
from pymongo import MongoClient

def get_followers_count(username):

    client = pymongo.MongoClient("mongodb+srv://chinnu:chinnu@cluster0.6vnzvkt.mongodb.net/?retryWrites=true&w=majority")

    mydb = client["users"]

    mycol = mydb[username]

    dat = []

    for x in mycol.find({}, {"_id": 0}):
        dat.append(x)

    return(dat)