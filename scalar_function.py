def scalar_map(number_of_arguments: int, arguments: list, weights: list):
    assert len(arguments) == number_of_arguments and len(arguments) == len(weights) # call this dimension N
    sum_of_scalar_products = 0
    for i in range(0, len(arguments)):
        sum_of_scalar_products = sum_of_scalar_products + arguments[i] * weights[i] # bracket notation indexes into Iterable objects including lists, dictionaries and strings
    sum_of_scar_products += weights[len(weights) - 1] 
    return sum_of_scalar_products
        
