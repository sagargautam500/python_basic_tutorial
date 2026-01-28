# 🔷 3️⃣ reduce() – COMBINE DATA
# 📌 Meaning (Easy)
# reduce() combines all elements into ONE value.

# ✅ Python Syntax
# from functools import reduce
# reduce(function, iterable)

# Example 1: Sum of all numbers
from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, nums)
print(result)

# 🟡 JavaScript reduce()
# let nums = [1, 2, 3, 4];

# let result = nums.reduce((a, b) => a + b);
# console.log(result);

# 🔑 Use reduce() when:
# ✔ You want single result
# ✔ Sum, product, max, min, etc.

# Final all comparision
# | Feature      | map       | filter   | reduce       |
# | ------------ | --------- | -------- | ------------ |
# | Purpose      | Transform | Select   | Combine      |
# | Output       | List      | List     | Single value |
# | Python needs | `list()`  | `list()` | `functools`  |
# | JS needs     | Built-in  | Built-in | Built-in     |

# 🧠 Memory Trick (Exam Friendly)
# map → change
# filter → select
# reduce → combine