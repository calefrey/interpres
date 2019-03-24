import numpy as np
import sensors

letter = "init"

print("What letter are you currently training?")
while(len(letter) > 1):
    letter = input().upper()
    if len(letter) > 1:
        print("Please enter a SINGLE letter:")
print(f"now training for letter {letter}")


def train(letter):
    print("Make the proper hand position and press enter when ready or enter q to quit")

    if input().lower() == "q":
        quit()
    data = sensors.read()
    # gets an array of values representing the sensor values

    data.insert(0, letter)
    # prepends the data array with the letter (class) being trained
    with open("training-data.txt", "a") as file:
        np.savetxt(file, [data], fmt="%s", delimiter="\t")
        # appends data to human readable text file, where the first column is the letter being trained

    train(letter)  # run again to speed up training process


train(letter)
quit()
