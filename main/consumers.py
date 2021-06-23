from channels.generic.websocket import WebsocketConsumer
import json
from .views import *

class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
	def receive(self,text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		self.send(text_data=json.dumps({
			'message': message
			}))

	
		
