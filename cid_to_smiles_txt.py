import pubchempy as pcp

# Dr. Talia SERSEG

file = open("cid.txt", "r")

output_file = open("results.txt", "w")

for line in file:
    line = line.strip()

    if not line:
        continue 

    try:
        c = pcp.Compound.from_cid(line)
        output_file.write(c.isomeric_smiles + "\n")
    except Exception as e:
        print(f"Error processing CID {line}: {e}") 

file.close()
output_file.close()