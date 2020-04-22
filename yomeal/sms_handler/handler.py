import kafka_producer as kp


class SMS():
    def __init__(self):
        # TODO: get this hostname from config file/s
        hostName = "localhost:9092"
        self.producer = kp.KProducer(hostName)

    def readSMS(self, msg):
        # TODO: Call parser to parse the message and
        #       detect which kafka topic needs to be selected
        # Following will be msg body
        msgContent = {}
        msgContent["body"] = msg['Body']
        msgContent["from"] = msg['From']
        msgContent["MessageSid"] = msg['MessageSid']
        self.__pushToKafka(msgContent, "test")
        return ""

    def __pushToKafka(self, msg, topic):
        self.producer.pushMessage(msg, topic)
