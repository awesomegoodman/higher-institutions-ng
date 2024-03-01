import institutionsData from './Nigerian Higher Institutions.json' assert { type: 'json' };

interface Institution {
  nameOfInstitution: string;
  type: InstitutionType;
  acronym: string;
  ownership: string;
  url: string;
  year: string;
  imagePath?: string;
  image?: string;
}

type InstitutionType = 'University' | 'College' | 'Polytechnic';

type StateType =
  | 'Abia'
  | 'Adamawa'
  | 'Akwa Ibom'
  | 'Anambra'
  | 'Bauchi'
  | 'Bayelsa'
  | 'Benue'
  | 'Borno'
  | 'Cross River'
  | 'Delta'
  | 'Ebonyi'
  | 'Edo'
  | 'Ekiti'
  | 'Enugu'
  | 'FCT - Abuja'
  | 'Gombe'
  | 'Imo'
  | 'Jigawa'
  | 'Kaduna'
  | 'Kano'
  | 'Katsina'
  | 'Kebbi'
  | 'Kogi'
  | 'Kwara'
  | 'Lagos'
  | 'Nasarawa'
  | 'Niger'
  | 'Ogun'
  | 'Ondo'
  | 'Osun'
  | 'Oyo'
  | 'Plateau'
  | 'Rivers'
  | 'Sokoto'
  | 'Taraba'
  | 'Yobe'
  | 'Zamfara';

// @ts-ignore
const institutions: Institution[] = institutionsData;

function excludeImage(institution: Institution): Institution {
  /**
   * Exclude the image data from the institution if requested.
   * @param institution The institution data.
   * @returns The institution data without the 'image' field if requested.
   */
  if ('image' in institution) {
    const { image, ...institutionCopy } = institution;
    return institutionCopy;
  }
  return institution;
}

export function getHigherInstitutionByAcronym(acronym: string, includeImage: boolean = true): Institution | null {
  /**
   * Retrieve data for one higher institution by its acronym.
   * @param acronym The acronym of the institution to retrieve.
   * @param includeImage Whether to include the image data. Default is true.
   * @returns Python object representing the institution data, or None if none is found.
   */
  const foundInstitution = institutions.find((institution) => institution.acronym === acronym);
  return foundInstitution ? (includeImage ? foundInstitution : excludeImage(foundInstitution)) : null;
}

export function getInstitutionsByName(name: string, includeImage: boolean = true): Institution[] {
  /**
   * Retrieve data for institutions whose name contains the specified string.
   * @param name The string to search for in the names of institutions.
   * @param includeImage Whether to include the image data. Default is true.
   * @returns List of objects representing the institution data that matches the search criteria.
   */
  const matchingInstitutions = institutions.filter((institution) => institution.nameOfInstitution.toLowerCase().includes(name.toLowerCase()));
  return includeImage ? matchingInstitutions : matchingInstitutions.map(excludeImage);
}

export function getAllHigherInstitutions(includeImage: boolean = true): Institution[] {
  /**
   * Retrieve data for all higher institutions.
   * @param includeImage Whether to include the image data. Default is true.
   * @returns Array of objects representing the institution data.
   */
  return includeImage ? institutions : institutions.map(excludeImage);
}

export function getInstitutionsByState(state: StateType, includeImage: boolean = true): Institution[] {
  /**
   * Retrieve data for institutions within a given state.
   * @param state The name of the state to search for.
   * @param includeImage Whether to include the image data. Default is true.
   * @returns Array of objects representing the institution data within the state.
   */
  const stateInstitutions = institutions.filter((institution) => institution.nameOfInstitution.toLowerCase().includes(state.toLowerCase()));
  return includeImage ? stateInstitutions : stateInstitutions.map(excludeImage);
}

export function getInstitutionsByType(institutionType: InstitutionType, includeImage: boolean = true): Institution[] {
  /**
   * Retrieve data for institutions of a specific type.
   * @param institutionType The type of institution to retrieve ("University", "College", "Polytechnic").
   * @param includeImage Whether to include the image data. Default is true.
   * @returns Array of objects representing the institution data of the specified type.
   */
  const typeInstitutions = institutions.filter((institution) => institution.type === institutionType);
  return includeImage ? typeInstitutions : typeInstitutions.map(excludeImage);
}
