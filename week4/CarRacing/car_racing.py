import json
def main():
    with open('cars.json', 'r') as json_file:
        cars_data = json.load(json_file)
        #returns list of dicts. for each driver we have dict with name, car, model, max_speed
        info = cars_data['people']
        # for participant in info:
        #     car = 

if __name__ == "__main__":
    main()

