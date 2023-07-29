import os

def open_file(city):
    """
    Opens the data file for the given city and returns the data as a list of lines.
    Args:
        city (str): The name of the city.
    Returns:
        list: The data as a list of lines, or None if the file doesn't exist.
    """
    file_path = f"{city}Case.txt"
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        return None
    except Exception as e:
        print("An error occurred while opening the file:", e)
        return None

def validate_city(city):
    """
    Validates if the entered city has a corresponding data file.

    Args:
        city (str): The name of the city.

    Returns:
        bool: True if the city is valid and has a data file, False otherwise.
    """
    try:
        # Get the list of available data files (cities)
        data_files = [file_name.split('Case.txt')[0] for file_name in os.listdir() if file_name.endswith('Case.txt')]

        if city in data_files:
            return True
        else:
            print("Invalid city. Available cities: ", data_files)
            return False
    except Exception as e:
        print("An error occurred while validating the city:", e)
        return False


def compute_total_confirmed(data):
    """
    Computes the total number of confirmed cases from the data.

    Args:
        data (list): The data as a list of lines.

    Returns:
        int: The total number of confirmed cases.
    """
    total_confirmed = 0

    try:
        for line in data[1:]:
            line_data = line.strip().split(',')
            confirmed_cases = int(line_data[1])
            total_confirmed += confirmed_cases

        return total_confirmed
    except Exception as e:
        print("An error occurred while computing the total confirmed cases:", e)
        return 0


def display_data(data):
    """
    Displays the COVID-19 cases data for the city.

    Args:
        data (list): The data as a list of lines.

    Returns:
        dict: A dictionary containing the COVID-19 cases data for each barangay.
    """
    city_data = {}

    try:
        for line in data[1:]:
            line_data = line.strip().split(',')
            brgy = line_data[0]
            confirmed = int(line_data[1])
            active = int(line_data[2])
            recovered = int(line_data[3])
            suspect = int(line_data[4])
            probable = int(line_data[5])
            deceased = int(line_data[6])

            city_data[brgy] = {
                'confirmed': confirmed,
                'active': active,
                'recovered': recovered,
                'suspect': suspect,
                'probable': probable,
                'deceased': deceased
            }

        return city_data
    except Exception as e:
        print("An error occurred while displaying the data:", e)
        return {}


def update_case(city, data, brgy):
    """
    Updates the COVID-19 case data for a specific barangay.

    Args:
        data (list): The data as a list of lines.
        brgy (str): The name of the barangay to update.

    Returns:
        bool: True if the update is successful, False otherwise.
    """
    try:
        for i in range(1, len(data)):
            line_data = data[i].strip().split(',')
            if line_data[0] == brgy:
                print("*" * 65)
                print("=" * 65)
                print(f"Updating data for {brgy}:")
                print("Which aspect of the data do you want to update?")
                print("1. Confirmed")
                print("2. Active")
                print("3. Recovered")
                print("4. Suspect")
                print("5. Probable")
                print("6. Deceased")
                choice = int(input("Enter your choice (1-6): "))
                print("=" * 65)
                print("*" * 65)
                if 1 <= choice <= 6:
                    value = int(input(f"Enter the value to add: "))
                    category = ['confirmed', 'active', 'recovered', 'suspect', 'probable', 'deceased'][choice - 1]

                    if category == 'recovered':
                        active_index = 2
                        recovered_index = 3
                        active_cases = int(line_data[active_index])
                        recovered_cases = int(line_data[recovered_index])
                        if value > active_cases:
                            print("Error: Recovered cases cannot exceed active cases.")
                            return False
                        line_data[recovered_index] = str(recovered_cases + value)
                        line_data[active_index] = str(active_cases - value)
                    else:
                        line_data[choice] = str(int(line_data[choice]) + value)

                    data[i] = ','.join(line_data) + '\n'
                    with open(f"{city}Case.txt", 'w') as file:
                        file.writelines(data)
                    print(f"Data updated for {brgy}.")
                    print("=" * 65)
                    return True
                else:
                    print("Invalid choice.")
                    return False
        print(f"No data found for {brgy}.")
        return False
    except Exception as e:
        print("An error occurred while updating the data:", e)
        return False

