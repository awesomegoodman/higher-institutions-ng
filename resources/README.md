# Institutions API Data Conversion

This Python script converts data from a CSV file containing information about Nigerian higher institutions into a JSON format. The CSV file includes details such as the name of the institution, type, acronym, ownership, URL, year of establishment, and image paths.

## Usage

1. Ensure you have the necessary dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

2. Set the base directory (`BASE_DIR`) in the script to the path where your CSV file and image directories are located.

3. Run the script:

   ```bash
   python higher_institutions.py
   ```

4. The converted JSON file will be saved in the base directory with the name specified in the `JSON_OUTPUT_PATH` variable.

## Additional Features

- **Image Handling:**

  - The script constructs image paths based on the institution's type, ownership, and acronym.
  - Images are encoded into base64 strings and included in the JSON output.

- **Error Handling:**
  - If an image file is not found, an error message is printed.
