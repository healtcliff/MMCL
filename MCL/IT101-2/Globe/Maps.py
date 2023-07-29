import os
import tkinter as tk
from PIL import Image, ImageTk
"""
Country Flag Viewer
This program is a simple tkinter application that allows the user to view flags of various countries grouped by continents.
The application features three main sections:
    1. Continent Selection: The user can select a continent using radio buttons.
    2. Country List: A list of countries belonging to the selected continent is displayed in a listbox.
    3. Flag Display: When the user clicks on a specific country in the listbox, the corresponding flag will be shown.

Data:
    - The 'continents' dictionary contains continents as keys, and the values are lists of countries belonging to each continent.

Functionality:
    - The application loads the default continent (Asia) and displays the list of Asian countries upon startup.
    - The user can select a different continent using the radio buttons, and the list of countries will be updated accordingly.
    - When a country is selected in the listbox, the program attempts to display its flag image if it exists in the 'Globe/Image' folder.
    - If the flag image is not available, the program creates a text file named '{country_name}_not_found.txt' in the 'Globe/Image' folder.

Icons:
    - The program sets an icon for the main tkinter window using the file 'turtle.ico' located in the 'Image' folder.

Usage:
    - Run the script, and a window will appear with radio buttons for continents, a listbox for countries, and a label for flag display.
    - Choose a continent using the radio buttons to display its countries in the listbox.
    - Click on a country in the listbox to view its flag (if available) in the flag display label.
    - If the flag image is missing, a message will be displayed, and a text file will be created to indicate the missing flag image.

Note:
    - Ensure that the 'Globe/Image' folder exists and contains the country flag images with filenames in lowercase (e.g., 'philippines.png').
    - The 'Image' folder must also contain the 'turtle.ico' file for setting the window icon.
    - os.path.dirname(__file__): This part retrieves the directory name of the current Python script's file. __file__ is a built-in variable that holds the path of the current Python script. os.path.dirname() extracts the directory part of that path.
Author: Marc Kennel M. Angeles
"""

# Data: continents dictionary contains continents as keys, and the values are lists of countries belonging to each continent.
continents = {
    "Asia": ["Philippines", "Malaysia", "Taiwan", "Singapore", "Thailand", "India"],
    "Africa": ["Algeria", "Angola", "Egypt", "Cape Verde", "Liberia", "Kenya", "Morocco", "Nigeria"],
    "America": ["Venezuela", "Peru", "Jamaica", "United States", "Cuba", "Chile", "Argentina"],
    "Europe": ["Russia", "Germany", "United Kingdom", "Italy", "Ukraine", "France", "Belgium"]
}

class CountryFlagApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Angeles Marc Kennel")
        self.root.geometry("500x200")

        # Variables to track the selected continent and country
        self.continent_var = tk.StringVar()
        self.continent_var.set("Asia")  # Set default continent to Asia
        self.country_var = tk.StringVar()
        self.country_var.set(continents["Asia"][0])  # Set default country to the first in the Asia list

        # Frame for displaying continent selection using radio buttons
        frameOne = tk.Frame(self.root, bg='white')
        frameOne.pack(side=tk.TOP, pady=10)

        # Create a list to store the radio buttons
        self.radio_buttons = []

        # Create radio buttons for each continent using your custom code
        n = 0
        for continent in continents.keys():
            self.create_custom_radio(frameOne, text=continent, value=continent)
            n += 1

        # Frame for displaying the list of countries in the selected continent
        frameTwo = tk.Frame(self.root)
        frameTwo.pack(side=tk.LEFT, padx=10)

        # Create a scrollbar and attach it to the listbox
        scrollbar = tk.Scrollbar(frameTwo)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.country_listbox = tk.Listbox(frameTwo, height=5, width=12, yscrollcommand=scrollbar.set, font='times 12')
        self.country_listbox.pack(pady=10)
        scrollbar.config(command=self.country_listbox.yview)

        # Bind the selection event of the listbox to the show_flag method
        self.country_listbox.bind("<<ListboxSelect>>", self.show_flag)

        # Frame for displaying the flag image or error message
        frameThree = tk.Frame(self.root)
        frameThree.pack(side=tk.LEFT, padx=10)
        self.flag_label = tk.Label(frameThree)
        self.flag_label.pack(pady=10)

        # Create a class-level variable to hold a reference to the resized image
        self.flag_image_ref = None

        # Call the update_country_list method to populate the country listbox with countries from the default continent (Asia)
        self.update_country_list()

        # Set the window icon
        IconPath = os.path.join(os.path.dirname(__file__), "Image", "turtle.ico")
        try:
            self.root.iconbitmap(IconPath)
        except tk.TclError:
            print("Icon file not found.")

    def create_custom_radio(self, frame, text, value):
        # Create a custom radio button with your settings
        v = tk.StringVar()
        radio = tk.Radiobutton(frame, text=text, variable=self.continent_var,
                            value=value, bg='white', fg='blue', relief=tk.RIDGE,
                            font='times 14 bold', width=8, command=self.update_country_list)
        radio.grid(row=0, column=len(self.radio_buttons), pady=5)
        self.radio_buttons.append(radio)

    def update_country_list(self):
        # Get the selected continent
        selected_continent = self.continent_var.get()
        # Get the list of countries for the selected continent
        countries = continents[selected_continent]
        # Clear the current items in the country listbox
        self.country_listbox.delete(0, tk.END)
        # Populate the country listbox with the countries for the selected continent
        for country in countries:
            self.country_listbox.insert(tk.END, country)

    def show_flag(self, event):
        # Get the selected country from the listbox
        selected_country = self.country_listbox.get(self.country_listbox.curselection())
        # Create the filename for the flag image based on the selected country
        flag_filename = os.path.join(os.path.dirname(__file__), "Image", selected_country.lower() + ".png")
        try:
            # Try to open and resize the flag image using LANCZOS filter
            flag_image = Image.open(flag_filename)
            # Get the original image size
            original_width, original_height = flag_image.size
            # Calculate the new image size while maintaining the aspect ratio
            new_width = 250
            new_height = int((new_width / original_width) * original_height)
            flag_image = flag_image.resize((new_width, new_height), Image.LANCZOS)
            # Convert the resized image to PhotoImage and store it in the class-level variable
            self.flag_image_ref = ImageTk.PhotoImage(flag_image)
            # Display the image in the label
            self.flag_label.config(image=self.flag_image_ref)
            self.flag_label.config(text="")  # Clear any previous text
        except FileNotFoundError:
            # If the flag image is not found, display an error message
            self.flag_label.config(text="Flag not found.")
            print(f"Flag image not found for {selected_country} (Filename: {os.path.abspath(flag_filename)})")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountryFlagApp(root)
    root.mainloop()
