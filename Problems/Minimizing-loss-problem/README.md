## 💸 Problem: Minimizing Loss

Rajeev is analyzing the projected prices of a house over the next several years. His goal is to **buy** the house in one year and **sell** it in a later year — but he must do so at a **loss**.

The objective is to **minimize the loss**, i.e., find the smallest positive difference between the buy and sell prices, where:

- **Buy year < Sell year**
- **Buy price > Sell price**

---

### 🧠 Example:

```python
prices = [20, 15, 7, 2, 13]
```

- Buying in **year 1** (price = 20) and selling in **year 5** (price = 13) gives a **loss of 7**.
- Buying in **year 2** (price = 15) and selling in **year 5** (price = 13) gives a **loss of 2**.

✅ The minimum loss happens when buying in **year 2** and selling in **year 5**.

---

### ✅ Output:

function returns a tuple:

```python
(buy_year_index, sell_year_index, loss_value)
```

Indices are **0-based**, i.e., index 1 = Year 2.

---

### NOTE :-

If there are no years where he cant sell the house for a loss, the output is given as 'No valid years for minimum loss'.

---

### 🧾 Sample Usage:

```python
print(minimize_loss([20,15,7,2,13]))
# Output: (1, 4, 2)
```
