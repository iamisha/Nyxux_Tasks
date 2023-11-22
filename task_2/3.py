class Car:
    def __init__(self):
        self.car_started = False

    def help(self):
        print("Follow below instructions:")
        print("start - Start the car")
        print("stop - Stop the car")
        print("exit - Close the program")

    def start_car(self):
        if self.car_started:
            print("Car already started")
        else:
            self.car_started = True
            print("Car is started.")

    def stop_car(self):
        if not self.car_started:
            print("Car already stopped")
        else:
            self.car_started = False
            print("Car is stopped.")

car = Car()
car.help()

while True:
    command = input("Enter any command: ").lower()

    if command == "start":
        car.start_car()
    elif command == "stop":
        car.stop_car()
    elif command == "exit":
        exit_command = input("Are you sure you want to exit? (Y/N): ").lower()
        if exit_command == "y":
            print("Exiting the program...")
            break
    else:
        print("Invalid command! Please follow the instructions.")
        car.help()
