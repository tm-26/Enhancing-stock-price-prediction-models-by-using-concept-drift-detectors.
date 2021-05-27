import csv
import matplotlib.pyplot
import os
import pandas
import sys

sys.path.append("..")
from main import main


if __name__ == "__main__":

    """
        Parameters:
        args[0] --> splitDays parameter
        Controls how many days the model waits before starting to train on the current distribution.
    """

    # Handle arguments
    splitDays = 5

    if len(sys.argv) >= 2:
        if sys.argv[1].lower() == "all":
            splitDays = -1
        else:
            try:
                splitDays = int(sys.argv[1])
                if 3 > splitDays < 31:
                    raise ValueError
                elif splitDays == 0:
                    splitDays = 5
            except ValueError:
                print("Argument error: " + str(sys.argv[1]) + " not a valid splitDays parameter")
                print("splitDays parameter needs to be an integer between 3 and 31")
                exit(-2)

    if not os.path.exists("../../results"):
        os.makedirs("../../results")
    
    if not os.path.exists("../../results/method2.csv"):
        file = open("../../results/method2.csv", "w+")
        writer = csv.writer(file)
        writer.writerow(["splitDays", "ACC", "MCC"])
        file.close()

    results = pandas.read_csv("../../results/method2.csv")

    if splitDays == -1:

        complete = []
        for i in results["splitDays"]:
            complete.append(int(i))

        for i in range(3, 31):
            if i not in complete:
                print("+------------------------------+")
                print("Starting splitDays parameter = " + str(i))
                print("+------------------------------+")
                acc, mcc = main(True, 2, i)
                results = results.append({"splitDays": i, "ACC": acc, "MCC": mcc}, ignore_index=True)
                results.to_csv("../../results/method2.csv", index=False)
        results.plot(x="splitDays", y="ACC")
        results.plot(x="splitDays", y="MCC")
        matplotlib.pyplot.show()
    else:
        print("develop me")