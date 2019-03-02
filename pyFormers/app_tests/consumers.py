from channels.generic.websocket import WebsocketConsumer
import json


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('CONNECTED!')
        print(self.scope)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(f'recieving: {message}')

        self.send(text_data=json.dumps({
            'message': message
        }))
