# 🔷 List (Python) vs Array (JavaScript)
# 1️⃣ What is a List / Array?
# Python List             	           JavaScript Array
# Collection of values	               Collection of values
# Can store different data types	       Can store different data types
# Built-in data type                  	Built-in object

# 2️⃣ Creating List / Array
# JavaScript Array
# let nums = [1, 2, 3, 4];
# let data = [1, "Sagar", true];

# Python List
nums = [1, 2, 3, 4]
data = [1, "Sagar", True]


# 3️⃣ Accessing Elements (Indexing)
# JavaScript
# console.log(nums[0]);   // 1

# Python
print(nums[0])   # 1
# ✔ Index starts from 0


# 4️⃣ Negative Indexing (Python Only 🔥)
# JavaScript
# nums[nums.length - 1];

# Python
nums[-1]   # last element


# 5️⃣ Length of List / Array
# JavaScript
# nums.length;

# Python
len(nums)


# 6️⃣ Changing Elements (Mutable)
# JavaScript
# nums[0] = 10;

# Python
nums[0] = 10
# ✔ Lists & Arrays are mutable


# 7️⃣ Adding Elements
# JavaScript
# nums.push(5);      // add at end
# nums.unshift(0);  // add at start

# Python
nums.append(5)    # add at end
nums.insert(0, 0) # add at index


# 8️⃣ Removing Elements
# JavaScript
# nums.pop();      // remove last
# nums.shift();   // remove first

# Python
nums.pop()       # remove last
nums.pop(0)      # remove by index
nums.remove(3)   # remove by value


# 9️⃣ List / Array Slicing
# JavaScript
# nums.slice(1, 4);

# Python
nums[1:4]


# 🔟 Loop Through List / Array
# JavaScript
# for (let n of nums) {
#   console.log(n);
# }

# Python
for n in nums:
    print(n)


# 1️⃣1️⃣ Check Element Exists
# JavaScript
# nums.includes(3);

# Python
3 in nums


# 1️⃣2️⃣ Sorting
# JavaScript
# nums.sort();

# Python
nums.sort()


# 1️⃣3️⃣ Important List Methods (Python)
# Method	    Work
# append()	Add element
# insert()	Add at index
# remove()	Remove by value
# pop()	    Remove by index
# sort()	    Sort list
# reverse()	Reverse list
# count()	    Count value
# index()	    Get index

nums = [1, 2, 3, 2]

print(nums.count(2))  # 2
print(nums.index(3))  # 2


# 1️⃣4️⃣ List Can Store Mixed Data
data = [1, "Python", 3.5, True]
# (JS arrays also allow this)


# 1️⃣5️⃣ List Comprehension (Python Only 🔥)
nums = [1, 2, 3, 4]
square = [n * n for n in nums]

print(square)
# ❌ No direct JS equivalent (closest is map())


# 🔑 Final Comparison Summary (Exam)
# Feature  	          JS Array	      Python List
# Mutable	             Yes	         Yes
# Negative indexing	     ❌         	  ✅
# Slicing	              slice()	   [start:end]
# Add element	          push()	    append()
# One-line creation	      ❌	         list comprehension