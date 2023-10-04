import math
import random


calories = {
    "squat": 1.8,
    "jumping_jacks": 2.4,
    "push_ups": 2.0,
    "lunges": 2.3,
    }

def merge(distribution):
    print(distribution)
    new_distribution = []
    for i in range(2):
        new_distribution.append(distribution[0] + distribution[1])
        distribution.pop(0), distribution.pop(0)
    if len(distribution) > 0:
        new_distribution.extend(distribution)
    return new_distribution

def find_factors(num):
    """
    Finds the factors of a number
    This factor represents the number of different workouts and what the 
    target of each workout should be
    """
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

def sample_unique(values, k):
    """Samples k unique values from a list"""
    sampled_values = []
    if k > len(values):
        raise ValueError("k cannot be greater than the length of the list")
    while len(sampled_values) < k:
        val = random.choice(values)
        if val not in sampled_values:
            sampled_values.append(val)
    return sampled_values

def main():
    present_capacity = int(input("What is your current capacity? "))
    weight = int(input("What is your weight? "))
    desired_target = int(input("What is your desired volume target? "))
    step = round(0.1 * present_capacity)
    next_capacity = present_capacity + step
    
    avaliable = int(input("How many days a week are you avaliable? "))
    expected_completion = math.ceil((desired_target - present_capacity) / step)
    print("You will reach your target in: ", expected_completion, " weeks")
    print("Your next capacity will be: ", next_capacity, end=" ")
    daily_target = augment(next_capacity / avaliable)
    print("Your daily target is: ", daily_target)
    workout_distributions = find_factors(daily_target)
    workout_distribution = random.choice(workout_distributions)
    workout_distribution = [workout_distribution[1] for i in range(workout_distribution[0])]
    # if the distribution is for 4 or 5 workouts but the expected MET value for each workout is less than 15
    # merge to get smaller number of workouts
    if (len(workout_distribution) >= 4) and (workout_distribution[0] < 15) :
        workout_distribution = merge(workout_distribution)

    print("You can distribute your workout as follows: ", workout_distribution)
    selected_workouts = sample_unique(list(calories.keys()), len(workout_distribution))
    complete_info = {}
    print("You can do the following workouts: ", selected_workouts)
    for i in range(len(selected_workouts)):
        complete_info[selected_workouts[i]] = {
            "Target MET": workout_distribution[i],
            "Calories": calories[selected_workouts[i]] * (weight/80),
        }
    print(complete_info)


if __name__ == "__main__":
    main()