# Simple Voting System

candidate1 = 0
candidate2 = 0
candidate3 = 0

print("Welcome to the Simple Voting System")
print("1. Candidate A")
print("2. Candidate B")
print("3. Candidate C")

while True:
    vote = input("Enter candidate number (1-3): ")

    if vote == "1":
        candidate1 += 1
    elif vote == "2":
        candidate2 += 1
    elif vote == "3":
        candidate3 += 1
    else:
        print("Invalid vote")

    cont = input("Another voter? (yes/no): ").lower()
    if cont != "yes":
        break

print("\nVoting Results")
print("Candidate A:", candidate1)
print("Candidate B:", candidate2)
print("Candidate C:", candidate3)

if candidate1 > candidate2 and candidate1 > candidate3:
    print("Winner: Candidate A")
elif candidate2 > candidate1 and candidate2 > candidate3:
    print("Winner: Candidate B")
elif candidate3 > candidate1 and candidate3 > candidate2:
    print("Winner: Candidate C")
else:
    print("It's a tie")
