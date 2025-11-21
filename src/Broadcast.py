from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait


class Broadcast:
    def __init__(self, broadcast_channel: int, observe_channels: list[int], callback):
        self.observe_channels = observe_channels
        self.callback = callback

        self.hub = PrimeHub(broadcast_channel=broadcast_channel, observe_channels=observe_channels)

    def transmit(self, message):
        self.hub.ble.broadcast(message)

    def receive(self, index=0):
        return self.hub.ble.observe(self.observe_channels[index])

    def run(self, data_in, data_out):
        while True:
            data = data_in()
            print(data)

            status = Color.RED

            if data != None:
                data_out(data)
                status = Color.GREEN
                
            self.hub.light.on(status)

            wait(100)

    def run_sender(self):
        self.run(self.callback, self.transmit)

    def run_receiver(self):
        self.run(self.receive, self.callback)