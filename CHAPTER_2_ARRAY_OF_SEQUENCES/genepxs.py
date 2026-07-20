colors = ['red','blue']
sizes = ['s','m','l']

shirts_pairs = ((color,size) for color in colors 
                            for size in sizes)
print(shirts_pairs)
for pair in shirts_pairs:
    print(pair)

for pair in shirts_pairs:
    print(pair)

