# Minimum Angle between hour and minute hand of clock at a given time

def Hour_And_Minute_Angle(hour, minute):
    hour_angle = 30 * hour + 0.5 * minute 
    minute_angle = 6 * minute 
    
    angle = abs(minute_angle - hour_angle)

    angle = min(angle, 360 - angle)
    return angle 

hour = 3                                                     #TC = O(1)
minute = 15                                                  #SC = O(1)
print(Hour_And_Minute_Angle(hour, minute))





