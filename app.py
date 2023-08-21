from flask_restx import Resource, Api
from flask import Flask, request
import request_validator

app = Flask(__name__)
api = Api(app)

ping_validator = request_validator.get_ping_body_validator(api=api)

@api.route("/ping")
class ping(Resource):
    @api.expect(ping_validator, validate=True)
    def get(self):
        payload = request.get_json()
        data = payload.get("data")

        res = {
            "response" : {
                "data" : data
            }
        }

        return res, 200

# ============================================
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
