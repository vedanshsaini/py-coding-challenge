import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        self.spot_size = spot_size
        self.total_spots = square_footage // (spot_size[0] * spot_size[1])
        self.available_spots = list(range(1, self.total_spots + 1))
        self.parking_map = {}

    def park_car(self, car, spot):
        if spot not in self.available_spots:
            return False  # Spot is already occupied
        else:
            self.available_spots.remove(spot)
            self.parking_map[car.license_plate] = spot
            return True  # Car parked successfully

    def generate_parking_map(self):
        return json.dumps(self.parking_map, indent=2)

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def park(self, parking_lot, spot):
        status = parking_lot.park_car(self, spot)
        if status:
            print(f"{self} parked successfully in spot {spot}")
        else:
            print(f"Failed to park {self} in spot {spot}. Spot is already occupied.")

def main():
    parking_lot_size = 2000
    car_license_plates = ["ABC1234", "XYZ5678", "DEF9876", "GHI6543", "JKL3210"]
    
    parking_lot = ParkingLot(parking_lot_size)

    cars = [Car(license_plate) for license_plate in car_license_plates]

    while cars and parking_lot.available_spots:
        car = random.choice(cars)
        spot = random.choice(parking_lot.available_spots)
        car.park(parking_lot, spot)
        cars.remove(car)

    print("Parking lot is full.")
    print("Parking Map:")
    print(parking_lot.generate_parking_map())

    # Save parking map to a file (optional/bonus)
    with open("parking_map.json", "w") as file:
        file.write(parking_lot.generate_parking_map())
    print("Parking map saved to parking_map.json")

if __name__ == "__main__":
    main()
