from flask import Flask, redirect, url_for, request, render_template, jsonify
from pandas.core.algorithms import take
from esConnector import conenect_es
import pandas as pd
app = Flask("__name__")
es = conenect_es()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get/es")
def get_data():
    query_body = {
        "query": {
            "multi_match": {
                "query": "/RAB",
                "fields": ["agency_id"]
            }
        }
    }

    result = es.search(index="search-summary-log", body=query_body)

    data = result["hits"]["hits"]

    print(pd.DataFrame(data)["_source"])

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)
