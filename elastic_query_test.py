from flask import Flask, redirect, url_for, request, render_template, jsonify
from datetime import datetime
from esConnector import conenect_es

app = Flask("__name__")
es=conenect_es()

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login', methods=["post"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == password:
        return "Login Successfull"
    else:
        return redirect(url_for("person", id=1))


@app.route("/insert")
def insert_es():
    body = {
        'slug': "rahim",
        'title': "hello rahim",
        'content':  " consectetur adipisicing elit. Placeat, quis!",
        'timestamp': datetime.now()
    }
    result = es.index(index='contents', doc_type='title',
                      id=body["slug"], body=body)
    return jsonify(result)


@app.route("/get/es")
def get_data():
    print("hi")
    result = es.get(index="search-summary-log", id="kFpfwHwBiSEDJahRArEE")
    # result = es.get(index="contents", id="tonmoy")
    print(result)
    return jsonify(result["_source"])


@app.route("/search/<slug>")
def search(slug):
    body = {
        "query": {
            "multi_match": {
                "query": slug,
                "fields": ["title", "content", "slug"]
            }
        }
    }
    result = es.search(index="contents", doc_type="title", body=body)
    data = result["hits"]["hits"]
    filterdata = []

    for item in data:
        filterdata.append(item["_source"])

    return jsonify({
        "data": {
            "data": filterdata
        }
    })


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)
