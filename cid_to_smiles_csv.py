import csv
import pubchempy as pcp

processed_cids = set()

# Dr. Talia SERSEG

with open('data.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=';')
    
    with open("results.txt", "w") as output_file:
        for row in reader:

            try:
                cid = row['cid'].strip()  
            except KeyError:
                continue 

            if not cid or cid in processed_cids:
                continue 

            processed_cids.add(cid)

            try:
                c = pcp.Compound.from_cid(cid)
                output_file.write(c.isomeric_smiles + "\n")
            except Exception as e:

                continue
