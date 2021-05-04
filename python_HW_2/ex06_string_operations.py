"""This module describes the solutions from the learnpython.org.

Exercise: Try to fix the code to print out the correct information
by changing the string.
"""


TEMP_STR = "Strings are awesome!"

if __name__ == "__main__":
    # Length should be a 20
    print("Length of s = %d" % len(TEMP_STR))

    # First occurrence of "a" should be at index 8
    print("The first occurrence of the letter a = %d" % TEMP_STR.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % TEMP_STR.count("a"))

    # Slicing the string into bits
    print("The first five characters are '%s'" % TEMP_STR[:5])
    # 5 to 10
    print("The next five characters are '%s'" % TEMP_STR[5:10])
    # Just number 12
    print("The thirteenth character is '%s'" % TEMP_STR[12])
    # (0-based indexing)
    print("The characters with odd index are '%s'" % TEMP_STR[1::2])
    # 5-th-from-last to end
    print("The last five characters are '%s'" % TEMP_STR[-5:])

    # Convert everything to uppercase
    print("String in uppercase: %s" % TEMP_STR.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % TEMP_STR.lower())

    # Check how a string starts
    if TEMP_STR.startswith("Str"):
        print("String starts with 'Str'. Good!")

    # Check how a string ends
    if TEMP_STR.endswith("ome!"):
        print("String ends with 'ome!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    print("Split the words of the string: %s" % TEMP_STR.split(" "))
