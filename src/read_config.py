def read_config():
    array = {}
    with open("config.txt","r") as file:
        for line in file:
            key, value = line.strip().split("=")
            array[key] = value

    width = int(array["WIDTH"])
    height = int(array["HEIGHT"])
    entry = tuple(int(i.strip()) for i in array["ENTRY"].split(","))
    exit_end = tuple(int(i.strip()) for i in array["EXIT"].split(","))
    out_file = array["OUTPUT_FILE"]
    prefect = bool(array["PERFECT"])

    return width, height, entry, exit_end, out_file, prefect

    