from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait


class Broadcast:
    """
    Creates an instance of the Broadcast class, allowing for seamless communication between LEGO Spike Prime Hubs.
    Only the broadcast channel or the observe_channels needs to be set.

    Parameters:
    - callback (function): Runs on loop at 10 times per second. Either returns value to be sent, or receives a value if data has been sent.
    - broadcast_channel (int): The channel to broadcast on.
    - observe_channels (list[int]): Channels to observe.
    """
    def __init__(self, callback, broadcast_channel=None, observe_channels=[0]):
        print(callback, broadcast_channel, observe_channels)
        
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