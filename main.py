# main.py
#
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox

# שלב מחזור החיים של חיית המחמד
class LifeStage:
    BABY = 'Baby'
    CHILD = 'Child'
    TEENAGER = 'Teenager'
    ADULT = 'Adult'
    SENIOR = 'Senior'
    SPECIAL = 'Special'
    ALL_STAGES = [BABY, CHILD, TEENAGER, ADULT, SENIOR, SPECIAL]

# מחלקת הבסיס לחיות מחמד
class Pet(ABC):
    def __init__(self, name, root):
        self.name = name
        self.hunger = 50  # ערך התחלתי
        self.happiness = 50  # ערך התחלתי
        self.training = 0  # ערך התחלתי
        self.sickness = 0  # ערך התחלתי
        self.stage = LifeStage.BABY  # התחל מ-Baby
        self.age = 0  # Added to track age
        self.root = root  # Save reference to the Tkinter root

    @abstractmethod
    def eat(self, amount):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def exercise(self):
        pass

    @abstractmethod
    def play(self):
        pass

    def age_up(self):
        stages = LifeStage.ALL_STAGES
        current_index = stages.index(self.stage)
        if current_index < len(stages) - 1:
            self.stage = stages[current_index + 1]
            self.age += 1
            messagebox.showinfo("Life Stage Update", f"{self.name} has grown to {self.stage}!")
        else:
            messagebox.showinfo("Life Stage Update", f"{self.name} is already at the highest life stage!")

    def increase_sickness(self):
        if self.sickness < 100:
            self.sickness = min(self.sickness + 2, 100)  # Increase sickness by 2
        if self.sickness >= 100:
            self.sickness = 100
            self.die()

    def die(self):
        messagebox.showinfo("Game Over", f"{self.name} has died due to illness!")
        self.root.quit()  # Close the Tkinter application
        exit()  # Ensure the script stops running

    def __str__(self):
        return (f"Pet: {self.__class__.__name__}\n"
                f"Name: {self.name}\n"
                f"LifeStage: {self.stage}\n"
                f"Hunger: {self.hunger}\n"
                f"Happiness: {self.happiness}\n"
                f"Training: {self.training}\n"
                f"Sickness: {self.sickness}")

# מחלקות חיות שונות
class Unicorn(Pet):
    def __init__(self, name, root):
        super().__init__(name, root)

    def eat(self, amount):
        self.hunger = min(self.hunger + amount, 100)

    def sleep(self):
        self.happiness = min(self.happiness + 10, 100)

    def exercise(self):
        self.training = min(self.training + 10, 100)

    def play(self):
        self.happiness = min(self.happiness + 10, 100)

class Dog(Pet):
    def __init__(self, name, root):
        super().__init__(name, root)

    def eat(self, amount):
        self.hunger = min(self.hunger + amount, 100)

    def sleep(self):
        self.happiness = min(self.happiness + 10, 100)

    def exercise(self):
        self.training = min(self.training + 10, 100)

    def play(self):
        self.happiness = min(self.happiness + 10, 100)

class Cat(Pet):
    def __init__(self, name, root):
        super().__init__(name, root)

    def eat(self, amount):
        self.hunger = min(self.hunger + amount, 100)

    def sleep(self):
        self.happiness = min(self.happiness + 10, 100)

    def exercise(self):
        self.training = min(self.training + 10, 100)

    def play(self):
        self.happiness = min(self.happiness + 10, 100)

class Lion(Pet):
    def __init__(self, name, root):
        super().__init__(name, root)

    def eat(self, amount):
        self.hunger = min(self.hunger + amount, 100)

    def sleep(self):
        self.happiness = min(self.happiness + 10, 100)

    def exercise(self):
        self.training = min(self.training + 10, 100)

    def play(self):
        self.happiness = min(self.happiness + 10, 100)

# מחלקת בסיס לפקודות
class PetCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

# פקודות קונקרטיות
class EatCommand(PetCommand):
    def __init__(self, pet, amount):
        self.pet = pet
        self.amount = amount

    def execute(self):
        self.pet.eat(self.amount)

class SleepCommand(PetCommand):
    def __init__(self, pet):
        self.pet = pet

    def execute(self):
        self.pet.sleep()

class ExerciseCommand(PetCommand):
    def __init__(self, pet):
        self.pet = pet

    def execute(self):
        self.pet.exercise()

class PlayCommand(PetCommand):
    def __init__(self, pet):
        self.pet = pet

    def execute(self):
        self.pet.play()

# מחלקת ניהול הפקודות
class CommandInvoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()
        self.commands = []  # Clear commands after execution

class PetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tamagotchi Game")

        self.pet = None
        self.command_invoker = CommandInvoker()

        self.create_widgets()

    def create_widgets(self):
        # Frame for choosing pet type
        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.pack()

        tk.Label(self.choice_frame, text="Select Pet Type:").pack()

        self.pet_type_buttons = {}
        pet_types = ["Unicorn", "Dog", "Cat", "Lion"]
        for pet_type in pet_types:
            button = tk.Button(self.choice_frame, text=pet_type, width=20, height=2,
                               command=lambda pt=pet_type: self.select_pet_type(pt))
            button.pack(pady=5)
            self.pet_type_buttons[pet_type] = button

        # Frame for entering pet name
        self.name_frame = None

        # Frame for showing pet information
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack()

        self.info_label = tk.Label(self.info_frame, text="")
        self.info_label.pack()

        # Buttons for pet actions
        self.action_buttons_frame = tk.Frame(self.root)
        self.action_buttons_frame.pack()

        self.feed_button = tk.Button(self.action_buttons_frame, text="Feed", command=self.feed_pet)
        self.sleep_button = tk.Button(self.action_buttons_frame, text="Sleep", command=self.sleep_pet)
        self.exercise_button = tk.Button(self.action_buttons_frame, text="Exercise", command=self.exercise_pet)
        self.play_button = tk.Button(self.action_buttons_frame, text="Play", command=self.play_pet)

        self.feed_button.pack()
        self.sleep_button.pack()
        self.exercise_button.pack()
        self.play_button.pack()

        self.hide_action_buttons()

    def select_pet_type(self, pet_type):
        # Hide the choice frame and show the name entry
        self.choice_frame.pack_forget()

        if self.name_frame:
            self.name_frame.destroy()

        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack()

        tk.Label(self.name_frame, text=f"Enter Name for {pet_type}:").pack()
        self.pet_name_entry = tk.Entry(self.name_frame)
        self.pet_name_entry.pack()

        tk.Button(self.name_frame, text="Create Tamagotchi", command=lambda: self.create_pet(pet_type)).pack()

    def create_pet(self, pet_type):
        name = self.pet_name_entry.get()

        if name:
            if pet_type == "Unicorn":
                self.pet = Unicorn(name, self.root)
            elif pet_type == "Dog":
                self.pet = Dog(name, self.root)
            elif pet_type == "Cat":
                self.pet = Cat(name, self.root)
            elif pet_type == "Lion":
                self.pet = Lion(name, self.root)

            self.update_info()
            self.name_frame.pack_forget()  # Hide the name entry frame
            self.show_action_buttons()
            self.start_life_cycle()  # Start the life cycle timer
            self.start_sickness_increase()  # Start the sickness timer
        else:
            messagebox.showerror("Error", "Please enter a name for the pet")

    def feed_pet(self):
        if self.pet:
            self.command_invoker.add_command(EatCommand(self.pet, 10))
            self.command_invoker.execute_commands()
            self.update_info()
        else:
            messagebox.showerror("Error", "No pet created yet")

    def sleep_pet(self):
        if self.pet:
            self.command_invoker.add_command(SleepCommand(self.pet))
            self.command_invoker.execute_commands()
            self.update_info()
        else:
            messagebox.showerror("Error", "No pet created yet")

    def exercise_pet(self):
        if self.pet:
            self.command_invoker.add_command(ExerciseCommand(self.pet))
            self.command_invoker.execute_commands()
            self.update_info()
        else:
            messagebox.showerror("Error", "No pet created yet")

    def play_pet(self):
        if self.pet:
            self.command_invoker.add_command(PlayCommand(self.pet))
            self.command_invoker.execute_commands()
            self.update_info()
        else:
            messagebox.showerror("Error", "No pet created yet")

    def update_info(self):
        if self.pet:
            info = str(self.pet)
            self.info_label.config(text=info)

    def hide_action_buttons(self):
        self.feed_button.pack_forget()
        self.sleep_button.pack_forget()
        self.exercise_button.pack_forget()
        self.play_button.pack_forget()

    def show_action_buttons(self):
        self.feed_button.pack()
        self.sleep_button.pack()
        self.exercise_button.pack()
        self.play_button.pack()

    def start_life_cycle(self):
        # Initialize the life cycle update
        self.life_stage_update_time = self.root.after(20000, self.update_life_stage)  # Start after 20 seconds

    def update_life_stage(self):
        if self.pet:
            self.pet.age_up()
            self.update_info()
            # Continue updating life stage every 20 seconds
            self.life_stage_update_time = self.root.after(20000, self.update_life_stage)

    def start_sickness_increase(self):
        # Initialize the sickness update
        self.sickness_update_time = self.root.after(1000, self.update_sickness)  # Start after 1 second

    def update_sickness(self):
        if self.pet:
            self.pet.increase_sickness()
            self.update_info()
            # Continue updating sickness every second
            if self.pet.sickness < 100:  # Only continue if not dead
                self.sickness_update_time = self.root.after(1000, self.update_sickness)

def main():
    root = tk.Tk()
    app = PetApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
