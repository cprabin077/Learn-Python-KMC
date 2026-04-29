# Smart Home Device System
class Device:
    def __init__(self, device_id, status):
        self.device_id = device_id
        self.status = status

    def turn_on(self):
        self.status = True
        return f"Device {self.device_id} is turned ON"

    def turn_off(self):
        self.status = False
        return f"Device {self.device_id} is turned OFF"


class SmartDevice(Device):
    def __init__(self, connectivity, connected, device_id, status):
        super().__init__(device_id, status)
        self.connectivity = connectivity
        self.connected = connected

    def connect(self):
        if self.status:
            self.connected = True
            return f"{self.device_id} connected via {self.connectivity}"
        else:
            return "Turn on the device first to connect"


class SmartThermosatat(SmartDevice):
    def __init__(self, device_id, status, connectivity, connected, temperature=40):
        super().__init__(connectivity, connected, device_id, status)
        self.temperature = temperature

    def set_temperature(self, temp):
        if temp < self.temperature:
            return self.turn_on()
        else:
            return self.turn_off()

    def display(self):
        return f"Device: {self.device_id}\nConnectivity: {self.connectivity}\nStatus: {self.status}"


t1 = SmartThermosatat("DID900", False, "Bluetooth", False)
t2 = SmartThermosatat("DID500", True, "WiFi", True)
t1.set_temperature(37)
t2.set_temperature(10)
print(t1.display())
print("------" * 20)
print(t2.display())
