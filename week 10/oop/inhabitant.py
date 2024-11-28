# Inhabitant class (located in oop/inhabitant.py)

class Inhabitant:
    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self):
        # Return a string representation that is useful for debugging.
        return f"Inhabitant(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        # Return a more user-friendly string representation.
        return f"{self.name}, Age: {self.age}, Energy: {self.energy}"


class Human(Inhabitant):

    def __init__(self, name="Human", age=0, energy=Inhabitant.MAX_ENERGY):
        super().__init__(name, age, energy)

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"Human {self.name}, Age: {self.age}, Energy: {self.energy}"

    def display(self):
        # Custom method to display information about the Human
        return f"Name: {self.name}, Age: {self.age}, Energy: {self.energy}"


class Robot(Inhabitant):
    laws = ["A robot may not harm a human being.", "A robot must obey human commands."]

    def __init__(self, name="Robot", age=0, energy=Inhabitant.MAX_ENERGY):
        super().__init__(name, age, energy)

    @staticmethod
    def the_laws():
        # Static method to return the laws
        return "\n".join(Robot.laws)

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"Robot {self.name}, Age: {self.age}, Energy: {self.energy}"

    def display(self):
        # Custom method to display information about the Robot
        return f"Name: {self.name}, Age: {self.age}, Energy: {self.energy}, Laws: {Robot.the_laws()}"


# Testing the Human and Robot classes
if __name__ == "__main__":
    # Create an object of type Human
    human = Human(name="Alice", age=30, energy=80)

    # Display the current state of the object
    print(repr(human))
    print(str(human))
    print(human.display())

    # Create an object of type Robot
    robot = Robot(name="R2D2", age=5, energy=100)

    # Display the current state of the object
    print(repr(robot))
    print(str(robot))
    print(robot.display())

    # Check laws for the robot
    print(Robot.the_laws())
