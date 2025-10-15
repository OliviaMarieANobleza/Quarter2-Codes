def calculate_delivery_fee(distance_km, rate_per_km):
    return distance_km * rate_per_km

distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer in php: "))
print(f"Total Delivery Fee: ₱{calculate_delivery_fee(distance, rate):.2f}")
