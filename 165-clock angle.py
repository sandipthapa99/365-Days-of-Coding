def clockAngle(hour, min):
    # angle of the hour's hand from 0 degree
    # each hour makes 30 degree angle
    h = (hour+(min/60))*30
 
    # angle of the minute's hand from 0 degree
    m = (min * 360) / (60)
 
    # angle difference
    angle = abs(h - m)
 
    # returning shorter angle
    if angle > 180:
        angle = 360 - angle
 
    return angle
 
# Clock Angle Problem
if __name__ == '__main__':
    hour = 12
    min = 13
    print("{:.2f} Degrees".format(clockAngle(hour, min)))

# --------
# Result:
# ----------------------------------------------------------
# 71.50 Degrees
# ----------------------------------------------------------