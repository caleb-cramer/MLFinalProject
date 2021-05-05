import pickle # standard python library

# "pickle" an object (AKA object serialization)
# save a Python object to a binary file

# "unpickle" an object (AKA object de-serialization)
# load a Python object from a binary file (back into memory)

# for your project, pickle an instance MyRandomForestClassifier, MyDecisionTreeClassifier
# for demo use header and interview_tree below
header = ["att0", "att1", "att2"]
tree = \

packaged_object = [header, tree]
# pickle packaged_object
outfile = open("tree.p", "wb")
pickle.dump(packaged_object, outfile)
outfile.close()
