# symbols = '#$%^&*()&|'
# symbol_unicode = [ord(symbol) for symbol in symbols]
# print(symbol_unicode)

# list_no_end = [1,2,] # list , tuples, dicts doesnt errors us if we add the comma at the end of them
# print(list_no_end)

""" list-comps vs. map filters"""
        # doing with list-comps
# symbols = '!@#$%^&*()_+"|<'
# unicode_symbols = [ord(symbol) for symbol in symbols if ord(symbol) > 90]
# print(unicode_symbols)
        # doing with filter function
# unicode_symbol = list(filter(lambda c : c > 90 , map(ord, symbols)))
# print(unicode_symbol)


""" cartesian product using list-comps"""
# t_shirts_colors = ['red','blue','black']
# t_shirts_sizes = ['s','m','l']
# available_pairs = [(color,size) for color in t_shirts_colors for size in t_shirts_sizes]
# print(f"Available pairs are  : {available_pairs}")



