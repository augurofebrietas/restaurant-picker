"""
For indecisive people who have trouble choosing somewhere to eat...
Simple GUI program that chooses a restaurant at random from user-inputted list
"""

import tkinter as tk
import random


class App:

    def __init__(self, root):
        """
        set up GUI for restaurant picker
        """

        self.restaurants = []
        self.restaurant_str = ""
        self.count = 1

        self.root = root
        root.title("Food Picker")
        root.geometry("400x500")
        root["bg"] = "lightgray"

        self.title = tk.Label(text="Choose somewhere to eat!", font="Lucida 20 bold",
        background="lightgray", foreground="purple")
        self.title.pack(pady=20)

        self.entry_box = tk.Entry(textvariable=tk.StringVar(), width=40)
        self.entry_box.pack(pady=5)
        self.entry_box.bind("<Return>", self.add_restaurant)

        self.add_button = tk.Button(text="Add restaurant", font="Lucida 10 bold",
        command=self.add_restaurant)
        self.add_button.pack(pady=3)

        self.display = tk.Label(font="Lucida 12", background="lightgray")
        self.display.pack(pady=10)

        self.choice = tk.Label(font="Calibri 18 bold", background="lightgray",
        foreground="green")
        self.choice.pack(pady=8)

        self.choose = tk.Button(text="Choose!", font="Lucida 10 bold",
        command=self.choose, foreground="green")
        self.choose.pack(pady=4)

        self.reset = tk.Button(text="Reset", font="Lucida 10 bold",
        command=self.reset, foreground="red")
        self.reset.pack()

    def add_restaurant(self, event=None):
        """
        on add_button click, gets text from entry box and adds to restaurant list
        also adds to display label and clears entry box
        """

        restaurant = self.entry_box.get()

        if restaurant.strip() != "":
            self.restaurants.append(restaurant)
            self.restaurant_str += f"{self.count}. {restaurant}\n"
            self.display.config(text=self.restaurant_str)
            self.entry_box.delete(0,tk.END)
            self.count += 1
        
    def choose(self):
        """
        choose restaurant at random from user-created list
        """

        if self.restaurants != []:
            choice = random.choice(self.restaurants)
            self.choice.config(text=choice)

    def reset(self):
        """
        resets all variables, clears all GUI elements
        """

        self.restaurants = []
        self.restaurant_str = ""
        self.count = 1

        self.entry_box.delete(0, tk.END)
        self.display.config(text="")
        self.choice.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    root.mainloop()