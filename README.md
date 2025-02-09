# PubChem-SMILES_3D_Structure_Retriever
This script retrieves the isomeric SMILES string and 2D/3D structures (in SDF format) of chemical compounds from PubChem based on a list of Compound IDs (CIDs) in a CSV file. 

For each CID, the script retrieves the corresponding compound information from PubChem, fetches its 2D/3D structure, and saves the SDF file. Additionally, the script extracts the isomeric SMILES string for each compound and appends it to the CSV.

# Dependencies

The script requires the following dependencies:

    requests
    pubchempy
    csv
    os

These dependencies can be installed via pip:

pip install requests pubchempy

# Usage

To use the script, place your input CSV file (e.g., data.csv) containing a column for cid (Compound ID) in the same directory as the script. The script will process each CID, download the 3D structure (SDF), and add the isomeric SMILES to the CSV file. The SDF files will be saved in a folder named 3D_structures.

Run the script as follows:

python cidtosmilescsv3D.py

# Input CSV Format

The input CSV should have a column named cid containing the PubChem Compound IDs. The CSV can also contain other columns, and the script will add an additional column isomeric_smiles to store the corresponding SMILES strings.

Example of the CSV format:

cid,name
12345,Compound A
67890,Compound B

# Functionality

The script performs the following tasks:

    Loads data from the CSV file into a list of dictionaries.
    For each CID in the CSV, the script:
        Retrieves the compound data from PubChem.
        Downloads the 2D/3D structure (SDF file) of the compound.
        Extracts the isomeric SMILES of the compound.
    Appends the isomeric SMILES to the CSV file and saves the SDF file in the 3D_structures directory.

# Error Handling

The script includes error handling to manage the following cases:

    If a compound's CID is missing or invalid, it is skipped.
    If fetching the 3D structure from PubChem fails (due to an incorrect CID or network issues), an error message is printed, and the script continues processing other compounds.
    If there is an issue with saving the SDF file, an error message is printed, and the script proceeds with the next compound.
    If a CID is repeated, it will be ignored.

# Directory Structure

After running the script, the directory will contain:

    data.csv: The updated CSV file with the added isomeric_smiles column.
    3D_structures/: A folder where the SDF files of compounds are saved.

# License

This script is licensed under the MIT License. See LICENSE for more information.
