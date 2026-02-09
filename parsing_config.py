from typing import Dict, Any


def read_file() -> dict[str, str]:
    try:
        with open("config.txt", "r") as file:
            my_dict = {}
            for line in file:
                key, value = line.strip().split("=")
                my_dict[key] = value
            return my_dict
    except FileNotFoundError:
        print("Error: Configuration file 'config.txt' not found.")
        return {}


def filter_config_data(config: dict[str, str]) -> dict[str, Any]:
    good_dict = {}
    for key, value in config.items():
        if key == 'WIDTH':
            try:
                width = int(value)
            except ValueError:
                raise ValueError("'WIDTH' must be an integer")
            if width <= 0:
                raise ValueError("'WIDTH' value cannot be negative!")
            good_dict[key] = width
        elif key == 'HEIGHT':
            if int(value) > 0:
                good_dict[key] = int(value)
            else:
                return "HEIGHT value cannot be negative!"
        elif key == 'HEIGHT' and int(value) < 0:
            return "Error: HEIGHT value cannot be negative!"
        elif key == 'ENTRY':
            entry_tuple = tuple(int(x) for x in value.split(","))
            if (len(entry_tuple) == 2):
                good_dict[key] = entry_tuple
            else:
                return "Error: Invalid data in 'ENTRY' input in 'config.txt'"
        elif key == 'EXIT':
            exit_tuple = tuple(int(y) for y in value.split(","))
            if (len(exit_tuple) == 2):
                good_dict[key] = exit_tuple
            else:
                return "Error: Invalid data in 'EXIT' in 'config.txt'"
        elif key == 'OUTPUT_FILE':
            if value == 'maze.txt':
                good_dict[key] = value
            else:
                return "Error: Invalid data in 'OUTPUT_FILE' in 'config.txt'"
        val = value.strip().upper()
        if key == 'PERFECT':
            if val == "TRUE":
                good_dict[key] = True
            elif val == "FALSE":
                good_dict[key] = False
            else:
                return "Error: Invalid data in 'PERFECT' boolean stats!"
        else:
            continue
        return good_dict

try:
    print(filter_config_data(read_file()))
except ValueError as e:
    print(f"Error: {e}")
