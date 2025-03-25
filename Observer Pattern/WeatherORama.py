from abc import ABC, abstractmethod

# Interface Equivalent in Python

# We need 3 interfaces, one for the Subject, one for the Observer and other for the common Display

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

# Now we need to implement the Classes

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
    
    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def measurements_changed(self):
        self.notify_observers()
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
    
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.measurements_changed()

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
    
    def display(self):
        print(f"Current conditions: {self.temperature} celsius, {self.humidity} humidity")


weather_data = WeatherData()
current_dispaly = CurrentConditionsDisplay(weather_data)
weather_data.set_measurements(25,85,1012)










# # Interface equivalent in Python
# class FlyBehavior(ABC):
#     @abstractmethod
#     def fly(self):
#         pass

# class QuackBehavior(ABC):
#     @abstractmethod
#     def quack(self):
#         pass

# # Implementations of FlyBehavior
# class FlyWithWings(FlyBehavior):
#     def fly(self):
#         print("I'm flying with wings!")

# class NoFly(FlyBehavior):
#     def fly(self):
#         print("I can't fly.")

# class RocketFly(FlyBehavior):
#     def fly(self):
#         print("I am flying like a rocket.")

# # Implementations of QuackBehavior
# class Quack(QuackBehavior):
#     def quack(self):
#         print("Quack!")

# class MuteQuack(QuackBehavior):
#     def quack(self):
#         print("<< Silence >>")

# # Duck base class
# class Duck:
#     def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
#         self.fly_behavior = fly_behavior
#         self.quack_behavior = quack_behavior

#     def perform_fly(self):
#         self.fly_behavior.fly()

#     def perform_quack(self):
#         self.quack_behavior.quack()

#     def swim(self):
#         print("All ducks float, even decoys!")

#     def set_fly_behavior(self, fb):
#         self.fly_behavior = fb
    
#     def set_quack_behavior(self, qb):
#         self.quack_behavior = qb

# # MallardDuck using FlyWithWings and Quack behaviors
# class MallardDuck(Duck):
#     def __init__(self):
#         super().__init__(FlyWithWings(), Quack())
    
# class ModelDuck(Duck):
#     def __init__(self):
#         super().__init__(NoFly(), Quack())
    
#     def display(self):
#         print("I am a Model Duck!")

# # Run the simulation
# mallard = MallardDuck()
# mallard.perform_fly()  # Output: I'm flying with wings!
# mallard.perform_quack()  # Output: Quack!
# mallard.swim()  # Output: All ducks float, even decoys!


# # Dynamically change implementation at runtime
# model_duck = ModelDuck()
# model_duck.perform_fly()
# model_duck.set_fly_behavior(RocketFly())
# model_duck.perform_fly()
