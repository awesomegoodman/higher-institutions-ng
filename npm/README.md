# Nigerian Higher Institutions (higher-institutions-ng)

Higher Institutions NG is a JavaScript library providing information about Nigerian higher institutions, including universities, colleges, and polytechnics.

## Installation

You can install the package via npm:

```bash
npm install higher-institutions-ng
```

## Usage

### Importing

```javascript
import {
  getAllHigherInstitutions,
  getHigherInstitutionByAcronym,
  getInstitutionsByName,
  getInstitutionsByState,
  getInstitutionsByType,
} from 'higher-institutions-ng';

// Retrieve data for all institutions with image excluded
const allInstitutionsData = getAllHigherInstitutions(false);
console.log(allInstitutionsData);

// Retrieve data for one institution with image excluded
const institutionDataNoImage = getHigherInstitutionByAcronym('UNILAG', false);
console.log(institutionDataNoImage);

// Retrieve institutions by name with image excluded
const covenantInstitutions = getInstitutionsByName('Covenant', false);
console.log("Institutions matching 'Covenant':", covenantInstitutions);

// Retrieve institutions of a specific type with image excluded
const universities = getInstitutionsByType('University', false);
console.log('Universities:', universities);

// Retrieve institutions within a state with image excluded
const lagosInstitutions = getInstitutionsByState('Lagos', false);
console.log('Institutions in Lagos:', lagosInstitutions);
```

### Functions

- `getAllHigherInstitutions(includeImage: boolean = true) -> Institution[]`: Returns an array of objects representing all higher institutions in Nigeria.

- `getHigherInstitutionByAcronym(acronym: string, includeImage: boolean = true) -> Institution | null`: Returns information about a specific higher institution identified by its acronym.

- `getInstitutionsByName(name: string, includeImage: boolean = true) -> Institution[]`: Returns institutions whose name contains the specified string.

- `getInstitutionsByState(state: string, includeImage: boolean = true) -> Institution[]`: Returns institutions within a given state.

- `getInstitutionsByType(institutionType: string, includeImage: boolean = true) -> Institution[]`: Returns institutions of a specific type.

### Type Definitions

- `Institution`: Represents the data structure for a higher institution with fields such as name, type, acronym, etc.

- `InstitutionType`: Literal type representing the types of higher institutions ('University', 'College', 'Polytechnic').

- `StateType`: Literal type representing the names of Nigerian states.

### Image Data

All images included in the returned data are represented as base64 strings.

### Backward Compatibility

This library ensures backward compatibility with older JavaScript versions, ensuring compatibility with a wide range of environments and browsers.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## GitHub Repository

You can find the source code and contribute to this project on GitHub: [Higher Institutions NG on GitHub](https://github.com/awesomegoodman/higher-institutions-ng/tree/main/npm)
