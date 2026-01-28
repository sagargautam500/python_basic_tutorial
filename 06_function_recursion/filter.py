# 🔷 2️⃣ filter() – SELECT DATA
# 📌 Meaning (Easy)
# filter() selects elements that satisfy a condition.

# ✅ Python Syntax
# filter(function, iterable)

nums = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, nums))
print(result)


# 🟡 JavaScript filter()
# let nums = [1, 2, 3, 4, 5];

# let result = nums.filter(x => x > 3);
# console.log(result);

# 🔑 Use filter() when:
# ✔ You want to remove unwanted elements
# ✔ Output list size may change