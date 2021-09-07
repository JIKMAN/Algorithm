enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def solution(enroll, referral, seller, amount):
    tree = {'-' : 'root'}
    sell = {'-' : 0}
    for i in range(len(enroll)):
        child = enroll[i]
        parent = referral[i]
        sell[child] = 0
        tree[child] = parent

    for i in range(len(seller)):
        child = seller[i]
        parent = tree[child]
        money = amount[i] * 100
        sell[child] += money
        while True:
            commission = money // 10
            sell[child] -= commission
            sell[parent] += commission
            if commission < 10:
                break
            child = parent
            parent = tree[child]
            money = commission
            if parent == 'root':
                break
    ans = []
    for e in enroll:
        ans.append(sell[e])

    return ans

