from pymongo import MongoClient
import statics.Constants as constants


def getCollectionData(collectionName):
    client = MongoClient(constants.DB_HOST, constants.DB_PORT)
    database = client[constants.DB_NAME]
    collection = database[collectionName]
    return collection.find()


def getDistinctNamesOfStock(collectionName):
    client = MongoClient(constants.DB_HOST, constants.DB_PORT)
    database = client[constants.DB_NAME]
    collection = database[collectionName]
    return collection.distinct("stockData.symbol")
