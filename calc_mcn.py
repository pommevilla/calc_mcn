from sys import argv
from itertools import combinations

def process_gauss_code(raw_gauss_code):
    '''
    Formats input Gauss code for use in other functions.

    input
    '''
    
    return [int(s.replace(',', '')) for s in argv[1:]]
    
def create_knot_dictionary(gauss_code):   
    '''
    Creates a knot dictionary from a Gauss code.
    inputs:
    gauss_code - a list of ints representing the Gauss code of the knot.  See attached email for explanation for the algorithm and sample run.
            This code will only run on standard Gauss code; it won't work for other versions of Gauss code.
            
    knot dictionary is of the form
            d_k = {
                s_i: [(gauss_subseq), [c_1, c_2, . . ., c_n]]
                .
                .
                .
            },
    where s_i is the name of the strand, gauss_subseq is a tuple representing the subsequence of the Gauss code corresponding to the the strand, 
    and the c_i represent the crossings that s_n are over.  The c_i are tuples (s_i_1, s_i_2), where s_i_1 and s_i_2 are the names of the strands 
    that s_i is over 
            
    returns the knot dictionary represented by the Gauss code.
    '''
    strand_set = set()

    i = 0
    while True:
        if gauss_code[i] < 0:
            beginning = i
            i = (i + 1) % len(gauss_code)
            while gauss_code[i] > 0:
                i = (i + 1) % len(gauss_code)
            if beginning > i:
                new_strand = gauss_code[beginning:]
                for k in range(i + 1):
                    new_strand.append(gauss_code[k])
                new_strand = tuple(new_strand)
            else:
                new_strand = tuple(gauss_code[beginning:i+1])
            if new_strand not in strand_set:
                strand_set.add(new_strand)
            else:
                break
        else:
            i = (i + 1) % len(gauss_code)
                
    letter_list = list(map(chr, range(65, 91)))
    knot_dictionary = dict()
    for i, strand in enumerate(strand_set):    
        knot_dictionary[letter_list[i]] = [strand, []]
    
    for key_outer in knot_dictionary:
        for under in knot_dictionary[key_outer][0]:
            if under > 0:
                found1, found2 = False, False
                for key_inner in knot_dictionary:
                    if found1 and found2:
                        break
                    else:
                        if knot_dictionary[key_inner][0][0] == -under:
                            under1 = key_inner
                            found1 = True
                        if knot_dictionary[key_inner][0][-1] == -under:
                            under2 = key_inner
                            found2 = True
                knot_dictionary[key_outer][1].append((under1, under2))

    return knot_dictionary

def is_valid_coloring(seed_strands, knot_dict):
    '''
    seed_strands - a set of characters representing strands in the knot diagram of a knot
    knot_dict - a dictionary representing the knot
    
    See ReadMe.md for explanation of algorithm.
    
    returns True if the seed_strands lead to a valid coloring of the knot, False otherwise
    '''
    colored_set = seed_strands.copy()
    new_coloring = True
    while new_coloring:
        new_coloring = False
        for strand in colored_set.copy():
            for crossing in knot_dict[strand][1]:
                if crossing[0] not in colored_set or crossing[1] not in colored_set:
                    if crossing[0] in colored_set or crossing[1] in colored_set:
                        colored_set.update(crossing)
                        new_coloring = True
                        
    if colored_set == set(knot_dict.keys()):
        return True
    
    return False
    
def calc_mcn(knot_dict):
    '''
    knot_dict - a dictionary representing the knot
    
    returns a tuple of (strands, n)
        strands - a set of letters corresponding to the seed strands
        n - an integer representing the meridional colorability rank of the knot
    
    '''

    
    strands = knot_dict.keys()
    # strands = set(knot_dict.keys())
    
    n = 2
    while n < len(knot_dict) - 1:
        for seed_strands in combinations(strands, n):
            seed_strands = set(seed_strands)
            if is_valid_coloring(seed_strands, knot_dict):
                return (n, seed_strands)
        n += 1

    
    # If control passes the above while loop, then it was not able to find a coloring beginning
    # with less than n - 1 strands.  In that case, return n - 1 colorability.
    strands.pop()
    return (n, seed_strands)

def print_knot_dictionary(kd):
    '''
    Prints out a knot dictionary in a nice format.

    Input: a knot dictionary kd 
    '''
    print("Knot dictionary:")
    print("{:^15}{:30}{}".format("STRAND", "SUBSEQUENCE", "CROSSINGS OVER"))
    for strand in knot_dict:
        subsequence = knot_dict[strand][0]
        undercrossings = ' '.join([str(x) for x in knot_dict[strand][1]])
        print("{:^15}{:30}{}".format(strand, str(subsequence), undercrossings))
    

if __name__ == '__main__':
    
    gauss_code = process_gauss_code(argv)    
    

    knot_dict = create_knot_dictionary(gauss_code)
    print_knot_dictionary(knot_dict)

    mcn_info = calc_mcn(knot_dict)
    print("\nMeridional coloring number: {}\nSeed strand set: {}".format(*mcn_info))
    