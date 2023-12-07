#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Use the intersection method to find common elements
    common_set = set_1.intersection(set_2)
    
    return common_set

if __name__ == "__main__":
    # Test the function with the provided sets
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)

    result_list = sorted(list(c_set))
    print(result_list)

