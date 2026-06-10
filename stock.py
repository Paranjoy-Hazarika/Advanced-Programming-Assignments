books_stock = [
        {"obj 1": 10},
        {"obj 2": 15},
        {"obj 3": 12},
        {"obj 4": 9},
        {"obj 5": 5},
        {"obj 6": 20},
        {"obj 7": 11},
    ]

print("Stock: ")

for i in books_stock:
    for key, value in i.items():
        if value < 10:
            print(f"{key} -> {value}")