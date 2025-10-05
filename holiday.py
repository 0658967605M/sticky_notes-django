# User inputs for holiday cost calculation

city_flights = ("New York", "Los Angeles", "Chicago", "Miami", "Dallas")
flight_costs = {
    "New York": 300, "Los Angeles": 450,
    "Chicago": 250, "Miami": 550, "Dallas": 380
    }

# Create the functions for each cost calculation


def hotel_cost(num_nights):
    return num_nights * 140

def plane_cost(city):
    # Make city case-insensitive and strip whitespace
    city = city.title().strip()
    return flight_costs.get(city, 0)

def rental_car_cost(rental_days):
    cost = rental_days * 100
    if rental_days >= 7:
        cost -= 100
    elif rental_days >= 3:
        cost -= 50
    return cost

# '''Calculate a user’s total holiday cost, which includes
# the plane cost, hotel cost, and car rental cost.'''

def holiday_cost(city, rental_days, num_nights):
    return plane_cost(city) + rental_car_cost(rental_days)\
     + hotel_cost(num_nights)

print("Available flight options:", ", ".join(city_flights))
city = input("Enter the city you are flying to: ")
if city.title().strip() not in city_flights:
    print("City not recognized. Please choose from:", ", ".join(city_flights))
else:
    rental_days = int(
        input("Enter the number of days you will rent the car: ")
        )
    num_nights = int(
        input("Enter the number of nights you will stay at the hotel: ")
    )

    print(f"Your hotel cost is: {hotel_cost(num_nights)}")
    print(f"Your flight cost is: {plane_cost(city)}")
    print(f"Your rental car cost is: {rental_car_cost(rental_days)}")
    print(
        f"Your total holiday cost is: {holiday_cost(city, rental_days, num_nights)}"
        )
