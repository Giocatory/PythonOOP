import sys

table_non_parsed, hand_non_parsed = sys.stdin.read().split(',')

table_cards = table_non_parsed.split()
hand_cards = hand_non_parsed.split()

r = [i[-1] for i in table_cards] + [i[-1] for i in hand_cards]
res = any([r.count(i)>=5 for i in 'DHCS'])
print('Flush' if res else 'No Flush')