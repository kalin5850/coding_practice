if __name__ == "__main__":
    words = ["zebra", "fat", "apply", "lion", "ink"]
    # sort words alphabetically
    words.sort()  # words = ["apply", "fat", "ink", "lion", "zebra"]

    nums = [40, 100, 1, 5, 25, 10]
    # sort nums in ascending order
    nums.sort()  # nums = [1, 5, 10, 25, 40, 100]
    print(nums)
    # sort nums in descending order
    nums.sort(reverse=True)  # nums = [100, 40, 25, 10, 5, 1]
    print(nums)

    # task tuples (description, priority)
    tasks = [("Cook dinner", 3), ("Buy grocery", 5)]

    # sort tasks by priority in ascending order
    sorted_tasks = sorted(tasks, key=lambda task: task[1])
    print(sorted_tasks)
    sorted_tasks = sorted(tasks, key=lambda task: task[0])
    print(sorted_tasks)
    # or use cmp_to_key
    # sorted_tasks = sorted(tasks, key=cmp_to_key(lambda t1, t2: t1[1] - t2[1])))
    # sorted_tasks = [('Buy grocery', 3), ('Cook dinner', 5)]