def add_or_delete_case(city, data, brgy, mode):
    """
    Adds or deletes the COVID-19 case data for a specific barangay.
    Args:
        data (list): The data as a list of lines.
        brgy (str): The name of the barangay to add or delete.
        mode (str): 'add' or 'delete' to specify the operation.
    Returns:
        bool: True if the operation is successful, False otherwise.
    """
    try:
        if mode == 'add':
            for line in data[1:]:
                line_data = line.strip().split(',')
                if line_data[0] == brgy:
                    print(f"Data already exists for {brgy}. Cannot add.")
                    return False
            print(f"Adding new data for {brgy}:")
            print("Enter the case numbers:")
            confirmed = int(input("Confirmed: "))
            active = int(input("Active: "))
            recovered = int(input("Recovered: "))
            suspect = int(input("Suspect: "))
            probable = int(input("Probable: "))
            deceased = int(input("Deceased: "))
            new_data = f"{brgy},{confirmed},{active},{recovered},{suspect},{probable},{deceased}\n"
            data.append(new_data)
            with open(f"{city}Case.txt", 'w') as file:
                file.writelines(data)
            print(f"Data added for {brgy}.")
            return True
        elif mode == 'delete':
            for i in range(1, len(data)):
                line_data = data[i].strip().split(',')
                if line_data[0] == brgy:
                    del data[i]
                    with open(f"{city}Case.txt", 'w') as file:
                        file.writelines(data)
                    print(f"Data deleted for {brgy}.")
                    return True
            print(f"No data found for {brgy}.")
            return False
        else:
            print("Invalid mode. Please choose 'add' or 'delete'.")
            return False
    except Exception as e:
        print("An error occurred while adding or deleting the data:", e)
        return False

def create_new_case(city):
    """
    Creates a new data file for a city.
    Args:
        city (str): The name of the city.
    Returns:
        bool: True if the data file is created successfully, False otherwise.
    """
    try:
        file_path = f"{city}Case.txt"
        if os.path.exists(file_path):
            print(f"Data file for {city} already exists.")
            return False
        with open(file_path, 'w') as file:
            header = "BRGY,CONFIRMED,ACTIVE,RECOVERED,SUSPECT,PROBABLE,DECEASED\n"
            file.write(header)
        print(f"Data file created for {city}.")
        return True
    except Exception as e:
        print("An error occurred while creating the data file:", e)
        return False

def main():
    """
    The main function that prompts the user for choices and performs the selected operations.
    """
    print("Data Management")
    while True:
        try:
            print("=" * 65)
            print("\nMenu:")
            print("1. Display Case")
            print("2. Update Case")
            print("3. Add or Delete Case")
            print("4. Create New Case")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            print("=" * 65)

            if choice == '1':
                city = input("Enter a city: ")
                while not validate_city(city):
                    city = input("Enter a city: ")
                data = open_file(city)
                if data is None:
                    print(f"No data available for {city} yet.")
                else:
                    print("=" * 65)
                    print(f"The Cases in {city}:")
                    print("=" * 65)
                    city_data = display_data(data)
                    for brgy, stats in city_data.items():
                        print("=" * 65)
                        print(f"{brgy}:")
                        print("=" * 65)
                        for category, value in stats.items():
                            print(f"{category}: {value}")
                    total_confirmed = compute_total_confirmed(data)
                    print("\nTotal Confirmed Cases:", total_confirmed)

            elif choice == '2':
                city = input("Enter a city: ")
                while not validate_city(city):
                    city = input("Enter a city: ")
                data = open_file(city)
                if data is None:
                    print(f"No data available for {city} yet.")
                else:
                    brgy = input("Enter the barangay to update: ")
                    update_case(city, data, brgy)

            elif choice == '3':
                city = input("Enter a city: ")
                while not validate_city(city):
                    city = input("Enter a city: ")

                data = open_file(city)
                if data is None:
                    print(f"No data available for {city} yet.")
                else:
                    print("=" * 65)
                    mode = input("Enter 'add' or 'delete': ")
                    brgy = input("Enter the barangay: ")
                    print("=" * 65)
                    add_or_delete_case(city, data, brgy, mode)

            elif choice == '4':
                city = input("Enter a new city: ")
                create_new_case(city)

            elif choice == '5':
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except Exception as e:
            print("An error occurred:", e)


if __name__ == '__main__':
    main()
