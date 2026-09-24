import json
import os

DATA_DIR = "data"


def initialize_data():
    """Create data directory and JSON files if they do not exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

    files = {
        "students.json": [],
        "rooms.json": [],
        "fees.json": [],
        "complaints.json": []
    }

    for filename, default_data in files.items():
        filepath = os.path.join(DATA_DIR, filename)

        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                json.dump(default_data, file, indent=4)


def load_data(filename):
    """Load data from a JSON file."""
    filepath = os.path.join(DATA_DIR, filename)

    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)