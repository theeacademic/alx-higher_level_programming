#!/usr/bin/python3

def number_keys(a_dictionary):
    # Use the len function to get the number of keys in the dictionary
    num_keys = len(a_dictionary)
    
    return num_keys

if __name__ == "__main__":

    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)


    print("Number of keys: {:d}".format(nb_keys))

