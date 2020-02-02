from confluent_kafka import Producer


class KProducer():
    def __init__(self, hostName, topic=""):
        self._hostName = hostName
        self.topic = topic
        self._p = Producer({'bootstrap.servers': self._hostName})

    def __produceMesaage(self, msg, topic):
        if topic is None or len(topic) <= 0 or msg is None or len(msg) <= 0:
            # TODO: log error and maybe create seprate condition for msg check
            return ""
        self._p.produce(
            self.topic, 
            msg.encode('utf-8'), 
            callback=self.delivery_report
            )
        return ""

    def delivery_report(self, err, msg):
        # TODO: Update this method to produce the logs
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(),
                                                        msg.partition()))

    def pushMessage(self, msg, topic):
        self.__produceMesaage(msg, topic)
        return ""
