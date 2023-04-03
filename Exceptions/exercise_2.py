'''
Astronauts limit their water usage to about 11 liters per day. Let's create a function that, depending on the number of astronauts, can calculate how much water will be left after a day
'''

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    
    print(f"Total water left after {days_left} days is: {total_water_left} liters")


water_left(5, 100, 2)