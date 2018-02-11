import pika
import sys

class MQ:
    def __init__(self):

        credentials = pika.PlainCredentials('user', 'password')

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))

        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='mongo_connector',
                                exchange_type='direct')##using direct exchange


    def publish(self,message,severity):
        severity = "{}".format(severity)
        self.channel.basic_publish(exchange='mongo_connector',
                            routing_key=severity,##collection_name
                            body=message)

        print(" [x] Sent %r:%r" % (severity, message))
    
    def __del__(self):

        self.connection.close()
