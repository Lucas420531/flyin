def parse_map(path):
    nb_drones = 0
    hubs = {}
    connections = []

    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            key, value = line.split(":", 1)
            value = value.strip()
            options = {}
            if "[" in value:
                value, bracket = value.split("[")
                value = value.strip()
                for item in bracket.replace("]", "").split():
                    name, val = item.split("=")
                    options[name] = val
            if key == "nb_drones":
                nb_drones = int(value)
            elif key in line.endswith("hub"):
                name, x, y = value.split()
                hubs[name] = {
                    "type": key,
                }