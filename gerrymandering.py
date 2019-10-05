info = list(map(int, input().split()))
precincts, districts = info[0], info[1]
votes = []
for _ in range(districts):
    votes.append([0, 0])

for _ in range(precincts):
    allo = list(map(int, input().split()))
    ord_district, A_vote, B_vote = allo[0], allo[1], allo[2]
    votes[ord_district-1][0] += A_vote
    votes[ord_district - 1][1] += B_vote

A_total = 0
B_total = 0
Total = 0

for i in votes:
    if i[0] > i[1]:
        Total += i[0] + i[1]
        A_wasted = i[0] - (i[0] + i[1]) // 2 - 1
        B_wasted = i[1]
        A_total += A_wasted
        B_total += B_wasted
        print("A {} {}".format(A_wasted, B_wasted))
    elif i[0] < i[1]:
        Total += i[0] + i[1]
        B_wasted = i[1] - (i[0] + i[1]) // 2 - 1
        A_wasted = i[0]
        A_total += A_wasted
        B_total += B_wasted
        print("B {} {}".format(A_wasted, B_wasted))

print("{:.10f}".format(abs(A_total - B_total) / Total))