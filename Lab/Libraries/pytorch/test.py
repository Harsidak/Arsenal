class HackerObject:
    def __eq__(self, other):
        # We rigged the math button! It always says True!
        return True 

corrupted_data = HackerObject()

# The == check gets fooled!
if corrupted_data == None:
    print("Data is empty!") # It prints this, even though it's NOT empty!

# The 'is' check CANNOT be fooled. It bypasses __eq__ entirely.
if corrupted_data is None:
    print("Data is empty!") # This safely returns False.