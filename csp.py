import math

print("Welcome to Student Locker Program")
lockers = 1000
students = 1000
lockersOpen = int(math.sqrt(lockers))
lockersClosed = lockers - lockersOpen

resultLockerIsOpen = {}

print("\nLockers"),

for a in range(1, lockers + 1):
    resultLockerIsOpen[a] = False
    for b in range(1, students + 1):
        if a % b == 0:
            resultLockerIsOpen[a] = not resultLockerIsOpen[a]
    if resultLockerIsOpen[a]:
        print(f"{a},"),
print(
    f"lockers are open.The total lockers open are: {lockersOpen} and closed: {lockersClosed}."
)
