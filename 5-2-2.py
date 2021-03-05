numbers = iter(list(range(1, 101)))
for i in numbers:
    print(i)
    try:
        next(numbers)
        next(numbers)
    except StopIteration:
        break