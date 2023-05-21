# while - Conditional

x = 1
running = True
while running:              # escape ?
    x += 1                  # x = x + 1
    print(x)
    if x > 10:
        running = False

x = 1
while True:              # escape ?
    x += 1               # x = x + 1
    print(x)
    if x > 10:
        break