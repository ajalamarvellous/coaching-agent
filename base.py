import math


def find_factors(num):
    MAX = 5
    factors = []
    for factor_i in range(2, MAX+1):
        if num % factor_i == 0:
            factor_j = num / factor_i
            factors.append((factor_i, factor_j))
    return factors

def augment(num):
    """Makes the values divisible by 5"""
    num = round(num)
    while num % 5 != 0:
        num += 1
    return num

def main():
    present_capacity = int(input("What is your current capacity? "))
    desired_target = int(input("What is your desired volume target? "))
    step = round(0.1 * present_capacity)
    next_capacity = present_capacity + step
    
    avaliable = int(input("How many days a week are you avaliable? "))
    expected_completion = math.ceil((desired_target - present_capacity) / step)
    print("You will reach your target in: ", expected_completion, " weeks")
    print("Your next capacity will be: ", next_capacity, end=" ")
    daily_target = augment(next_capacity / avaliable)
    print("Your daily target is: ", daily_target)
    workout_distribution = find_factors(daily_target)
    print("You can distribute your workout as follows: ", workout_distribution)


if __name__ == "__main__":
    main()