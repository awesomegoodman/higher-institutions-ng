import os
import json
from typing import List, Dict, Any, Optional, TypedDict, Literal


InstitutionType = Literal['University', 'College', 'Polytechnic']
class Institution(TypedDict, total=False):
    nameOfInstitution: str
    type: InstitutionType
    acronym: str
    ownership: str
    url: str
    year: str
    imagePath: str
    image: Optional[str]

StateType = Literal[
    "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", 
    "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT - Abuja", "Gombe", 
    "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", 
    "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", 
    "Taraba", "Yobe", "Zamfara"
]

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the JSON file relative to the current script
JSON_PATH = os.path.join(current_dir, 'Nigerian Higher Institutions.json')

def read_json_file(json_file_path: str) -> list:
    """
    Read JSON data from a file and return it as a list of dictionaries.

    Args:
        json_file_path (str): Path to the JSON file.

    Returns:
        list: List of dictionaries representing the JSON data.
    """
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

institutions = read_json_file(JSON_PATH)

def _exclude_image(institution: Institution) -> Institution:
    """
    Exclude the image data from the institution if requested.

    Args:
        institution (Dict[str, Any]): The institution data.

    Returns:
        Dict[str, Any]: The institution data without the 'image' field if requested.
    """
    if 'image' in institution:
        institution_copy = institution.copy()
        del institution_copy['image']
        return institution_copy
    return institution

# Function to retrieve 1 higher institution data
def get_higher_institution_by_acronym(acronym: str, include_image: bool = True) -> Optional[Institution]:
    """
    Retrieve data for one higher institution by its acronym.

    Args:
        acronym (str): The acronym of the institution to retrieve.
        include_image (bool): Whether to include the image data. Default is True.

    Returns:
        Institution: Python object representing the institution data, or None if none is found.
    """
    for institution in institutions:
        if institution['acronym'] == acronym:
            return institution if include_image else _exclude_image(institution)
    return None

def get_institution_by_name(name: str, include_image: bool = True) -> List[Institution]:
    """
    Retrieve data for institutions whose name contains the specified string.

    Args:
        name (str): The string to search for in the names of institutions.
        include_image (bool): Whether to include the image data. Default is True.

    Returns:
        List[Institution]: List of objects representing the institution data that matches the search criteria.
    """
    matching_institutions = []
    for institution in institutions:
        if name.lower() in institution['nameOfInstitution'].lower():
            if include_image:
                matching_institutions.append(institution)
            else:
                matching_institutions.append(_exclude_image(institution))
    return matching_institutions

# Function to retrieve all schools data
def get_all_higher_institutions(include_image: bool = True) -> List[Institution]:
    """
    Retrieve data for all higher institutions.

    Args:
        include_image (bool): Whether to include the image data. Default is True.

    Returns:
        List[HigherInstitutionType]: Array of objects representing the institution data.
    """
    return [institution if include_image else _exclude_image(institution) for institution in institutions]


# Function to retrieve institutions within a state
def get_institutions_by_state(state: StateType, include_image: bool = True) -> List[Institution]:
    """
    Retrieve data for institutions within a given state.

    Args:
        state (str): The name of the state to search for.
        include_image (bool): Whether to include the image data. Default is True.

    Returns:
        List[Institution]: Array of objects representing the institution data within the state.
    """
    state_institutions: List[Institution] = []
    for institution in institutions:
        if state.lower() in institution['nameOfInstitution'].lower():
            if not include_image:
                state_institutions.append(_exclude_image(institution))
            else:
                state_institutions.append(institution)
    return state_institutions

# Function to retrieve institutions by type
def get_institutions_by_type(institution_type: Institution, include_image: bool = True) -> List[Institution]:
    """
    Retrieve data for institutions of a specific type.

    Args:
        institution_type (InstitutionType): The type of institution to retrieve ("University", "College", "Polytechnic").
        include_image (bool): Whether to include the image data. Default is True.

    Returns:
        List[Institution]: Array of objects representing the institution data of the specified type.
    """
    valid_types: set[InstitutionType] = {'University', 'College', 'Polytechnic'}
    if institution_type not in valid_types:
        raise ValueError("Invalid institution type. Valid types are 'University', 'College', and 'Polytechnic'.")

    type_institutions: List[Institution] = []
    for institution in institutions:
        if institution['type'] == institution_type:
            if not include_image:
                type_institutions.append(_exclude_image(institution))
            else:
                type_institutions.append(institution)
    return type_institutions
