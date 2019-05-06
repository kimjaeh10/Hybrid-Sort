# Hybrid-Sort
Hybrid Sort (Insertion Sort + Merge Sort) in Python

Merge Sort has a time complexity nlog(n), which is not bad but it is not always the best solution.
Insertion Sort has a time complexiity n^2, however it can be a better way to sort the list when there are very few elements in it.

If there are less elements than the threshold, use insertion sort.
If there are more elements than the threshold, use merge sort.
