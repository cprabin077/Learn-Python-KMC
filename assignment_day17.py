# Smart Home System (Mini Project using Multiple Inheritance)
class Device:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        return f"{self.name} is turned ON"

    def turn_off(self):
        self.status = "OFF"
        return f"{self.name} is turned OFF"
    
class SmartFeature:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        return "Device connected to network"

    def disconnect(self):
        self.connected = False
        return "Device disconnected"
    
class SecurityFeature:
    def __init__(self):
        self.alarm = False

    def trigger_alarm(self):
        self.alarm = True
        return "Alarm Triggered!"

    def stop_alarm(self):
        self.alarm = False
        return "Alarm stopped"
    
class SmartCamera(Device, SmartFeature, SecurityFeature):
    def __init__(self, name):
        Device.__init__(self, name)
        SmartFeature.__init__(self)
        SecurityFeature.__init__(self)

    def status_report(self):
        return f"""
Device: {self.name}
Power: {self.status}
Connected: {self.connected}
Alarm: {self.alarm}
"""
    
cam = SmartCamera("Front Door Camera")

print(cam.turn_on())
print(cam.connect())
print(cam.trigger_alarm())

print(cam.status_report())

print(cam.stop_alarm())
print(cam.disconnect())
print(cam.turn_off())


# Upgrade Version (Using super() – Advanced)
class Device:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        return f"{self.name} is ON"

    def turn_off(self):
        self.status = "OFF"
        return f"{self.name} is OFF"

class SmartFeature:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connected = False

    def connect(self):
        self.connected = True
        return "Connected to network"

    def disconnect(self):
        self.connected = False
        return "Disconnected from network"

class SecurityFeature:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alarm = False

    def trigger_alarm(self):
        self.alarm = True
        return "Alarm ON"

    def stop_alarm(self):
        self.alarm = False
        return "Alarm OFF"

class SmartCamera(Device, SmartFeature, SecurityFeature):
    def __init__(self, name):
        super().__init__(name=name)

    def status_report(self):
        return f"""
Device: {self.name}
Power: {self.status}
Connected: {self.connected}
Alarm: {self.alarm}
"""

cam = SmartCamera("Front Camera")

print(cam.turn_on())
print(cam.connect())
print(cam.trigger_alarm())

print(cam.status_report())