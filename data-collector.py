import numpy as np
import sensors

print("What letter are you currently training?")

letter = input()
print(f"now training for letter {letter}")


def train(letter):
    print(
        "Make the proper hand posisition and press enter when ready, or enter q to quit "
    )
    if input() == "q":
        return
    data = sensors.read()
    # gets an array of values representing the sensor values

    data.insert(0, letter)
    # prepends the data array with the letter (class) being trained
    with open("training-data.txt", "a") as file:
        np.savetxt(file, [data], fmt="%s", delimiter="\t")
        # appends data to human readable text file, where the first column is the letter being trained

    train(letter)  # run again to speed up training process


train(letter)
