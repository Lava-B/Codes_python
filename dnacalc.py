#Calculate GC content of a DNA sequence

sequence = input("Enter your DNA sequence: ")

#Calculate counts
g_count = sequence.upper().count('G')
c_count = sequence.upper().count('C')

# Formula: (G + C)/Total Length*100
gc_content = (g_count + c_count) / len(sequence) * 100

print(f"DNA Sequence: {sequence}")
print(f"GC Content: {gc_content:.2f}%")

#Get the reverse complement
def reverse(sequence):
    
    complement_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    # list comprehension
    comp_sequence = [complement_map[base] for base in sequence.upper()]
    reverse_comp = "".join(comp_sequence[::-1])
    
    return reverse_comp

print(f"Original: {sequence}")
print(f"Reverse Complement: {reverse(sequence)}")