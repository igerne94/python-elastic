#pip3 install elasticsearch
from elasticsearch import Elasticsearch

es = Elasticsearch(
    [secrets['host']],port=secrets['port'],url_prefix=secrets['prefix'],
    http_auth=(secrets['user'],secrets['pass']),scheme="http",
)

res = es.search(index="testindex", body={"query": {"match_all": {}}})
print(res)