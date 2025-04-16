import json
import os

def load_data(file_path=None):
    """
    Args:
        file_path (str): The path to the JSON file. Defaults to '../data/sample_itinerary.json'.

    Returns:
        list of dict: A list of dictionaries representing the data in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file is not valid JSON.
    """
    if file_path is None:
        # Construct the default file path relative to this script's location
        file_path = os.path.join(os.path.dirname(__file__), '../data/sample_itinerary.json')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in file {file_path}: {e}")
To test your new change we need to change main.py as well.
from itinerary_builder import build_itinerary
from data_loader import load_data
from utils import print_itinerary

def main():
    """
    Main function to generate and print a travel itinerary.

    This function performs the following steps:
    1. Loads sample data.
    2. Builds an itinerary based on the loaded data.
    3. Prints the generated itinerary.

    Returns:
        None
    """
    data = load_data() # Uses default sample file path
    print(data)
    itinerary = build_itinerary(data)
    print("Generated Itinerary:")
    print_itinerary(itinerary)

if __name__ == "__main__":
    main()
