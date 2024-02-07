x = 25
epsilon = 0.01
step = 0.1
guess = 4.5

while guess <= x:
    print(abs(guess**2 -x))
    print(abs(guess**2 -x) - epsilon)
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))