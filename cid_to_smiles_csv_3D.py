import csv
import requests
import os
import pubchempy as pcp

# Dr. Talia SERSEG

processed_cids = set()


with open('data.csv', 'r', encoding='utf-8-sig') as file:

    reader = csv.DictReader(file, delimiter=';')

    fieldnames = reader.fieldnames + ['isomeric_smiles'] 
    
    with open('data.csv', 'w', encoding='utf-8-sig', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter=';')
        
        writer.writeheader()

        for row in reader:
        
            try:
                cid = row['cid'].strip() 
            except KeyError:
                continue 

            if not cid or cid in processed_cids:
                continue 

            processed_cids.add(cid)

            try:
                compound = pcp.Compound.from_cid(cid)
                row['isomeric_smiles'] = compound.isomeric_smiles 

                sdf_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/sdf"

                response = requests.get(sdf_url)

                if response.status_code == 200:
                    if not os.path.exists('3D_structures'):
                        os.makedirs('3D_structures')
                    with open(f"3D_structures/{cid}.sdf", "wb") as sdf_file:
                        sdf_file.write(response.content)
                else:
                    print(f"Failed to retrieve SDF for CID {cid}: Status code {response.status_code}")
            except Exception as e:
                row['isomeric_smiles'] = "" 
                print(f"Error processing CID {cid}: {e}")

            writer.writerow(row)
