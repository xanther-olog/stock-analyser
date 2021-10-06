from flask import Flask, request
import traceback
import service.ServiceUtils as service

app = Flask(__name__)


@app.route("/api/generateFile")
def generateCsv():
    try:
        stockIdentifier = request.args.get("identifier")
        day = request.args.get("day")
        month = request.args.get("month")
        year = request.args.get("year")
        service.processFileCreation(stockIdentifier, service.generateCollectionName(day, month, year))
    except:
        traceback.print_exc()
        return "ERROR", 500
    return "SUCCESS", 200


@app.route("/api/generateAllCsv")
def generateAllStockCsv():
    try:
        day = request.args.get("day")
        month = request.args.get("month")
        year = request.args.get("year")
        service.processAllFileCreations(service.generateCollectionName(day, month, year))
    except:
        traceback.print_exc()
        return "ERROR", 500
    return "SUCCESS", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=3000)
