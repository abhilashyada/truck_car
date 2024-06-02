class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False

    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started yet")
        else:
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
    def apply_brakes(self):
        self.current_speed -= self.tyre_friction
        if self.current_speed < 0:
            self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")


class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.max_cargo_weight = max_cargo_weight
        self.load = 0

    def load_cargo(self, cargo_weight):
        if self.is_engine_started:
            print("Cannot load cargo during motion")
        elif cargo_weight + self.load > self.max_cargo_weight:
            print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
        else:
            self.load += cargo_weight

    def unload_cargo(self, cargo_weight):
        if self.is_engine_started:
            print("Cannot unload cargo during motion")
        else:
            self.load -= cargo_weight
            if self.load < 0:
                self.load = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Car has not started yet")

def default_test():
    truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)
    print(truck.is_engine_started)
    truck.load_cargo(cargo_weight=50)  # Loading cargo_weight 50 to the truck
    print(truck.load)  # 0 + 50 => 50
    truck.unload_cargo(cargo_weight=25)  # Unloading cargo_weight 25 from the truck
    print(truck.load)  # 50 - 25 => 25
    truck.unload_cargo(cargo_weight=70)  # Unloading cargo_weight 70 (more than load in the truck)
    print(truck.load)  # 25 - 75 => 0 as load never be negative
    truck.load_cargo(cargo_weight=120)  # Prints "Cannot load cargo more than max limit: 100"

    truck.load_cargo(cargo_weight=20)  # Loading cargo_weight 20 to the truck
    truck.start_engine()
    print(truck.is_engine_started)  # True
    truck.load_cargo(cargo_weight=40)  
    truck.unload_cargo(cargo_weight=10)  

    truck.sound_horn()  
    truck.stop_engine()
    truck.sound_horn() 