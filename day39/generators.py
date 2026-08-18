#A generator is a function that produces values one by one instead of producing all values at once.
#It uses the keyword yield.
##def:A generator is a Python function that uses yield to produce values one at a time, pausing its execution between values and saving memory.

#Normal function:
# Function → produces result → ends

# Generator:
# Function → produces value → pauses
#               ↓
#           next value → continues
#               ↓
#           next value → continues


#yield means
# yield = give a value + pause the function
# When the next value is requested, the function continues from where it stopped.

# next() means
# next() = ask the generator for its next value


#Why generators?
# The biggest advantage is memory efficiency.
# If you need 1 crore values:
# Normal approach → may store all values in memory.
# Generator → produces one value at a time.