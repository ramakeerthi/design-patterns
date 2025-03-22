from abc import ABC, abstractmethod

# Interface equivalent in Python
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

# Implementations of FlyBehavior
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying with wings!")

class NoFly(FlyBehavior):
    def fly(self):
        print("I can't fly.")

class RocketFly(FlyBehavior):
    def fly(self):
        print("I am flying like a rocket.")

# Implementations of QuackBehavior
class Quack(QuackBehavior):
    def quack(self):
        print("Quack!")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

# Duck base class
class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb
    
    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

# MallardDuck using FlyWithWings and Quack behaviors
class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())
    
class ModelDuck(Duck):
    def __init__(self):
        super().__init__(NoFly(), Quack())
    
    def display(self):
        print("I am a Model Duck!")

# Run the simulation
mallard = MallardDuck()
mallard.perform_fly()  # Output: I'm flying with wings!
mallard.perform_quack()  # Output: Quack!
mallard.swim()  # Output: All ducks float, even decoys!


# Dynamically change implementation at runtime
model_duck = ModelDuck()
model_duck.perform_fly()
model_duck.set_fly_behavior(RocketFly())
model_duck.perform_fly()
