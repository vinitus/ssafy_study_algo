def solution(cap, n, deliveries, pickups):
    cnt = 0
    now = [cap,0]
    deliveries.insert(0,0)
    pickups.insert(0,0)
    total = sum(deliveries) + sum(pickups)
    idx = 0
    direction = 0
    while total != 0:
        if not direction:
            while deliveries[idx] and now[0]:
                deliveries[idx] -= 1
                total -= 1
                now[0] -= 1
            else:
                if now[0] <= 0:
                    direction = 1
                else:
                    idx += 1
                    cnt += 1
        else:
            while pickups[idx] and now[1] < cnt:
                pickups[idx] -= 1
                total -= 1
                now[1] += 1
            else:
                if now[1] >= cap:
                    direction = 0
                elif idx:
                    idx -= 1
                    cnt += 1
                else:
                    now = [0,0]
                    direction = 0

    return cnt

solution(4,5,[1,0,3,1,2],[0,3,0,4,0])