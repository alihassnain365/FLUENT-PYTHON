def count_items(items):
    """counts the items and return"""
    count = 0
    for item in items:
        count += 1
    return count
print(count_items([1, 2, 3]))          # 3
print(count_items(("a", "b")))         # 2
print(count_items({10, 20, 30, 40}))   # 4
