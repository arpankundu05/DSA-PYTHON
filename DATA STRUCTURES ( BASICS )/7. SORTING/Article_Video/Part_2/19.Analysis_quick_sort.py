"""Case	Time Complexity	Explanation"""
# Best Case	O(n log n)	"""The array is evenly split into two halves at each step (balanced partitions)."""
# Average Case	O(n log n)	"""The partitioning is reasonably balanced on average."""
# Worst Case	O(n²)	"""The pivot always results in unbalanced partitions (e.g., sorted or reverse sorted array with Lomuto partitioning)."""

""" Space Complexity Analysis"""
# Case	Space Complexity	Explanation 
# Worst Case	O(n)	If recursion depth reaches n (e.g., already sorted array).
# Best Case	O(log n)	If partitions are balanced, recursion depth is log n.