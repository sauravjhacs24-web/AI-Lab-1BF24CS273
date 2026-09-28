def vacuum_cleaner_agent():
    # Goal State: Both locations A and B must be Clean ('0')
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # User inputs for initial environment configuration
    location = input("Enter starting location of Vacuum Agent (A or B): ").strip().upper()
    status_current = input(f"Enter status of Location {location} (1 for Dirty, 0 for Clean): ").strip()
   
    other_location = 'B' if location == 'A' else 'A'
    status_other = input(f"Enter status of Location {other_location} (1 for Dirty, 0 for Clean): ").strip()

    # Environment status dictionary
    environment = {
        location: status_current,
        other_location: status_other
    }

    print("\n--- Simulation Started ---")
    print(f"Initial State: {environment}")

    # Process first location
    if environment[location] == '1':
        print(f"Location {location} is Dirty.")
        print(f"Action: SUCK (Cleaning Location {location})")
        environment[location] = '0'
        cost += 1
    else:
        print(f"Location {location} is already Clean.")

    # Move to the adjacent location
    if location == 'A':
        print("Action: MOVE RIGHT (A -> B)")
        location = 'B'
        cost += 1
    else:
        print("Action: MOVE LEFT (B -> A)")
        location = 'A'
        cost += 1

    # Process second location
    if environment[location] == '1':
        print(f"Location {location} is Dirty.")
        print(f"Action: SUCK (Cleaning Location {location})")
        environment[location] = '0'
        cost += 1
    else:
        print(f"Location {location} is already Clean.")

    # Check goal state
    print("\n--- Simulation Summary ---")
    print(f"Final Environment State: {environment}")
    print(f"Total Cost (Steps Taken): {cost}")

    if environment == goal_state:
        print("Result: Goal achieved! Both locations are clean.")

if __name__ == "__main__":
    vacuum_cleaner_agent()