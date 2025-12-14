import heapq

def calculate_total(cable_lengths):
    if not cable_lengths:
        return 0
    total_cost = 0
    heapq.heapify(cable_lengths)

    while len(cable_lengths)>1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        cost = first + second
        total_cost += cost

        heapq.heappush(cable_lengths, cost)
    return total_cost

if __name__ == "__main__":
    cable_lengths = [3, 7, 12, 4, 1]
    result=calculate_total(cable_lengths)
    print(f"Total cost: "+str(result))
