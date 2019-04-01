
def gas_stations(distance ,tank_size, stations):
    result = []
    distance_traveled=0
    while True:
        if distance_traveled + tank_size >= distance:
            break
        gas_station = max([station for station in stations
            if station <= distance_traveled + tank_size])
        result.append(gas_station)
        distance_traveled = gas_station    

    return result