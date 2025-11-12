def find_all_starts(dna):
    starts = []
    for i in range(len(dna) - 2):
       if dna[i:i+3] == "ATG":
           starts.append(i)
    return starts

def find_first_in_register_stop(dna):
    pass # Replace the `pass` with your code


def all_orfs_range(dna):
    pass # Replace the `pass` with your code


def longest_orf(dna):
    pass # Replace the `pass` with your code




