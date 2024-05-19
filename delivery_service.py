def delivery_service(robots: list, limit: float):
    if min(robots) > limit / 2 or len(robots) == 1:
        return len(robots)
    else:
        robots.sort(reverse=True)
        count_platforms = 0
        count_robots = 0
        last = -1
        penult = last - 1
        while True:
            if (len(robots) > count_robots + 1
                    and robots[last] + robots[penult] <= limit):
                last -= 2
                penult -= 2
                count_platforms += 1
                count_robots += 2
            else:
                count_platforms += len(robots[last::-1])
                break
    return count_platforms


robots = list(map(float, input().split()))
limit = float(input())

print(delivery_service(robots, limit))
