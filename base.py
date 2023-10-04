import math
import random


calories = {
    "squat": 1.8,
    "jumping_jacks": 2.4,
    "push_ups": 2.0,
    "lunges": 2.3,
    }

def merge_targets(distribution, n_iterations=2):
    """
    Merge a number of workout targets to get a smaller number of workouts
    """
    print(distribution)
    new_distribution = []
    for i in range(n_iterations):
        new_distribution.append(distribution[0] + distribution[1])
        distribution.pop(0), distribution.pop(0)
    if len(distribution) > 0:
        new_distribution.extend(distribution)
    return new_distribution

def find_factors(num, MAX=5):
    """
    Finds the factors of a number
    This factor represents the number of different workouts and what the 
    target of each workout should be
    """
    factors = []
    for factor_i in range(2, MAX+1):
        if num % factor_i == 0:
            factor_j = num / factor_i
            factors.append((factor_i, factor_j))
    return factors

def augment(num):
    """
    Makes the values divisible by 5
    This will come handy later to make the process of division of workouts for 
    different days easier
    """
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

def get_workout_info(workout, target, weight):
    """
    Returns the workout info
    """
    STANDARD_WEIGHT = 80
    calorie_per_workout = calories[workout] * (weight/STANDARD_WEIGHT)
    total_n = augment(target / calorie_per_workout)
    reps_and_no_factor = find_factors(total_n)
    reps_and_no_factor = random.choice(reps_and_no_factor)
    # flatten the reps_and_no_factor with len = no of reps and value = no of cycles
    number_per_rep = [reps_and_no_factor[1] for i in range(reps_and_no_factor[0])]
    # if the no of reps is more than 4 and the no cycles is less than 15
    # merge to get smaller number of workouts
    if (len(number_per_rep) >= 4) or (number_per_rep[1] < 15) :
        number_per_rep = merge_targets(number_per_rep)
    return {
        "Original target MET": target,
        "Calories": calorie_per_workout,
        "reps_count": len(number_per_rep),
        "No of cycles for reps": number_per_rep,
        "Target to achieve": sum(number_per_rep) * calorie_per_workout
    }

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
    target_distributions = find_factors(daily_target)
    target_distribution = random.choice(target_distributions)
    # flatten the target distribution with len = no of different exercise and values = target met for that workout
    target_distribution = [target_distribution[1] for i in range(target_distribution[0])]
    # if the distribution is for 4 or 5 workouts but the expected MET value for each workout is less than 15
    # merge to get smaller number of workouts
    if (len(target_distribution) >= 4) and (target_distribution[0] < 15) :
        target_distribution = merge_targets(target_distribution)

    print("You can distribute your workout as follows: ", target_distribution)
    selected_workouts = sample_unique(list(calories.keys()), len(target_distribution))
    complete_info = {}
    print("You can do the following workouts: ", selected_workouts)
    for i in range(len(selected_workouts)):
        complete_info[selected_workouts[i]] = get_workout_info(selected_workouts[i], target_distribution[i], weight)
        # complete_info[selected_workouts[i]] ={
        #     "Target MET": workout_distribution[i],
        #     "Calories": calories[selected_workouts[i]] * (weight/80),
        #     "reps_count": get_reps_count(complete_info, selected_workouts[i])
        # }
    print(complete_info)


if __name__ == "__main__":
    main()