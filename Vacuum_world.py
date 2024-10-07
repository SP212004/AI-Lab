#2 quadrants vacuum world problem
initial_states = []
cost = 0
goal_state = ["A", 0, "B", 0]

def vacuum_world(location):
    global cost
    current_state = ["A", initial_states[0], "B", initial_states[1]]
    print("Current state:",current_state)
    while current_state[1] != 0 or current_state[3] != 0:
        if location == "A":
            if current_state[1] == 1:
                print("Location A is dirty.")
                print("Cleaning Location A...")
                cost += 1
                current_state[1] = 0
                print("Cost for suck:", cost)
            print("Moving to B...")
            location = "B"
        elif location == "B":
            if current_state[3] == 1:
                print("Location B is dirty.")
                print("Cleaning Location B...")
                cost += 1
                current_state[3] = 0
                print("Cost for suck:", cost)
            print("Moving to A...")
            location = "A"
        print("Current state:",current_state)
    print("Final state:", current_state)
    print("Total cost:", cost)

for room in ['A', 'B']:
    state = input(f"Is Room {room} dirty? (1 for dirty, 0 for clean): ").strip()
    while state not in ['0', '1']:
        print("Invalid input. Please enter 1 for dirty or 0 for clean.")
        state = input(f"Is Room {room} dirty? (1 for dirty, 0 for clean): ").strip()
    initial_states.append(int(state))

location = input("Enter the starting location of the vacuum cleaner (A or B): ").strip().upper()
while location not in ['A', 'B']:
    print("Invalid location. Please enter 'A' or 'B'.")
    location = input("Enter the starting location of the vacuum cleaner (A or B): ").strip().upper()

vacuum_world(location)

#4 quadrants vacuum world problem
initial_states = []
cost = 0
goal_state = [0, 0, 0, 0]

def vacuum_world(location):
    global cost
    current_state = [initial_states[0], initial_states[1], initial_states[2], initial_states[3]]
    print("Current state:", current_state)

    while current_state != goal_state:
        if location == "A":
            if current_state[0] == 1:
                print("Location A is dirty.")
                print("Cleaning Location A...")
                cost += 1
                current_state[0] = 0
                print("Cost for cleaning:", cost)
            print("Moving to B...")
            location = "B"
        elif location == "B":
            if current_state[1] == 1:
                print("Location B is dirty.")
                print("Cleaning Location B...")
                cost += 1
                current_state[1] = 0
                print("Cost for cleaning:", cost)
            print("Moving to C...")
            location = "C"
        elif location == "C":
            if current_state[2] == 1:
                print("Location C is dirty.")
                print("Cleaning Location C...")
                cost += 1
                current_state[2] = 0
                print("Cost for cleaning:", cost)
            print("Moving to D...")
            location = "D"
        elif location == "D":
            if current_state[3] == 1:
                print("Location D is dirty.")
                print("Cleaning Location D...")
                cost += 1
                current_state[3] = 0
                print("Cost for cleaning:", cost)
            print("Moving to A...")
            location = "A"
        print("Current state:", current_state)
    print("Final state:", current_state)
    print("Total cost:", cost)

for quadrant in ['A', 'B', 'C', 'D']:
    state = input(f"Is Quadrant {quadrant} dirty? (1 for dirty, 0 for clean): ").strip()
    while state not in ['0', '1']:
        print("Invalid input. Please enter 1 for dirty or 0 for clean.")
        state = input(f"Is Quadrant {quadrant} dirty? (1 for dirty, 0 for clean): ").strip()
    initial_states.append(int(state))

location = input("Enter the starting location of the vacuum cleaner (A, B, C, or D): ").strip().upper()
while location not in ['A', 'B', 'C', 'D']:
    print("Invalid location. Please enter 'A', 'B', 'C', or 'D'.")
    location = input("Enter the starting location of the vacuum cleaner (A, B, C, or D): ").strip().upper()

vacuum_world(location)
