def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    trips = 0
    current_weight = 0
    start = 0
    for index, person_weight in enumerate(people_weight):
        current_weight+= person_weight
        if current_weight > max_weight or len(people_weight[start:index]) >= max_people:
            trips += len(set(people_floors[start:index])) + 1
            current_weight = person_weight
            start = index

    if len(people_weight) > 0 and len(people_floors) > 0:
        trips += len(set(people_floors[start:])) + 1

    return trips