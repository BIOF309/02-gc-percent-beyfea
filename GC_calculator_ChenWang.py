
#Paste Code here
flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'
c = flu_ns1_seq.count('C')
g = flu_ns1_seq.count('G')
cg = c + g
Percentage = cg / len(flu_ns1_seq)
print(Percentage)