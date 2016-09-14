import itertools

#Collect cards for hand(1-5)
#todo require int between 1-13 for this part
print('Welcome. Please enter your cards as numbers (K=13, Q=12, J=11)')
card1 = input('Enter the turn-up card:')

card2 = input('Enter your first card:')

card3 = input('Enter your second card:')

card4 = input('Enter your third card:')

card5 = input('Enter your fourth card:')

hand = card1, card2, card3, card4, card5

print('Thanks your hand is:', hand)

#todo Have a way to redo hand if incorrect

#define values (J,Q,K = 10)
values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 10, '12': 10, '13': 10}

score = 0

#Check for sum of 15(all combos)
for x in itertools.combinations(hand, 2):
    if (values.get(x[0]) + values.get(x[1])) == 15:
        score = score + 2
        print('15 for 2', x)
for x in itertools.combinations(hand, 3):
    if (values.get(x[0]) + values.get(x[1]) + values.get(x[2])) == 15:
        score = score + 2
        print('15 for 2', x)
for x in itertools.combinations(hand, 4):
    if (values.get(x[0]) + values.get(x[1]) + values.get(x[2]) + values.get(x[3])) == 15:
        score = score + 2
        print('15 for 2', x)
for x in itertools.combinations(hand, 5):
    if (values.get(x[0]) + values.get(x[1]) + values.get(x[2])+ values.get(x[3])+ values.get(x[4])) == 15:
        score = score + 2
        print('15 for 2', x)


#Check for pairs(2 card combos only)
for x in itertools.combinations(hand, 2):
    if ((x[0]) == (x[1])):
        score = score + 2
        print('Pair for 2', x)

#Check for straight(3-5 card combos)
for a in itertools.combinations(hand, 5):
    b = (int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]))
    c = sorted(b)
    if c[4] - c[3] == 1 and c[3] - c[2] == 1 and c[2] - c[1] == 1 and c[1] - c[0] == 1:
        score = score + 5
        print('Straight of 5 for 5', a)
        break
else:
    for d in itertools.combinations(hand, 4):
        e = (int(d[0]), int(d[1]), int(d[2]), int(d[3]))
        f = sorted(e)
        if f[3] - f[2] == 1 and f[2] - f[1] == 1 and f[1] - f[0] == 1:
            score = score + 4
            print('Straight of 4 for 4', d)
            break
    else:
        for x in itertools.combinations(hand, 3):
            y = (int(x[0]), int(x[1]), int(x[2]))
            z = sorted(y)
            if z[2] - z[1] == 1 and z[1] - z[0] == 1:
                score = score + 3
                print('Straight of 3 for 3', x)

#todo figure out how to handle flushes and nobs

#Provides score
print('Your score is', score, 'if all suits match add 5')