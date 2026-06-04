def filter_multiples_of_10(nums):
    for num in nums:
        if num % 10 == 0:
            yield num

nums = [10, 15, 20, 25, 30]

for num in filter_multiples_of_10(nums):
    print(num)