import sys
import csv

def main():

    #file = open("../../assets/Data2.csv", "r")
    #file = open("C:/Users/Xanatos/Desktop/FP/Darth-J-Squared.github.io/assets/Data2.csv", "r")
    #with open("C:/Users/Xanatos/Desktop/FP/Darth-J-Squared.github.io/assets/Data2.csv", "r") as file:
    with open("../../assets/Data2.csv", "r") as file:
        read = csv.reader(file, delimiter=",")

        ID = input("What Person ID are you looking for?")

        for line in read:
            #split = line.split(",")
            if ID == line[1]:
                output = evaluate(line)
                print("This Client has a housing risk score of %s%%" % (output * 100))
                sys.exit()
        print("Sorry, we were unable to find anyone with that ID.")
        file.close()


def evaluate(data):
    print("Found")
    # Housed=0.77914-0.23056(EverCPS)-0.33527(Pet)+0.24641(Emotional Support animal)-0.13103(AddHousingSearch)-0.28021(Eviction)-0.47262(HealthIns)-0.38529(Translator)
    #                        LINE 21         LINE 30          LINE 32                         LINE 34?                  LINE 37            LINE 71           LINE 78
    result = .77914
    result -= (.23056 * int(data[21] == "TRUE"))
    result -= (.33527 * int(data[30] == "TRUE"))
    result += (.24641 * int(data[32] == "TRUE"))
    result -= (.13103 * int(data[34] == "TRUE"))
    result -= (.28021 * int(data[37] == "TRUE"))
    result -= (.47262 * int(data[71] == "TRUE"))
    result -= (.38529 * int(data[78] == "TRUE"))
    return result

main()