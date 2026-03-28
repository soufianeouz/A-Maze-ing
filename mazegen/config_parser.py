import sys


def parse_coordinate(value):
    """Manually extracts x,y integers from a string."""
    comma_pos = value.find(",")
    if comma_pos == -1:
        raise ValueError(f"Invalid coordinate format: {value}")
    
    try:
        x = int(value[:comma_pos].strip())
        y = int(value[comma_pos + 1:].strip())
        return (x, y)
    except ValueError:
        raise ValueError(f"Coordinates must be integers: {value}")


def validate_parameters(config):
    """Checks for missing keys and impossible maze logic."""
    mandatory = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]
    
    for key in mandatory:
        if key not in config:
            raise ValueError(f"Missing mandatory key: {key}")
    
    w, h = config["WIDTH"], config["HEIGHT"]
    for label in ["ENTRY", "EXIT"]:
        x, y = config[label]
        if not (0 <= x < w and 0 <= y < h):
            raise ValueError(f"{label} {x,y} is outside {w}x{h} bounds")
    
    if config["ENTRY"] == config["EXIT"]:
        raise ValueError("ENTRY and EXIT cannot be the same cell")


def parse_config_file(filepath):
    """The core loop to read and clean the file data."""
    config = {}
    
    with open(filepath, 'r') as f:
        for line in f:
            comment_idx = line.find("#")
            if comment_idx != -1:
                line = line[:comment_idx]
            line = line.strip()
            
            if not line:
                continue

            equal_idx = line.find("=")
            if equal_idx == -1:
                raise ValueError(f"Syntax error (missing '='): {line}")
            
            key = line[:equal_idx].strip()
            val = line[equal_idx + 1:].strip()

            if key in ("WIDTH", "HEIGHT"):
                config[key] = int(val)
            elif key in ("ENTRY", "EXIT"):
                config[key] = parse_coordinate(val)
            elif key == "PERFECT":
                if val.lower() == "true":
                    config[key] = True
                elif val.lower() == "false":
                    config[key] = False
                else:
                    raise ValueError(f"PERFECT must be True or False: {val}")
            elif key == "OUTPUT_FILE":
                config[key] = val

    validate_parameters(config)
    return config


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    try:
        maze_settings = parse_config_file(sys.argv[1])
        print("Settings loaded successfully:")
        print(maze_settings)
                
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()