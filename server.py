from flask import Flask
from flask import jsonify
import flask
from flask_cors import CORS
import requests
import os, copy
from flask import request


API_ENDPOINT = 'https://search-api-stg.byjusweb.com/byjus/web_search/'

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    return app


app = create_app()

@app.route("/get_question_by_id/<qid>/", methods=["GET"])
def get_question(qid):
    api_response = requests.get(
            url=API_ENDPOINT + "get_question_by_id/" + str(qid) + "/",
            headers={},
        )
    api_response = api_response.json()
    return api_response

@app.route("/update_question/", methods=["POST"])
def update_question():
    qid = request.json.get("qid")
    solution = request.json.get("solution")
    question = request.json.get("question")
    dataTosend = {
                "question" : question,
                "solution" : solution,
                "qid" : qid
            }
    api_response = requests.post(
            url=API_ENDPOINT + "update_question/",
            json=dataTosend,
            headers={},
        )
    api_response = api_response.json()
    return api_response



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)


