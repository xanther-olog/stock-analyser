from pymongo import MongoClient
import csv


def generateCSVFile(requiredStockList, collectionName, identifier):
    filepath = "C:\\Users\\Biswadip Basu\\Desktop\\StockAnalyserReports\\" + collectionName + "_" + identifier + ".csv"
    header = ["lastUpdateTime", "Symbol", "yearHigh", "previousClose", "dayHigh", "yearLow", "totalTradedVolume",
              "pChange", "dayLow", "series", "ffmc", "open", "lastPrice"]

    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        allRows = list()
        for i in requiredStockList:
            currentRow = list()
            currentRow.append(i["lastUpdateTime"])
            currentRow.append(i["symbol"])
            currentRow.append(i["yearHigh"])
            currentRow.append(i["previousClose"])
            currentRow.append(i["dayHigh"])
            currentRow.append(i["yearLow"])
            currentRow.append(i["totalTradedVolume"])
            currentRow.append(i["pChange"])
            currentRow.append(i["dayLow"])
            currentRow.append(i["series"])
            currentRow.append(i["ffmc"])
            currentRow.append(i["open"])
            currentRow.append(i["lastPrice"])
            allRows.append(currentRow)
        writer.writerows(allRows)


def processFileCreation(identifier, collectionName):
    client = MongoClient("localhost", 27017)
    database = client["central-db"]
    collection = database[collectionName]
    entireCollectionData = collection.find()
    requiredStockList = list()
    for entity in entireCollectionData:
        listOfAllStocksOnCurrentEntry = entity["stockData"]
        for currentStock in listOfAllStocksOnCurrentEntry:
            if str(currentStock["identifier"]).casefold() == identifier.casefold():
                requiredStockList.append(currentStock)
                break
    generateCSVFile(requiredStockList, collectionName, identifier)


def generateCollectionName(day, month, year):
    return str(year) + "-" + str(month) + "-" + str(day)


def processAllFileCreations(collectionName):
    client = MongoClient("localhost", 27017)
    database = client["central-db"]
    collection = database[collectionName]
    listOfStocks = collection.distinct("stockData.symbol")
    listOfStocks.remove("NIFTY 50")
    for currentStock in listOfStocks:
        processFileCreation(currentStock, collectionName)
