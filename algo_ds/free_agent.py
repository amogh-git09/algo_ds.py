import collections

def maximize_vorp(X, fee, vorp):
    N = len(fee)
    P = len(fee[0])

    def rec(budget, pos, cache={}):
        # print(budget, pos)
        if pos >= N:
            return 0

        if (budget, pos) in cache:
            return cache[(budget, pos)]

        max_vorp = 0
        for player in range(0, P):
            with_player = vorp[pos][player] + rec(budget - fee[pos][player], pos + 1) if budget >= fee[pos][player] else 0
            without_player = rec(budget, pos + 1)

            if max(with_player, without_player) > max_vorp:
                max_vorp = max(with_player, without_player)

        cache[(budget, pos)] = max_vorp
        return max_vorp

    return rec(X, 0)

def maximize_vorp2(X, fee, vorp):
    N = len(fee)
    P = len(fee[0])

    VorpPlayer = collections.namedtuple('VorpPlayer', ['vorp', 'player'])
    c = [[VorpPlayer(0, None)]*(X+1) for _ in range(N)]

    for pos in range(N-1, -1, -1):
        for budget in range(X, -1, -1):
            for player in range(0, P):
                if budget < fee[pos][player]:
                    continue

                bottom = c[pos + 1][budget - fee[pos][player]].vorp if pos < N-1 else 0
                with_player = vorp[pos][player] + bottom

                if with_player > c[pos][budget].vorp:
                    c[pos][budget] = VorpPlayer(with_player, player)

            without_player = c[pos + 1][budget].vorp if pos < N-1 else 0
            if without_player > c[pos][budget].vorp:
                c[pos][budget] = VorpPlayer(without_player, None)

    return c

def print_players(c, fee, vorp, X):
    N = len(fee)
    P = len(fee[0])
    charge = [0]*N
    vorps = [0]*N

    budget = X
    for pos in range(0, N):
        player = c[pos][budget].player
        charge[pos] = fee[pos][player] if player != None else 0
        vorps[pos] = vorp[pos][player] if player != None else 0
        print("Position: {0:2d}, Player: {1:2d}, Fee: {2:2d}, VORP: {3:2d}".format(pos, player if player != None else -1, charge[pos], vorps[pos]))
        budget -= charge[pos]

    print("Total Budget: {}, Exhausted: {}, Total VORP: {}".format(X, sum(charge), sum(vorps)))
