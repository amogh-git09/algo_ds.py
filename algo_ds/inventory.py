def plan(d, m, h, c):
    n = len(d)
    r = [0]*n    # regular manufactures
    x = [0]*n    # extra manufactures
    s = [0]*n    # stock at the end of month
    cost = [0]*n # cost incurred in month

    sol_r = [0]*n    # optimal regular manufactures
    sol_x = [0]*n    # optimal extra manufactures
    sol_s = [0]*n    # optimal stock at the end of month
    sol_cost = [0]*n # optimal cost incurred in month

    def rec(i):
        r[i] = min(d[i] - s[i-1], m)
        x[i] = max(d[i] - (s[i-1] + r[i]), 0)
        print(r[i], x[i], s[i-1], d[i])
        s[i] = min(s[i-1] + r[i] + x[i] - d[i], 0) if i > 0 else 0
        cost[i] = c * x[i] + h(s[i])
        min_cost = float('inf')

        while True:
            if i < n-1:
                rec(i+1)

            total_cost = sum(cost)
            # print(i, total_cost, min_cost)
            if total_cost >= min_cost:
                break

            min_cost = total_cost
            sol_r[i] = r[i]
            sol_x[i] = x[i]
            sol_s[i] = s[i]
            sol_cost[i] = cost[i]

            if r[i] < m:
                r[i] += 1
            else:
                x[i] += 1

            s[i] += 1
            cost[i] = c*x[i] + h(s[i])
            # print("cost[i]", cost[i])

    rec(0)
    return (sol_r, sol_x, sol_s, sol_cost)
