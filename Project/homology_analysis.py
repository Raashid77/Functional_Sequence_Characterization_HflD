# from Bio.Blast import NCBIWWW

# from Bio import SeqIO
# record=SeqIO.read("input_sequence.fasta","fasta")

# result_handle=NCBIWWW.qblast(
#     program="blastp",
#     database="nr",
#     sequence=record.seq)

# with open ("blast_results.xml","w") as y:
#     y.write(result_handle.read())
 
# print("Blast performed successfully")

from Bio.Blast import NCBIXML

with open ("blast_results.xml") as b:
    blast_record=NCBIXML.read(b)

print(len(blast_record.alignments))

first_alignment=blast_record.alignments[0]
# print(first_alignment.title)
# print(first_alignment.length)

# for a in blast_record.alignments:
#     print(a.title)

print(len(first_alignment.hsps))

first_hsp=first_alignment.hsps[0]
print(first_hsp.score)
print(first_hsp.expect)

print("query")
print(first_hsp.query)

print("matched")
print(first_hsp.sbjct)

print("alignment")
print(first_hsp.match)