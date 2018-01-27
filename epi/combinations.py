def combinations(target, plays):
    def rec(target, plays, p, r, cache={}):
        if p == r:
            return 1 if target % plays[p] == 0 else 0

        if (target, p, r) in cache:
            return cache[(target, p, r)]

        solutions = 0
        for i in range((target // plays[p]) + 1):
            solutions += rec(target - plays[p]*i, plays, p+1, r)

        cache[(target, p, r)] = solutions
        return solutions

    return rec(target, plays, 0, len(plays)-1)

def combinations2(target, plays):
    """
    No cache.
    """
    def rec(target, plays, p, r):
        if p == r:
            return 1 if target % plays[p] == 0 else 0

        solutions = 0
        for i in range((target // plays[p]) + 1):
            solutions += rec(target - plays[p]*i, plays, p+1, r)

        return solutions

    return rec(target, plays, 0, len(plays)-1)

def combinations3(target, play_scores):
    """
    Bottom up approach. O(len(play_scores)*target) space.
    """
    num_of_comb = [[1] + [0]*target for _ in play_scores]
    for i in range(len(play_scores)):
        for j in range(1, target+1):
            without_this_play = num_of_comb[i - 1][j] if i >= 1 else 0
            with_this_play = num_of_comb[i][j - play_scores[i]] if j >= play_scores[i] else 0
            num_of_comb[i][j] = without_this_play + with_this_play
    return num_of_comb[-1][-1]

def combinations4(target, play_scores):
    """
    Bottom up approach. O(taget) space.
    """
    def new_row():
        return [1] + [0]*target

    row1, row2 = new_row(), new_row()
    for i in range(len(play_scores)):
        for j in range(1, target+1):
            without_this_play = row1[j] if i >= 1 else 0
            with_this_play = row2[j - play_scores[i]] if j >= play_scores[i] else 0
            row2[j] = without_this_play + with_this_play

        row1 = row2
        row2 = new_row()
    return row1[-1]

def permutations(target, play_scores):
    num_of_perm = [1] + [0]*target
    for i in range(1, target+1):
        for play_score in play_scores:
            num_of_perm[i] += num_of_perm[i - play_score] if i >= play_score else 0
    return num_of_perm[-1]

def permutations_2_teams(target1, target2, play_scores):
    num_of_perm = [[0]*(target2+1) for _ in range(target1+1)]
    num_of_perm[0][0] = 1
    for i in range(target1 + 1):
        for j in range(target2 + 1):
            if not (i == 0 and j == 0):
                for play_score in play_scores:
                    num_of_perm[i][j] += num_of_perm[i - play_score][j] if i >= play_score else 0
                    num_of_perm[i][j] += num_of_perm[i][j - play_score] if j >= play_score else 0
    return num_of_perm[-1][-1]
