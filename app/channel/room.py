import pika

class RabbitRoom(object):

    def __init__(self, room):
        self.connector = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5000))
        self.channel = self.connector.channel()
        self.room = room

        args = {'x-max-length': 2000, 'durable': True}

        self.channel.queue_declare(queue=room, arguments=args)
    
    def publish_message(self, data):
        self.channel.basic_publish(
            exchange='', routing_key=self.room, body=json.dumps(data))

    def get_messages(self, limit=50):
        messages = []
        count = 0
        for method_frame, properties, body in channel.consume(self.room):
            messages.append(json.loads(body))
            count += 1
            
            self.channel.basic_ack(method_frame.delivery_tag)

            if count == size:
                break

        requeued_messages = self.channel.cancel()
        print('Requeued %i messages' % requeued_messages)

        return messages
