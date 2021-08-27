import json
from json import JSONEncoder

class Bike:
    def __init__(self, name, displacement, price):
        self.name = name
        self.displacement = displacement
        self.price = price

class BikeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

bike = Bike("Yamaha YZF R1 ", "1000", 40000)

vehicleJson = json.dumps(bike, indent=2, cls=BikeEncoder)
print(vehicleJson)

# --------
# Result:
# ------------------------------------------------------
# {
#   "name": "Yamaha YZF R1 ",
#   "displacement": "1000",
#   "price": 40000
# }
# ------------------------------------------------------