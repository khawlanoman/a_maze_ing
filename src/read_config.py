def read_config():
    required = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
    data = {}

    try:
        with open("config.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: 'config.txt' not found")
        exit(1)

    found_keys = set()
    for raw_line in lines:
        line = raw_line.strip()
        if not line or "=" not in line:
            print("Error: Invalid data in 'config.txt'")
            exit(1)

        key, value = line.split("=", 1)
        key = key.strip().upper()
        value = value.strip()

        if key not in required:
            print(f"Error: Unknown key '{key}'")
            exit(1)

        if key in found_keys:
            print(f"Error: Duplicate key '{key}' in 'config.txt'")
            exit(1)

        found_keys.add(key)

        if key == "WIDTH":
            if value == "":
                print("Error: 'WIDTH' has no value!")
                exit(1)

            value = value.replace(" ", "")
            try:
                width = int(value)
            except ValueError:
                print("Error: 'WIDTH' must be an integer!")
                exit(1)
            if width <= 0:
                print("Error: 'WIDTH' must be greater than 0!")
                exit(1)
            data["WIDTH"] = width

        elif key == "HEIGHT":
            if value == "":
                print("Error: 'HEIGHT' has no value!")
                exit(1)
            value = value.replace(" ", "")
            try:
                height = int(value)
            except ValueError:
                print("Error: 'HEIGHT' must be an integer!")
                exit(1)
            if height <= 0:
                print("Error: 'HEIGHT' must be greater than 0!")
                exit(1)
            data["HEIGHT"] = height

        elif key in {"ENTRY", "EXIT"}:
            if value == "":
                print(f"Error: '{key}' coordinates cannot be empty!")
                exit(1)
            parts = value.split(",")
            if len(parts) != 2:
                print(f"Error: '{key}' must contain exactly two numbers!")
                exit(1)
            try:
                x = int(parts[0].strip())
                y = int(parts[1].strip())
                if x >= data["WIDTH"] or y >= data["HEIGHT"]:
                    print(f"Error: in '{key}' coordinates {x, y} must be less than 'WIDTH' value")
                    exit(1)
            except ValueError:
                print(f"Error: '{key}' coordinates must be integers!")
                exit(1)
            if x < 0 or y < 0:
                print(f"Error: Negative number in '{key}' coordinates!")
                exit(1)
            data[key] = (x, y)
            if "ENTRY" in data and "EXIT" in data:
                if data["ENTRY"] == data["EXIT"]:
                    print("Error: 'ENTRY' and 'EXIT' must have different coordinate!")
                    exit(1)
        elif key == "OUTPUT_FILE":
            if value.lower() != "maze.txt":
                print("Error: 'OUTPUT_FILE' must be 'maze.txt'")
                exit(1)

            data["OUTPUT_FILE"] = "maze.txt"
        elif key == "PERFECT":
            value = value.upper()

            if value not in {"TRUE", "FALSE"}:
                print("Error: 'PERFECT' must be TRUE or FALSE")
                exit(1)

            data["PERFECT"] = value
    missing = required - found_keys
    if missing:
        print(f"Error: Missing key(s): {', '.join(missing)}")
        exit(1)

    return data
