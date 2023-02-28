import time


timestamp = time.strftime('%H:%M:%S')
print("The time is: ")
print(timestamp)

t1 = int(time.strftime('%H'))
print(timestamp, "Hours")
timestamp = time.strftime('%M')
print(timestamp, "Minutes")
timestamp = time.strftime('%S')
print(timestamp, "Seconds")
if (t1 <= 12 or t1 <= 5):
    print("Good Morning ABMOHIZ")
elif(t1 > 12 and t1 <= 17):
    print("Good after noon ABMOHIZ")
elif (t1 > 18 and t1 <= 21):
    print("Good Evening ABMOHIZ")
else:
    print("Sleep its getting late")