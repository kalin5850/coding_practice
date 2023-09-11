# Google Question
# Given a list = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given a list = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given a list = [2, 3, 4, 5]
# It should return None


def first_recurring_character(input):
    result = {}
    for number in input:
        if number not in result:
            result[number] = 1
        else:
            return number
    return None


if __name__ == "__main__":
    input = [2, 3, 4, 5]
    print(first_recurring_character(input))

# Bonus... What if we had this:
#  [2,5,5,2,3,5,1,2,4]
#  return 5 because the pairs are before 2,2
