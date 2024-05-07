import sys
import csv
import math

def main():

    #file = open("../../assets/Data2.csv", "r")
    #file = open("C:/Users/Xanatos/Desktop/FP/Darth-J-Squared.github.io/assets/Data2.csv", "r")
    #with open("C:/Users/Xanatos/Desktop/FP/Darth-J-Squared.github.io/assets/Data2.csv", "r") as file:
    with open("./assets/Data2.csv", "r") as file:
        read = csv.reader(file, delimiter=",")

        ID = input("What Person ID are you looking for?")

        for line in read:
            #split = line.split(",")
            if ID == line[1]:
                value, factors = evaluate(line)
                print("This Client has a housing risk score of %s%%" % (value))
                print("Major contributing factors are:")
                print(*factors, sep = ", ")
                sys.exit()
        print("Sorry, we were unable to find anyone with that ID.")
        file.close()


def evaluate(data):
    print("Found")
    # Housed=0.77914-0.23056(EverCPS)-0.33527(Pet)+0.24641(Emotional Support animal)-0.13103(AddHousingSearch)-0.28021(Eviction)-0.47262(HealthIns)-0.38529(Translator)
    #                        LINE 21         LINE 30          LINE 32                         LINE 34?                  LINE 37            LINE 71           LINE 78
    EverCPS = (data[21] == "TRUE")
    Pet = (data[30] == "TRUE")
    esa = (data[32] == "TRUE")
    AddHousingSearch = (data[34] == "TRUE")
    Eviction = (data[37] == "TRUE")
    HealthIns = (data[71] == "TRUE")
    Translator = (data[78] == "TRUE")

    factors = []

    result = .77914
    if EverCPS:
        result -= (.23056 * int(EverCPS))
        factors.append("CPS Involvenment")
    if Pet:
        result -= (.33527 * int(Pet))
        factors.append("Pet ownership")
    if esa:
        result += (.24641 * int(esa))
        factors.append("Emotional Support Animal positively affecting data")
    if AddHousingSearch:
        result -= (.13103 * int(AddHousingSearch))
        factors.append("Additional housing search needed")
    if Eviction:
        result -= (.28021 * int(Eviction))
        factors.append("Previous eviction troubles")
    if HealthIns:
        result -= (.47262 * int(HealthIns))
        factors.append("Lacks health insurance")
    if Translator:
        result -= (.38529 * int(Translator))
        factors.append("Language barrier with translator necessary")
    result = math.trunc(result * 100)

    if factors == []:
        factors.append("No major contributing factors.")

    return result, factors

main()