def read_file():
    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    with open("config.txt", "r") as file:
        lines = file.readlines()

    found_keys = set()
    for line in lines:
        if "=" in line:
            k = line.split("=", 1)[0].strip().upper()
            if k in found_keys and k in required:
                print(f"Error: Duplicate key '{k}' in 'config.txt'")
                exit(1)
            found_keys.add(k)
    for key in required:
        if key not in found_keys:
            print(f"Error: Missing key '{key}' in config.txt")
            exit(1)
    for line in lines:
        line = line.strip()
        if not line or "=" not in line:
            print("Error: Invalid data in 'config.txt'")
            exit(1)
        key, value = line.split("=", 1)
        key = key.strip().upper()
        value = value.strip()
        if key == "WIDTH":
            if value == "":
                print("Error: 'WIDTH' has no value!")
                exit(1)
            value = value.replace(" ", "")
            try:
                x_value = int(value)
                if x_value < 0:
                    print("Error: 'WIDTH' value cannot be negative!")
                    exit(1)
            except ValueError:
                print("Error: 'WIDTH' must be an integer!")
                exit(1)
        elif key == "HEIGHT":
            if value == "":
                print("Error: 'HEIGHT' has no value!")
                exit(1)
            try:
                y_value = int(value)
                if y_value < 0:
                    print("Error: 'HEIGHT' value cannot be negative!")
                    exit(1)
            except ValueError:
                print("Error: 'HEIGHT' must be an integer!")
                exit(1)
        elif key == "ENTRY":
            parts = value.split(",")
            if len(parts) != 2:
                print("Error: 'ENTRY' must have exactly two numbers!")
                exit(1)
            elif value == "":
                print("Error: 'ENTRY' coordinates cannot be empty!")
                exit(1)
            try:
                x, y = map(int, value.split(","))
            except ValueError:
                print("Error: 'ENTRY' coordinates must be two integers!")
                exit(1)
            if x < 0 or y < 0:
                print("Error: Invalid negative number in 'ENTRY' coordinates")
                exit(1)
        elif key == "EXIT":
            parts = value.split(",")
            if len(parts) != 2:
                print("Error: 'EXIT' coordinates must be exactly two integers!")
                exit(1)
            if value == "":
                print("Error: 'EXIT' coordinates cannot be empty!")
                exit(1)
            try:
                x, y = map(int, value.split(","))
            except ValueError:
                print("Error: 'EXIT' coordinates must be two integers!")
                exit(1)
            if x < 0 or y < 0:
                print("Error: Invalid negative number in 'EXIT' coordinates")
                exit(1)
        elif key == "OUTPUT_FILE":
            if value.lower().strip() != "maze.txt":
                print("Error: 'OUTPUT_FILE' value must be 'maze.txt'")
                exit(1)
        elif key == "PERFECT":
            valuee = value.upper()
        else:
            value = "maze.txt"
            if valuee not in ["TRUE", "FALSE"]:
                print("Error: 'PERFECT' value must be True or False")
                exit(1)
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        upper_key = key.upper()
        if upper_key in ["WIDTH", "HEIGHT"]:
            value = value.replace(" ", "")
        elif upper_key in ["ENTRY", "EXIT"]:
            try:
                x, y = map(int, value.split(","))
                value = f"{x},{y}"
            except ValueError:
                pass
        elif upper_key == "OUTPUT_FILE":
            value = value.lower()
        elif upper_key == "PERFECT":
            value = value.upper()
        cleaned_lines.append(f"{upper_key}={value}")
    return "\n".join(cleaned_lines)


print(read_file())