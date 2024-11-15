# Author: Morgan Eads.40
import random
random.seed(3230)

last_hour = 5 # last_hour - 1 = The # of hours available to choose from.
num_students = 60
for i in range(num_students):
    # Select a random number of time slots the customer is available.
    J = random.randrange(1, last_hour)
    times = []
    for j in range(J):
        addon = random.randrange(1, last_hour)
        # Cannot choose a number that has already been chosen.
        while (addon in times):
            addon = random.randrange(1, last_hour)
        times.append(addon)
    times.sort()
    print("Customer ", i, ": ", times)
# Read as: "Customer i is available for the jth hour."
