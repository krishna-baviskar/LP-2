# Format: (Job_ID, Deadline, Profit)
jobs = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27), ('J4', 1, 25), ('J5', 3, 15)]
jobs.sort(key=lambda x: x[2], reverse=True) # Sort by profit

slots = [None] * max(j[1] for j in jobs)
for j in jobs:
    for s in range(min(len(slots), j[1]) - 1, -1, -1):
        if slots[s] is None:
            slots[s] = j[0]
            break

print("Scheduled Sequence:", [s for s in slots if s])
