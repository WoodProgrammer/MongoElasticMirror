from pymongo import Connection
import time,json,os
from bson_encoder import JSONEncoder
from mq_p import MQ
import argparse
import threading
#POOL = os.environ("POOL_OF_MQ")

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('collections', metavar='N', type=str, nargs='+',
                    help='Collection Names')


parser.add_argument('--cols', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='Collection Names here like ex: [ col1_name col2_name --cols ] ')


parser.add_argument('db', metavar='N', type=str, nargs='+',
                    help='db name')


parser.add_argument('--db', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='Db Names  like ex: [ db_name  --db ] ')








args = parser.parse_args()
print(args)
db_name = args.db
cols = args.collections
##gevent
mq_obj = MQ()


doc = {}
def tailer(col):

    db = Connection()['{}'.format(db_name[0])]
    coll = db['{}'.format(col)]
    print("Looking for db {} {}".format(db,col))
    cursor =  coll.find(tailable=True)
    while cursor.alive:
        try:
            doc = cursor.next()
            print(doc)
        except:
            pass

threads = []

for i in range(int(len(cols))):
    t = threading.Thread(target=tailer, args=(cols[i],))
    threads.append(t)
    t.start()