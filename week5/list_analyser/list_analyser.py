numbers = [12, 5, 27, 8, 14, 27, 3]

def analyser(numbers):
    highest = float('-inf')
    lowest = float('inf')
    total = 0
    average = 0
    aboveaverage = 0
    count = 0
    indexofhighest = 0
    indexoflowest = 0
    index = 0

    for num in numbers:
        count += 1
        total += num

        if num > highest:
            highest = num
            indexofhighest = index
        elif num < lowest:
            lowest = num
            indexoflowest = index
        index += 1
    average = total/count


    for num in numbers:
        if num > average:
            aboveaverage += 1
    

    result = f"highest: {highest} at {indexofhighest}\nlowest: {lowest} at {indexoflowest}\ntotal={total}\naverage: {average}\nnumbers above average: {aboveaverage}"
    print(result)
analyser(numbers)