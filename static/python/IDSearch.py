import sys
file = open("../../assets/individuals.csv", "r")
file.readline()

ID = input("What Person ID are you looking for?")



for line in file:
    split = line.split(",")
    if ID == split[1]:
        print("Here is the data on Person ID %s \n %s" % (ID, line))
        sys.exit()
print("Sorry, we were unable to find anyone with that ID.")
file.close()