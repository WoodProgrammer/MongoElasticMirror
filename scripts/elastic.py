from datetime import datetime
from elasticsearch import Elasticsearch
class ElasticConn:
    def __init__(self):
        self.es = Elasticsearch()

    def insert_data(self,data,id,doc_type,index):

        res = self.es.index(index=index, doc_type=doc_type, id=id, body=data)


