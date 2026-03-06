from typing import Any


class config_exception(Exception):
    pass


def read_config(filename: str) -> dict:
    required = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
    data: dict[str, Any] = {}

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: configuration file not found")
        exit(1)
    try:
        found_keys = set()
        for raw_line in lines:
            line = raw_line.strip()
            if not line:
                continue
            elif line.startswith("#"):
                continue
            elif "=" not in line:
                raise config_exception("Invalid data in configuration file")
            key, value = line.split("=", 1)
            key = key.strip().upper()
            value = value.strip()

            if key not in required:
                raise config_exception(f"Unknown key '{key}'")

            if key in found_keys:
                raise config_exception(f"Duplicate key '{key}' in "
                                       f"configuration file")

            found_keys.add(key)
            if key == "WIDTH":
                if value == "":
                    raise config_exception("'WIDTH' has no value!")

                value = value.replace(" ", "")
                try:
                    width = int(value)
                except ValueError:
                    raise config_exception("'WIDTH' value must be an integer!")
                if width <= 3:
                    raise config_exception("'WIDTH' value must be greater"
                                           " than 2!")
                data["WIDTH"] = width

            elif key == "HEIGHT":
                if value == "":
                    raise config_exception("'HEIGHT' has no value!")
                value = value.replace(" ", "")
                try:
                    height = int(value)
                except ValueError:
                    raise config_exception("'HEIGHT' must be an integer!")
                if height <= 3:
                    raise config_exception("'HEIGHT' must be greater than 2!")
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
                    x = int(parts[1].strip())
                    y = int(parts[0].strip())
                    if "WIDTH" in data and "HEIGHT" in data:
                        if x >= data["WIDTH"] or y >= data["HEIGHT"]:
                            raise config_exception(f"in '{key}' coordinates "
                                                   f"{y, x} must be less than "
                                                   "'WIDTH' and 'HEIGHT' value")
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
                if value not in {"TRUE", "FALSE", "0", "1"}:
                    raise config_exception(
                        "'PERFECT' must be 'TRUE/FALSE' '1/0'"
                        )
                data["PERFECT"] = value
        missing = required - found_keys
        if missing:
            raise config_exception(f"Missing key(s): {', '.join(missing)}")
    except config_exception as e:
        raise e
    return data
