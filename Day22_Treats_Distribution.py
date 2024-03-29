"""
Say we are given an integer array of an even length, where different numbers in the array represent certain kinds of snack or treats. Each number maps to/represents one kind of snack. So the following array would have two kinds: snack type 3 and type 2:

const snacks = [3, 3, 2, 2];
You need to distribute these snacks equally in number to a brother and sister duo. Write an algorithm treatsDistribution(snacks: array) to return the maximum number of unique kinds of snacks the sister could gain.

const snacks = [2, 2, 3, 3, 4, 4];
treatsDistribution(snacks);
// 3
In the above example, there are three different kinds of snacks (2, 3 and 4), and a quantity of two each. Thus, the sister can have snacks [2, 3, 4] and the brother will have snacks [2, 3, 4] as well. The sister has at most 3 different unique kinds of snacks.

const snacks = [1, 1, 2, 4]
treatsDistribution(snacks)
// 2
In this example, the sister can have a collection of snacks consisting of [2, 4] and the brother has snack collection [1, 1]. The sister can have up to 2 different kinds of snacks, while the brother has only 1 kind of snacks.

You may assume that the length of the given array is in range is even, and that there's less than 10,000 elements.
"""

def treatsDistribution(snacks):

    varietyOfSnacks = []
    for i in range(len(snacks)):
        if snacks[i] not in varietyOfSnacks:
            varietyOfSnacks.append(snacks[i])

    if len(varietyOfSnacks) >= len(snacks)/2:
        return len(snacks)/2
    else:
        return len(varietyOfSnacks)

if __name__ == '__main__':
    snacks = [7, 7]
    print(treatsDistribution(snacks))
