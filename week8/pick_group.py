import random

if __name__ == "__main__":
    groups = ["1","2","3","4","5","6","7","8","9"]
    team = [1,2]

    while len(groups) > 0:
        group_to_present = random.choice(groups)
        print(f"Group {group_to_present} will present next.")     
        print(f"Team {random.choice(team)} will present. The other team will do Q&A")        
        groups.remove(group_to_present)
        input()

    print("Presentations are complete.")
