import paho.mqtt.client as mqtt
import json

data = {
        "data":{
            "teste": "fpoaeia carol"
        }
        
}

topic = "house/state"

class Message():
    def __init__(self, topic, payload, qos=0):
        self.topic = topic
        self.payload = json.dumps(payload) 
        self.qos = qos

    def _repr__(self):
        return "Topic %s \n Message: %s" % (self.topic, self.payload)

class MQTTClient(mqtt.Client):
    def __init__(self):
        self.broker_address = "localhost" #"192.168.100.65"
        self.broker_port = 1883
        

        mqtt.Client.__init__(self,"myclient")

        self.on_connect = self.connected
        self.on_disconnect = self.disconnected
        self.on_publish = self.published
        
    def do_connect(self):
        self.connect(self.broker_address, self.broker_port)

    def do_publish(self, message):
        if not isinstance(message, Message):
            return None
        
        topic = message.topic
        payload = message.payload

        p = self.publish(topic, payload)
        print("P: ", p)

    def connected(self, client, userdata, flags, rc):
        if rc == 0:
            self.__connected_flag = True
            print("Connected!")
        print("Connected returned error rc=%d" % rc)
    def disconnected(self, client, userdata, rc):
        self.__connected_flag = False
        print("Disconnected!")

    def published(self, client, userdata, mid):
        print("message is published!")




client = MQTTClient()
client.do_connect()
message = Message(topic, data)
client.do_publish(message)
