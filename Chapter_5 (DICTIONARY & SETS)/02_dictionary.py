d = {} # Empty dictionary

marks = {
    "puja" : 85,
    "sumit" : 75,
    "Rahul" : 50,
}


# These are dictionary Methods 

# a.item()
print(marks.items())

# a.keys()
print(marks.keys())

# a.value()
print(marks.values())

# a.update({"friends" :}):
marks.update({"puja":90, "trisha":80})
print(marks)

# a.get("name"):
print(marks.get("puja2")) # prints (none)
print(marks["puja2"]) # Returns an (keyError)