#!/usr/bin/env python
import pika
import sys,json
from elastic import ElasticConn
obj = ElasticConn()
credentials = pika.PlainCredentials('user', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='mongo_connector',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='mongo_connector',
                       queue=queue_name,
                       routing_key='test')



def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    my_json = json.loads(body)
    tmp_id = my_json['_id']
    del my_json['_id']
    obj.insert_data(data=json.dumps(my_json),id=tmp_id,doc_type='tweet',index='text_index')

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()