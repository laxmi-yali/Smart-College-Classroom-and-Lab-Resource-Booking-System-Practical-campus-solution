
bookings = []

def book_room(room, time, student):
    for booking in bookings:
        if booking["room"] == room and booking["time"] == time:
            print("Room already booked!")
            return

    bookings.append({
        "room": room,
        "time": time,
        "student": student
    })

    print("Room booked successfully!")

book_room("Lab 1", "10 AM", "Student A")
book_room("Lab 1", "10 AM", "Student B")
book_room("Seminar Hall", "11 AM", "Student C")

print("\nAll Bookings:")

for booking in bookings:
    print(booking)