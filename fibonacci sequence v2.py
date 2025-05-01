#fibonacci sequence v2  10/3/2024 12am

counter = 2
new_num = 1
prev_num = 0

print(prev_num)

while counter <= 50:
    print(new_num)
    new_num += prev_num
    prev_num = new_num - prev_num
    counter += 1