# Author: Morgan Eads.40
# NOTE: Nearly a copy-and-paste of Hour_Sampling.py
import random
random.seed(3230)

last_hour = 5 # last_hour - 1 = The # of hour available to choose from.
num_teachers = 14
for i in range(num_teachers):
    # Select a random number of time slots the teacher is available.
    # NOTE: The teacher has to be available to teach at least two of the classes.
    J = random.randrange(2, last_hour)
    times = []
    for j in range(J):
        addon = random.randrange(1, last_hour)
        # Cannot choose a number that has already been chosen.
        while (addon in times):
            addon = random.randrange(1, last_hour)
        times.append(addon)
    times.sort()
    print("Teacher ", i, ": ", times)
# Read as: "Teacher i is available for the jth hour."
