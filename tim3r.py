# https://stackoverflow.com/questions/18406165/creating-a-timer-in-python/18406263


import time
run = input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 1:
        print(">>>>>>>>>>>>>>>>>>>>> {}".format(mins))
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
