from elasticsearch import Elasticsearch

# es = Elasticsearch("https://0.0.0.0:9200")

# es = Elasticsearch(
#     ['localhost'],
#     http_auth=('', ''),
#     scheme="https",
#     port=9200,
#     use_ssl=False,
# )
def conenect_es(**kwargs):
    es = Elasticsearch([{"host": "0.0.0.0", "port": 9200}])
    if es.ping():
        print("es connected successfully")
    else:
        print("es disconnected")
    return es    


