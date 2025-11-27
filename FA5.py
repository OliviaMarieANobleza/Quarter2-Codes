destinations = []
print("Enter your 5 destinations: ")
for i in range(5):
    dest = input(f"Destination {i+1}: ")
    destinations.append(dest)  

print("Original travel itinerary: ")
for i in range(5):
    print(f"{i+1}. {destinations[i]}")  

print("Lets update your 2nd and 5th destinations.")
destinations[1] = input("Enter new 2nd destination: ")
destinations[4] = input("Enter new 5th destination: ")
print("Updated travel itinerary: ")
for i in range(5):
    print(f"{i+1}. {destinations[i]}")