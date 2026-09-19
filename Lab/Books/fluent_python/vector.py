good_data = (1, 2, 3) # Tuple (Immutable)
print(hash(good_data)) # Works perfectly

bad_data = [1, 2, 3]  # List (Mutable)
#print(hash(bad_data)) # CRASH: TypeError: unhashable type: 'list'