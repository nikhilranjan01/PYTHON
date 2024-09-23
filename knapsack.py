def knapsack_greedy(profits, weights, capacity):
    n = len(profits)
    # Calculate profit-to-weight ratios for each item
    ratios = [(profits[i] / weights[i], i) for i in range(n)]
    # Sort items based on profit-to-weight ratios in descending order
    ratios.sort(reverse=True, key=lambda x: x[0])

    selected = [0] * n
    current_weight = 0
    final_profit = 0.0

    # Iterate through sorted items
    for ratio, i in ratios:
        # If adding the entire item won't exceed the capacity, add it
        if current_weight + weights[i] <= capacity:
            selected[i] = 1
            current_weight += weights[i]
            final_profit += profits[i]
        else:
            # If adding the entire item would exceed the capacity, add a fraction
            remaining_weight = capacity - current_weight
            final_profit += profits[i] * (remaining_weight / weights[i])
            break

    # Print the selected items
    print("Selected items:")
    for i in range(n):
        if selected[i]:
            print(f"Item {i + 1}")

    print(f"Maximum profit in Knapsack = {final_profit:.2f}")

# Given profits and weights
profits = [6, 10, 18, 15, 3, 5, 7]
weights = [1, 6, 4, 5, 1, 3, 7]
capacity = 15

# Solve the Knapsack problem using the greedy approach
knapsack_greedy(profits, weights, capacity)
