# lib/test_inheritance.py
from vehicle import Vehicle
from car import Car

def test_vehicle():
    print("Testing Vehicle class...")
    vehicle = Vehicle(18, 4)
    assert vehicle.wheel_size == 18
    assert vehicle.wheel_number == 4
    assert vehicle.go() == "vrrrrrrrooom!"
    assert vehicle.fill_up_tank() == "filling up!"
    print("✓ Vehicle tests passed!")

def test_car():
    print("Testing Car class...")
    car = Car(16, 4)
    assert car.wheel_size == 16  # Inherited attribute
    assert car.wheel_number == 4  # Inherited attribute
    assert car.go() == "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"  # Overridden method
    assert car.fill_up_tank() == "filling up!"  # Inherited method
    print("✓ Car tests passed!")

def test_inheritance():
    print("Testing inheritance relationship...")
    car = Car(16, 4)
    assert isinstance(car, Car)
    assert isinstance(car, Vehicle)  # Car inherits from Vehicle
    assert Car.__bases__[0] == Vehicle  # Direct parent is Vehicle
    print("✓ Inheritance tests passed!")

if __name__ == "__main__":
    test_vehicle()
    test_car()
    test_inheritance()
    print("All tests passed! 🎉")