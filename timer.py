import time 

user_input = int(input("Enter amount of time in seconds: "))
for x in range(user_input, 0, -1):
    seconds = int(x % 60)
    minutes = int((x/ 60) % 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")