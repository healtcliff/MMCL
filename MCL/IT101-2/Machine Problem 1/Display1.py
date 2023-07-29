import os
#courtesy of Marc Kennel M. Angeles with the help of stockoverflow and github
def open_file(city):
    """
    Opens the data file for the given city and returns the data as a list of lines.

    Args:
        city (str): The name of the city.

    Returns:
        list: The data as a list of lines, or None if the file doesn't exist.
    """
    file_path = f"{city}Case.txt"

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.readlines()
        return data
    else:
        return None


def validate_city(city):
    """
    Validates if the entered city has a corresponding data file.

    Args:
        city (str): The name of the city.

    Returns:
        bool: True if the city is valid and has a data file, False otherwise.
    """
    # Get the list of available data files (cities)
    data_files = [file_name.split('Case.txt')[0] for file_name in os.listdir() if file_name.endswith('Case.txt')]

    if city in data_files:
        return True
    else:
        print("Invalid city. Available cities: ", data_files)
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

    for line in data[1:]:
        line_data = line.strip().split(',')
        confirmed_cases = int(line_data[1])
        total_confirmed += confirmed_cases

    return total_confirmed


def display_data(data):
    """
    Displays the COVID-19 cases data for the city.

    Args:
        data (list): The data as a list of lines.

    Returns:
        dict: A dictionary containing the COVID-19 cases data for each barangay.
    """
    city_data = {}

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


def main():
    """
    The main function that prompts the user for a city, validates it, and displays the COVID-19 cases data.
    """
    city = input("Enter a city: ")
    while not validate_city(city):
        city = input("Enter a city: ")

    data = open_file(city)
    if data is None:
        print(f"No data available for {city} yet.")
        return
    print("*" *30)
    print("="*30)
    print(f"\nCOVID-19 Cases in {city}:")
    print("="*30)
    print("*" *30)
    city_data = display_data(data)
    for brgy, stats in city_data.items():
        print("=" *30)
        print(f"\n{brgy}:")
        print("=" *30)
        for category, value in stats.items():
            print(f"{category}: {value}")

    total_confirmed = compute_total_confirmed(data)
    print("=" *30)
    print("\nTotal Confirmed Cases:", total_confirmed)
    print("=" *30)


if __name__ == '__main__':
    main()