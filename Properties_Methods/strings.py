text = "hello, world! "

print(text.upper())
print(text.lower())
print(text.title())

print(text.strip())
print(text.lstrip())
print(text.rstrip())

print(text.find("world"))
print(text.count("1"))
print(text.endswith("!  "))

print(text.replace("world" , "python"))
print(text.strip() .replace(",",""))

sentence = "apple,banana,cherry"
parts = sentence.split(",")
print(parts)

words = "hello world python"
print(words.split())

items = ["apple", "banana", "cherry"]
print(", ".join(items))

print("world" in text)
print("xyz" in text)

