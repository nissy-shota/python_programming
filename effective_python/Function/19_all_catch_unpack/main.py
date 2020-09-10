def get_avg_ration(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)

    return scaled

length = [63, 73, 72, 60, 67, 88]

longest, *middle, shortest = get_avg_ration(length)

print(f'Longest: {longest:>4.0%}')
print(f'shortest: {shortest:>4.0%}')