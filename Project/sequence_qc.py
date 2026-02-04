from Bio import SeqIO

record=SeqIO.read("input_sequence.fasta","fasta")
print(record.id)
print(record.seq)
print(record.description)
print(len(record.seq))

with open ("qc_summary.txt","w") as x:
    x.write(record.id+"\n")
    x.write(record.description+"\n")
    x.write(str(record.seq+"\n"))
    x.write(str(len(record.seq))+"\n")
   

print("qc analysis performed successfully")