def count_platforms(robots, limit):
    robots.sort()
    left_pointer = 0
    right_pointer = len(robots) - 1
    count = 0
    while left_pointer <= right_pointer:
        count += 1
        if robots[left_pointer] + robots[right_pointer] <= limit:
            left_pointer += 1
        right_pointer -= 1
    return count


robots = list(map(float, input().split()))
limit = float(input())

print(count_platforms(robots, limit))
