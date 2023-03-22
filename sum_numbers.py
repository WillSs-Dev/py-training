inputs = input(
    'Type some numbers, separating them by a space, and I will sum them for you: ')

results_list = inputs.split(' ')
total_sum = 0

for result in results_list:
    if (result.isdigit()):
        total_sum += int(result)
    else:
        print(f'Error trying to sum values, {result} is an invalid value!')
        exit()

print(f'Here is the total sum of the values: {total_sum}')
