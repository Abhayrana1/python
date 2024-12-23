# Hotel Room Booking Manager

def display_summary(rooms):
    """Display a summary of available and booked rooms."""
    available_rooms = rooms.count("Available")
    booked_rooms = rooms.count("Booked")
    print(f"\nSummary:\nAvailable Rooms: {available_rooms}\nBooked Rooms: {booked_rooms}\n")

def check_availability(rooms):
    """Display the availability of all rooms."""
    print("\nRoom Status:")
    for i, status in enumerate(rooms, start=1):
        print(f"Room {i}: {status}")

def book_room(rooms):
    """Allow the user to book an available room."""
    try:
        room_number = int(input("Enter the room number to book: "))
        if 1 <= room_number <= len(rooms):
            if rooms[room_number - 1] == "Available":
                rooms[room_number - 1] = "Booked"
                print(f"Room {room_number} has been successfully booked.")
            else:
                print(f"Room {room_number} is already booked.")
        else:
            print("Invalid room number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid room number.")

def cancel_booking(rooms):
    """Allow the user to cancel a room booking."""
    try:
        room_number = int(input("Enter the room number to cancel booking: "))
        if 1 <= room_number <= len(rooms):
            if rooms[room_number - 1] == "Booked":
                rooms[room_number - 1] = "Available"
                print(f"Booking for Room {room_number} has been successfully canceled.")
            else:
                print(f"Room {room_number} is not currently booked.")
        else:
            print("Invalid room number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid room number.")

def main():
    """Main function to manage the hotel room bookings."""
    number_of_rooms = 10
    rooms = ["Available"] * number_of_rooms

    while True:
        print("\nHotel Room Booking Manager")
        print("1. Check Room Availability")
        print("2. Book a Room")
        print("3. Cancel a Booking")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                check_availability(rooms)
            elif choice == 2:
                book_room(rooms)
            elif choice == 3:
                cancel_booking(rooms)
            elif choice == 4:
                print("Thank you for using the Hotel Room Booking Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

            display_summary(rooms)

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
