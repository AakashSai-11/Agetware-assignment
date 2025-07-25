## 🧩 Problem: Combining Two Lists Based on Overlapping Positions

In this task, you're given **two lists** of elements, where each element is a dictionary with:

- `positions`: a pair of integers representing a range (start and end).
- `values`: a list of values associated with that range.

### 📋 Objective

You need to **combine** elements from both lists into a single list. But here's the rule:

- If an element from one list **overlaps more than 50%** with an element in the other list, then their values should be **merged**.
- When merging, **keep the position of the element that comes first**.
- After merging everything, the final list should be **sorted by the left position**.

### 🔁 Example

Input:

```python
list1 = [
    {"positions": [2, 10], "values": [2, 5, 7]},
    {"positions": [15, 20], "values": [4, 5]}
]

list2 = [
    {"positions": [5, 8], "values": [9, 4, 2]},
    {"positions": [16, 19], "values": [3, 4]}
]
```

Output:

```python
[
    {"positions": [2, 10], "values": [2, 5, 7, 9, 4, 2]},
    {"positions": [15, 20], "values": [4, 5, 3, 4]}
]
```

### 🧠 Key Concepts Used

- **Overlapping check**: We calculate how much two ranges intersect and compare it with half the length of the second range.
- **Merging values**: If the overlap is enough, we extend the values list.
- **Sorting**: After combining, the list is sorted by the **starting (left) position** of each element.

### ✅ Assumptions

- Only two input lists are given.
- Values are merged **only if the overlap condition is met**.
- Merging considers **one-way overlap** (typically `list2` into `list1`).
- Positions in the final output always reflect the **first element**.
