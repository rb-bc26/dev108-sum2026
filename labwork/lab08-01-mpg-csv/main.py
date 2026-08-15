
import csv

filename = "trips.csv"

def create_file():
#Opens the file in append mode, which creates it if it doesn't exist."""
    with open(filename, "a", newline="") as file:
        file.write("")

def read_trips():
#Reads the trip data from the CSV file and returns a 2D list of trips."""
    trips = []
    with open(filename, "r", newline="") as file:

        reader = csv.reader(file)
        for row in reader:
         if len(row) > 0:
            distance = float(row[0])
            gallons = float(row[1])
            mpg = float(row[2])
            trips.append(row)
    return trips

def write_trips(trips):
#Writes the entire 2D trips list to the CSV file
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)


def list_trips(trips):
    """Displays the trip data in a table."""
    print()
    print("Distance\tGallons\t\tMPG")
    print("-----------------------------------")

    for i in range (0, len(trips)):
        trip = trips [i]
        print(str(trip[0] + "\t\t" + str(trip[1]  + "\t\t" + str(trip[2]))))
        distance = trip[0]
        gallons = trip[1]
        mpg = trip[2]
    print(f"{distance}\t\t{gallons}\t\t{mpg}")

    print()

def main():
    print("The Miles Per Gallon Program\n")

# Make sure the file exists, then read any trips already stored in it
create_file()
trips = read_trips()

# Display the trips if there are any
if len(trips) > 0:
    list_trips(trips)
more = "y"

while more.lower() == "y":
# Get input from the user
    miles = float(input("Enter miles driven: "))
    gallons = float(input("Enter gallons of gas used: "))

# Calculate MPG
mpg = round(miles / gallons, 2)
print(f"Miles Per Gallon: {mpg}\n")


# Add the new trip to the 2D list
trip = [miles, gallons, mpg]
trips.append(trip)

# Write the updated list back to the CSV file
write_trips(trips)

# Display the updated list of trips
list_trips(trips)
more = input("More entries? (y or n): ")
print()
print("Bye!")

if __name__ == "__main__":
    main()