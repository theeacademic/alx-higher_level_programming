#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Use the symmetric_difference method to find elements present in only one set
    diff_set = set_1.symmetric_difference(set_2)
    
    return diff_set

if __name__ == "__main__":
    # Test the function with the provided sets
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)

    # Convert the result set to a sorted list for consistent output
    result_list = sorted(list(od_set))

    # Print the result
    print(result_list)

