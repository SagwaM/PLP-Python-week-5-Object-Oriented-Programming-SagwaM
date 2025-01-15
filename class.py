# Base class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def check_battery(self):
        print(f"Battery life remaining: {self.battery_life}%")

# Inherited class representing a GamingPhone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, gaming_performance):
        # Calling the constructor of the parent class (Smartphone)
        super().__init__(brand, model, battery_life)
        self.gaming_performance = gaming_performance

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gaming_performance} performance!")

# Creating instances of Smartphone and GamingPhone
smartphone = Smartphone("Apple", "iPhone 14", 80)
gaming_phone = GamingPhone("Asus", "ROG Phone 5", 90, "High")

# Using methods from both classes
smartphone.make_call("1234567890")
smartphone.send_message("1234567890", "Hello!")
smartphone.check_battery()

gaming_phone.make_call("9876543210")
gaming_phone.play_game("PUBG Mobile")
gaming_phone.check_battery()
