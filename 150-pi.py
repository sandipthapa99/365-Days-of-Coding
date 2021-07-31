from math import radians, sin, cos, acos

print("Coordinates of two points:")
start_lon = radians(float(input("Starting longitude: ")))
start_lat = radians(float(input("Starting latitude: ")))
end_lon = radians(float(input("Ending longitude: ")))
end_lat = radians(float(input("Ending latitude: ")))

distance = 6371.01 * acos(sin(start_lat)*sin(end_lat) +
 cos(start_lat)*cos(end_lat)*cos(start_lon - end_lon))
print(f"The distance is {distance} KM ")

# --------------------------------------------------------
# Input:
# # Starting point
# 27.71, 85.30
# # Ending point
# 27.69, 85.28
# --------------------------------------------------------
# Result:
# 2.24 KM