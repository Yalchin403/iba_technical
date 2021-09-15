def main(cars: list, k: int):
    n = len(cars)
    range_ = n + 1 - k
    cars.sort()  # quick sort or other custom sorts can also be used
    print(cars)
    result = float('inf')  # set a variable with infinite size
    for i in range(range_):
        result = min(result, cars[i+k-1] - cars[i])
    result += 1
    return result


cars = list(map(int, input("Enter car slots separated by space: ").split()))
k = int(input("Please enter the value for k: "))


if __name__ == "__main__":
    print(main(cars, k))
