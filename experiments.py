import sys

str_split = sys.stdin.read().split(',')

current_hand = [int(x) if x.strip().isdigit() else x.strip() for x in str_split]

nums_dict = {
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 0,
    8: 0,
    9: 0,
    10: -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1,
}
result = sum([nums_dict[i] for i in current_hand])
print(result)