max_starting_number = 1000000
starting_number = 13
longest_chain = 0
starting_number_with_longest_chain = 13


def calculate_next_in_chain(num, chain_length):
    if num == 1:
        return chain_length
    chain_length += 1
    if num % 2 == 0:
        return calculate_next_in_chain(num/2, chain_length)
    else:
        return calculate_next_in_chain(3 * num + 1, chain_length)

while starting_number < max_starting_number:
    chain_length = 1
    returned_chain_length = calculate_next_in_chain(starting_number, chain_length)
    if returned_chain_length > longest_chain:
        longest_chain = returned_chain_length
        starting_number_with_longest_chain = starting_number
        print(starting_number_with_longest_chain, longest_chain)
    starting_number += 1

print(starting_number_with_longest_chain)
