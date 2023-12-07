#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is not None and not empty
    if a_dictionary:
        # Find the key with the maximum value
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None

if __name__ == "__main__":
    # Test the function with the provided dictionary
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    # Test the function with None
    best_key = best_score(None)
    print("Best score: {}".format(best_key))

