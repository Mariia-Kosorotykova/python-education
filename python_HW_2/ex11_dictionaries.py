"""This module describes the solutions from the learnpython.org.

Exercise: Add "Jake" to the phonebook with the phone number
938273443, and remove Jill from the phonebook.
"""


phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

if __name__ == "__main__":
    # added Jake
    phonebook["Jake"] = 938273443
    # removed Jill
    del phonebook["Jill"]

    # testing code
    if "Jake" in phonebook:
        print("Jake is listed in the phonebook.")

    if "Jill" not in phonebook:
        print("Jill is not in listed in the phonebook.")
