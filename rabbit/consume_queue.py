#!/usr/bin/env python
import pika
import time 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # начало работы
    time.sleep(5)
    # окончание работы
    filename = '/tmp/status/' + body.decode()
    fd = open(filename, 'w')
    fd.write("1")
    fd.close()
    print("save status in %s" % filename)


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)



channel.start_consuming()
connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
