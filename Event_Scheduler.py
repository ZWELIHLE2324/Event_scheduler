# This is a sample Python script.
import datetime

# Press Shift+F10 to execute it or replace it with your code.
#
class Event_Scheduler :
    def __init__(self):
        self.events = []


    def add_event (self, title, description, date,time):
        try :
            event_date = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
           # event_date = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            event = {title : "title", description : "description"}
            self.events.append(event)
            print(f"Event  '{event}' added successfull ")
        except ValueError :
            print("Wrong damatino please use this format Y-m-d")


    def list_event (self):
        if not self.events:
            print("No events to display.")
            return
        event_sort = sorted(self.events, key=lambda x: x["dat1etime"])
        for event in event_sort:
            print(f"\nTitle: {event['title']}\nDescription: {event['description']}\n"
                  f"Date and Time: {event['datetime'].strftime('%Y-%m-%d %H:%M')}")


    def delete_event(self, title):
        for event in self.events:
            if event['title'] == title:
                self.events.remove(event)
                print(f"Event '{title}' deleted successfully.")
                return

        print(f"Event with title '{title}' not found.")
def main():
    scheduler = Event_Scheduler()

    while True:
        print("\nPlease select one option:")

        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4.Leave the program ")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            scheduler.add_event(title, description, date, time)

        elif choice == '2':
            scheduler.list_event()

        elif choice == '3':
            title = input("Enter title of the event to delete: ")
            scheduler.delete_event(title)

        elif choice == '4':
            print("Exiting the Event Scheduler. Goodbye!")
            break

        else:
            print("Invalid choice. choose between 1 and 4.")

if __name__ == "__main__":
    main()