fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = ["alice", 20, True, 3.14]

print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

fruits[1] = "mango"
print(fruits)

fruits.append("grape")
fruits.insert(1, "kiwi")
print(fruits)

fruits.remove("mango")
fruits.pop()
fruits.pop(0)
print(fruits)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))

nums.sort()
print(nums)

nums.reverse()
print(nums)

print("apple" in fruits)
print("cherry" in fruits)

nums2 = [1, 2, 2, 3, 2, 2]
print(nums2.count(2))