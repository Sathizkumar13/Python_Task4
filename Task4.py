#1.Create a Python Class called circle with Constructor which will take a list as an argument for the task. The List is [10, 501, 22, 37, 100, 999, 87, 351]

# Circle with the given list
circle = Circle([10, 501, 22, 37, 100, 999, 87, 351])

class Circle:
    def __init__(self, data):
        """
        Constructor that initializes the Circle object with a list of values.
        
        :param data: List of numbers.
        """
        if not isinstance(data, list):
            raise ValueError("Expected a list as input.")
        self.data = data

    def display_data(self):
        """
        Displays the list stored in the Circle object.
        """
        print(f"The list is: {self.data}")

# Display the data
circle.display_data()

#Output
The list is: [10, 501, 22, 37, 100, 999, 87, 351]


#2. Create a proper member variables inside the task if required and use them when necessary. For example for this task create a class private variable named pi=3.141 

# Example usage
List = [10, 501, 22, 37, 100, 999, 87, 351]

class Circle:
    # Private class variable for Pi
    __pi = 3.141

    def __init__(self, radii):
        """
        Constructor that initializes the Circle object with a list of radii.
        
        :param radii: List of radii (positive numbers).
        """
        if not isinstance(radii, list) or not all(isinstance(r, (int, float)) and r > 0 for r in radii):
            raise ValueError("Input must be a list of positive numbers.")
        self.radii = radii  # Member variable to store radii

    def calculate_area(self):
        """
        Calculates and returns the area of circles for each radius in the list.
        :return: List of areas.
        """
        return [self.__pi * (r ** 2) for r in self.radii]

    def calculate_circumference(self):
        """
        Calculates and returns the circumference of circles for each radius in the list.
        :return: List of circumferences.
        """
        return [2 * self.__pi * r for r in self.radii]

    def display_results(self):
        """
        Displays the radii, areas, and circumferences of the circles.
        """
        areas = self.calculate_area()
        circumferences = self.calculate_circumference()

        print(f"Radii: {self.radii}")
        print(f"Areas: {areas}")
        print(f"Circumferences: {circumferences}")


# Display the results
circle.display_results()

#Output
Radii: [10, 501, 22, 37, 100, 999, 87, 351]
Areas: [314.1, 788394.1410000001, 1520.244, 4300.029, 31410.0, 3134721.141, 23774.229, 386974.341]
Circumferences: [62.82, 3147.282, 138.204, 232.434, 628.2, 6275.718, 546.534, 2204.982]

#3. From the given list create two class Methods Area and perimeter which will be going to calculate the Area and Perimeter.

# Given list
List = [10, 501, 22, 37, 100, 999, 87, 351]

class ShapeCalculator:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def area(self):
        return [dim ** 2 for dim in self.dimensions]

    def perimeter(self):
        return [4 * dim for dim in self.dimensions]

dimensions = [10, 501, 22, 37, 100, 999, 87, 351]
calculator = ShapeCalculator(dimensions)

areas = calculator.area()
perimeters = calculator.perimeter()

print("Areas:", areas)
print("Perimeters:", perimeters)

#Output
Areas: [100, 251001, 484, 1369, 10000, 998001, 7569, 123201]
Perimeters: [40, 2004, 88, 148, 400, 3996, 348, 1404]


