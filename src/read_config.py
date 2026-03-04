class config_exception(Exception):
    pass


def read_config() -> dict:
    required = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
    data = {}

    try:
        with open("config.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: 'config.txt' not found")
        exit(1)
    try:
        found_keys = set()
        for raw_line in lines:
            line = raw_line.strip()
            if not line:
                continue
            elif "#" in line:
                continue
            elif "=" not in line:
                raise config_exception("Invalid data in 'config.txt'")
            key, value = line.split("=", 1)
            key = key.strip().upper()
            value = value.strip()

            if key not in required:
                raise config_exception(f"Unknown key '{key}'")

            if key in found_keys:
                raise config_exception(f"Duplicate key '{key}' in "
                                       f"'config.txt'")

            found_keys.add(key)
            if key == "WIDTH":
                if value == "":
                    raise config_exception("'WIDTH' has no value!")

                value = value.replace(" ", "")
                try:
                    width = int(value)
                except ValueError:
                    raise config_exception("'WIDTH' value must be an integer!")
                if width <= 0:
                    raise config_exception("'WIDTH' value must be greater"
                                           " than 0!")
                data["WIDTH"] = width

            elif key == "HEIGHT":
                if value == "":
                    raise config_exception("'HEIGHT' has no value!")
                value = value.replace(" ", "")
                try:
                    height = int(value)
                except ValueError:
                    raise config_exception("'HEIGHT' must be an integer!")
                if height <= 0:
                    raise config_exception("'HEIGHT' must be greater than 0!")
                data["HEIGHT"] = height

            elif key in {"ENTRY", "EXIT"}:
                if value == "":
                    raise config_exception(f"'{key}' coordinates "
                                           f"cannot be empty!")
                parts = value.split(",")
                if len(parts) != 2:
                    raise config_exception(f"'{key}' must contain exactly two "
                                           f"numbers!")
                try:
                    x = int(parts[0].strip())
                    y = int(parts[1].strip())
                    if "WIDTH" in data and "HEIGHT" in data:
                        if x >= data["WIDTH"] or y >= data["HEIGHT"]:
                            raise config_exception(f"in '{key}' coordinates "
                                                   f"{x, y} must be less than "
                                                   "'WIDTH' value")
                except ValueError:
                    raise config_exception(f"'{key}' coordinates must"
                                           f" be integers!")
                if x < 0 or y < 0:
                    raise config_exception(f"Negative number in '{key}'"
                                           f" coordinates!")
                data[key] = (x, y)
                if "ENTRY" in data and "EXIT" in data:
                    if data["ENTRY"] == data["EXIT"]:
                        raise config_exception("'ENTRY' and 'EXIT' must have"
                                               " different coordinate!")
            elif key == "OUTPUT_FILE":
                if len(value) < 1:
                    raise config_exception("'OUTPUT_FILE' value is empty!")
                data["OUTPUT_FILE"] = value
            elif key == "PERFECT":
                value = value.upper()
                if value not in {"TRUE", "FALSE"}:
                    raise config_exception("'PERFECT' must be TRUE or FALSE")
                data["PERFECT"] = value
        missing = required - found_keys
        if missing:
            raise config_exception(f"Missing key(s): {', '.join(missing)}")
    except config_exception as e:
        print(f"Error: {e}")
        exit(1)
    return data
