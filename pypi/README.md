# Higher Institutions NG

Higher Institutions NG is a Python library providing information about Nigerian higher institutions, including universities, colleges, and polytechnics.

## Installation

You can install the package via pip:

```bash
pip install higher-institutions-ng
```

## Usage

### Importing

```python
from higher_institutions_ng import (
    get_all_higher_institutions,
    get_higher_institution_by_acronym,
    get_institution_by_name,
    get_institutions_by_state,
    get_institutions_by_type
)

# Retrieve data for all institutions with image excluded
all_institutions_data = get_all_higher_institutions(include_image=False)
print(all_institutions_data)

# Retrieve data for one institution with image excluded
institution_data_no_image = get_higher_institution_by_acronym("UNILAG", include_image=False)
print(institution_data_no_image)

# Retrieve institutions by name with image excluded
covenant_institutions = get_institution_by_name("Covenant", include_image=False)
print("Institutions matching 'Covenant':", covenant_institutions)

# Retrieve institutions of a specific type with image excluded
universities = get_institutions_by_type("University", include_image=False)
print("Universities:", universities)

# Retrieve institutions within a state with image excluded
lagos_institutions = get_institutions_by_state("Lagos", include_image=False)
print("Institutions in Lagos:", lagos_institutions)
```

### Functions

- `get_all_higher_institutions() -> List[Institution]`: Returns an array of dictionaries representing all higher institutions in Nigeria.

- `get_higher_institution_by_acronym(acronym: str, include_image: bool = True) -> Optional[Institution]`: Returns information about a specific higher institution identified by its acronym.

- `get_institution_by_name(name: str, include_image: bool = True) -> List[Institution]`: Returns institutions whose name contains the specified string.

- `get_institutions_by_state(state: StateType, include_image: bool = True) -> List[Institution]`: Returns institutions within a given state.

- `get_institutions_by_type(institution_type: InstitutionType , include_image: bool = True) -> List[Institution]`: Returns institutions of a specific type.

### Type Definitions

- `Institution`: Represents the data structure for a higher institution with fields such as name, type, acronym, etc.

- `InstitutionType`: Literal type representing the types of higher institutions ('University', 'College', 'Polytechnic').

- `StateType`: Literal type representing the names of Nigerian states.

### Image Data

All images included in the returned data are encoded in base64 string format and represent the logos of the respective institutions.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## GitHub Repository

You can find the source code and contribute to this project on GitHub: [Higher Institutions NG on GitHub](https://github.com/awesomegoodman/higher-institutions-ng/tree/main/pypi)
