import csv
import json
import os
import base64
from typing import List, Dict, Any

# Get the current working directory
current_dir = os.getcwd()

# Set the base directory
BASE_DIR = os.path.join(current_dir)
NARR_DIR = os.path.join(BASE_DIR, 'resources', 'NARR')
JSON_OUTPUT_PATH = 'Nigerian Higher Institutions.json'

# Constants for keys
NAME_KEY = "Name of Institution"
TYPE_KEY = "Type"
ACRONYM_KEY = "Acronym"
OWNERSHIP_KEY = "Ownership"
URL_KEY = "Url"
YEAR_KEY = "Year"
IMAGE_PATH_KEY = "Image Path"
IMAGE_KEY = "Image"
CITY_KEY = "City"
STATE_KEY = "State"


def create_directories_if_not_exist(directory: str) -> None:
    """Create directories if they do not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_image_path(row: Dict[str, Any]) -> str:
    """
    Construct the image path based on the institution's type, ownership, and acronym.
    Assumes that images are in the 'NARR' directory.

    Args:
        row (Dict[str, Any]): Row data from the CSV file.

    Returns:
        str: Image path.
    """
    type_plural = row[TYPE_KEY] + \
        's' if row[TYPE_KEY] != "University" else "Universities"
    ownership_folder = row[OWNERSHIP_KEY].replace(' ', '_') + " " + type_plural
    image_name = row[ACRONYM_KEY] + '.jpg'
    image_path = os.path.join(NARR_DIR, type_plural, ownership_folder, image_name)
    return image_path


def get_image_data(row: Dict[str, Any]) -> str:
    """
    Convert the image file into a base64-encoded string.

    Args:
        row (Dict[str, Any]): Row data from the CSV file.

    Returns:
        str: Base64-encoded image data.
    """
    image_path = get_image_path(row)
    try:
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"{image_path} not found")
        return
    return image_data


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Read data from a CSV file and return a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict[str, Any]]: List of dictionaries representing the CSV data.
    """
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Create a dictionary for each institution
            institution_data = {
                'nameOfInstitution': row[NAME_KEY],
                'type': row[TYPE_KEY],
                'acronym': row[ACRONYM_KEY],
                'ownership': row[OWNERSHIP_KEY],
                'url': row[URL_KEY],
                'year': row[YEAR_KEY],
                # 'city': row[CITY_KEY,
                # 'state': row[STATE_KEY],
                # 'imagePath': get_image_path(row),
                # 'image': get_image_data(row),
            }
            data.append(institution_data)
    return data


def write_json(data: List[Dict[str, Any]], output_file: str) -> None:
    """
    Write data to a JSON file.

    Args:
        data (List[Dict[str, Any]]): Data to be written to the JSON file.
        output_file (str): Path to the output JSON file.
    """
    with open(output_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Construct the full path to the CSV file using the base directory
    csv_file_path = os.path.join(NARR_DIR, 'NARR institution.csv')

    # Use the predefined JSON output path
    json_output_path = os.path.join(BASE_DIR, 'resources', JSON_OUTPUT_PATH)
    npm_output_path = os.path.join(BASE_DIR, 'npm', 'src', 'higher-institutions-ng', 'Nigerian Higher Institutions.json')
    pypi_output_path = os.path.join(BASE_DIR, 'pypi', 'src', 'higher-institutions-ng', 'Nigerian Higher Institutions.json')
    
    # Read CSV data
    csv_data = read_csv(csv_file_path)

    # Write CSV data to a JSON file
    write_json(csv_data, json_output_path)
    write_json(csv_data, npm_output_path)
    write_json(csv_data, pypi_output_path)

    print(f"Conversion completed. JSON file saved at: {json_output_path}")
