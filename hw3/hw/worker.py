import zmq
import threading
import random
import time
import pprint
import math

def worker():
    worker_id = threading.current_thread().ident #each thread has different id
    print("I am worker " ,worker_id)  #get thread id
    context = zmq.Context()
    # recieve work
    worker_receiver = context.socket(zmq.PULL)
    worker_receiver.connect("tcp://127.0.0.1:5153")
    # send work
    worker_sender = context.socket(zmq.PUSH)
    worker_sender.connect("tcp://127.0.0.1:5159")
  

        
    work = worker_receiver.recv_json()
    if work[0]== 'minimum':
        result= [worker_id,'minimum',min(work[1])]
    else:
        result= [worker_id,'maximum',max(work[1])]

    print('sending result to collector', result)
    worker_sender.send_json(result)

for i in range(10):
    worker_id = random.randrange(1,10005)
    pWorker = threading.Thread(target=worker).start()