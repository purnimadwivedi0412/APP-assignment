class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: Rs.", self.price)
        print("Category:", self.get_category())
        print("------------------------")


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_all(self):
        print("\n--- Mobile Store Details ---")
        for mobile in self.mobiles:
            mobile.display()


# Main program
store = Store()

m1 = Mobile("Apple", "iPhone 15", 70000)
m2 = Mobile("Samsung", "Galaxy A55", 35000)
m3 = Mobile("Redmi", "Note 13", 15000)

store.add_mobile(m1)
store.add_mobile(m2)
store.add_mobile(m3)

store.display_all()


#output
'''--- Mobile Store Details ---
Brand: Apple
Model: iPhone 15
Price: Rs. 70000
Category: Premium
------------------------
Brand: Samsung
Model: Galaxy A55
Price: Rs. 35000
Category: Mid-range
------------------------
Brand: Redmi
Model: Note 13
Price: Rs. 15000
Category: Budget
------------------------'''


#6. 

class Vehicle:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    def get_category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def display(self):
        print("Vehicle Number :", self.number)
        print("Brand          :", self.brand)
        print("Price          : Rs.", self.price)
        print("Category       :", self.get_category())
        print("--------------------------------")


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all(self):
        print("\n========== VEHICLE SHOWROOM ==========")
        
        for vehicle in self.vehicles:
            vehicle.display()


# Main Program
showroom = Showroom()

v1 = Vehicle("MH12AB1234", "BMW", 2500000)
v2 = Vehicle("MH14CD5678", "Maruti", 700000)
v3 = Vehicle("MH12EF9012", "Toyota", 1500000)

showroom.add_vehicle(v1)
showroom.add_vehicle(v2)
showroom.add_vehicle(v3)

showroom.display_all()


#output
'''========== VEHICLE SHOWROOM ==========

Vehicle Number : MH12AB1234
Brand          : BMW
Price          : Rs. 2500000
Category       : Luxury
--------------------------------
Vehicle Number : MH14CD5678
Brand          : Maruti
Price          : Rs. 700000
Category       : Economy
--------------------------------
Vehicle Number : MH12EF9012
Brand          : Toyota
Price          : Rs. 1500000
Category       : Luxury
--------------------------------'''