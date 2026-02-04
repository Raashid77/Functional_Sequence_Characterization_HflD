from Bio.Blast import NCBIWWW

from Bio import SeqIO
record=SeqIO.read("input_sequence.fasta","fasta")

result_handle=NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq)

with open ("blast_results.txt","w") as x:
    x.write(result_handle.read())

print("Blast performed successfully")


