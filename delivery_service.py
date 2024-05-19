def delivery_service(platforms, limit):
    if min(platforms) > limit / 2:
        return len(platforms)
    else:
        platforms.sort(reverse=True)
        count = 0
        while len(platforms) != 0:
            if len(platforms) > 1 and platforms.pop() + platforms.pop() <= limit:
                count += 1
            else:
                platforms.pop()
                count += 1
    return count


platforms = list(map(int, input().split()))
limit = int(input())

print(delivery_service(platforms, limit))
