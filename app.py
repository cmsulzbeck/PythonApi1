from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if(functionName == "add" or functionName == "subtract" or functionName == "multiply" or functionName == "divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301 # Missing parameter
        elif postedData["y"] == 0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "Missing parameter",
                "Status Code": status_code
            }
            return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)

            ret = x + y
            retMap = {
                'Message':ret,
                'StatusCode':status_code
            }
            return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "subtract")
        if (status_code != 200):
            retJson = {
                "Message": "Invalid data",
                "Status Code": status_code
            }
            return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)

            ret = x - y
            retMap = {
                'Message':ret,
                'StatusCode':status_code
            }
            return jsonify(retMap)

class Divide(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "divide")
        if (status_code != 200):
            if (status_code == 302):
                retJson = {
                    "Message": "y cannot be equal to 0",
                    "Status Code": status_code
                }

                return jsonify(retJson)
            else:
                retJson = {
                    "Message": "Invalid data",
                    "Status Code": status_code
                }

                return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)

            ret = x/y
            retMap = {
                'Message':ret,
                'StatusCode':status_code
            }
            return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "multiply")
        if (status_code != 200):
            retJson = {
                "Message": "Invalid data",
                "Status Code": status_code
            }
            return jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)

            ret = x*y
            retMap = {
                'Message':ret,
                'StatusCode':status_code
            }
            return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Divide, "/divide")
api.add_resource(Multiply, "/multiply")

if __name__ == "__main__":
    app.run(debug=True)
