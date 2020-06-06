start = int(input())
end = int(input())

for i in range(start, end + 1):
    sum_odd = 0
    sum_even = 0
    i_as_string = str(i)
    for j in range(0, len(i_as_string)):
        current = int(i_as_string[j])

        if (j + 1) % 2 == 0:
            sum_even += current
        else:
            sum_odd += current
    if sum_odd == sum_even:
        print(i, end=" ")
