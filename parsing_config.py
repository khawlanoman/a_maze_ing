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
    try:
        good_dict = {}
        for key, value in config.items():
            if key == 'WIDTH':
                good_dict[key] = int(value)
            elif key == 'HEIGHT':
                good_dict[key] = int(value)
            elif key == 'ENTRY':
                good_dict[key] = tuple(int(x) for x in value.split(","))
            elif key == 'EXIT':
                good_dict[key] = tuple(int(y) for y in value.split(","))
            elif key == 'OUTPUT_FILE' and value == 'maze.txt':
                good_dict[key] = value
            val = value.strip().upper()
            if key == 'PERFECT':
                if val == "TRUE":
                    good_dict[key] = True
                elif val == "FALSE":
                    good_dict[key] = False
            else:
                continue
        return good_dict
    except ValueError:
        print("Error: invalid data in 'config.txt' file.")


print(filter_config_data(read_file()))
