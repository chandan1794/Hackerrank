no_of_items = int(raw_input())

items = []
items = raw_input().split(" ")

items = [int(i) for i in items] #comprehension

#print hash(items)
items = tuple(items)
print hash(items)
