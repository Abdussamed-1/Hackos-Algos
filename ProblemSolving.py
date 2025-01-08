def mostBalancedPartition(parent, files_size):
    """
    Task1: Balanced System Files Partition
    You are tasked with implementing a function mostBalancedPartition that 
    calculates the minimum difference in file sizes when a system's directory tree is split into two parts.

    Goal:
    Partition the tree into two subtrees by cutting one branch such that the difference between the total file
    sizes of the two resulting subtrees is minimized. Return the minimum possible difference.
    """
    # Step 1: Find the total size of the tree
    n = len(parent)
    total_size = sum(files_size)

    # Create a list to store the sizes of subtrees
    subtree_sizes = [0] * n

    # Helper function to calculate the sizes of subtrees
    def calculate_subtree_size(directory):
        subtree_sizes[directory] = files_size[directory]
        for i in range(n):
            if parent[i] == directory:
                subtree_sizes[directory] += calculate_subtree_size(i)
        return subtree_sizes[directory]

    # Calculate the sizes of all subtrees starting from the root node
    calculate_subtree_size(0)

    # Step 2: Find the minimum difference
    min_difference = float('inf')
    for size in subtree_sizes:
        difference = abs(total_size - 2 * size)
        min_difference = min(min_difference, difference)

    return min_difference


# Example usage
if __name__ == "__main__":
    parent = [-1, 0, 0, 1, 1, 2]
    files_size = [1, 2, 2, 1, 1, 1]
    result = mostBalancedPartition(parent, files_size)
    print(result)  # Expected output: 1


def maxCost(cost, labels, dailyCount):
    """
    Task2:
    Maximum Cost of Laptop Count
    A company manufactures a fixed number of laptops every day. However, during testing, some laptops are labeled as "illegal" if a defect is found, and these laptops are not included in the count of legal laptops produced that day.
    Despite being defective, the cost to manufacture an illegal laptop is still incurred by the company.
    """
    total_cost = 0
    max_cost = 0
    legal_count = 0

    for i in range(len(cost)):
        total_cost += cost[i]
        if labels[i] == "legal":
            legal_count += 1

        # If the daily legal count is complete
        if legal_count == dailyCount:
            max_cost = max(max_cost, total_cost)
            total_cost = 0  # Start a new day
            legal_count = 0  # Reset the legal count

    return max_cost

# Example Test
cost = [2, 5, 3, 11, 1]
labels = ["legal", "illegal", "legal", "illegal", "legal"]
dailyCount = 2
print(maxCost(cost, labels, dailyCount))  # Output: 14