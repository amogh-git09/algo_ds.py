import collections, itertools

def current_month_cost(d, c, h, m, month, lms, tms):
    required = d[month] + tms - lms
    regular_manufacture = max(min(required, m), 0)
    extra_manufacture = max(required - regular_manufacture, 0)
    return c*extra_manufacture + h(tms)

def plan(d, m, h, c):
    D = sum(d) # total demand
    stocks = [0]*len(d)
    costs = [0]*len(d)

    def rec(month, lms, cache={}):
        if month >= len(d):
            # after last month
            return 0

        if (month, lms) in cache:
            return cache[(month, lms)]

        # lms: last month stock
        # tms: this month stock
        min_cost = float('inf')
        tms = max(lms - d[month], 0)

        while True:
            cost = current_month_cost(d, c, h, m, month, lms, tms) + rec(month + 1, tms)
            if cost > min_cost:
                break
            else:
                min_cost = cost
                costs[month] = min_cost
                stocks[month] = tms
                tms += 1

        cache[(month, lms)] = min_cost
        return min_cost

    min_cost = rec(0, 0)
    print("costs", costs)
    return (min_cost, stocks)

def interpret_result(cs, d, c, h, m):
    requirements = [0]*(len(d))
    r = [0]*(len(d))
    x = [0]*(len(d))
    cost = [0]*(len(d))
    stocks = [0]*(len(d))
    lms = 0

    for month in range(len(d)):
        required = d[month] + cs[month][lms].stock - lms

        stocks[month] = cs[month][lms].stock
        requirements[month] = required
        r[month] = max(min(required, m), 0)
        x[month] = max(required - r[month], 0)
        cost[month] = c*x[month] + h(stocks[month])

        lms = cs[month][lms].stock

    print("  demand", ["{0:2d}".format(a) for a in d])
    print("   stock", ["{0:2d}".format(a) for a in stocks])
    print("required", ["{0:2d}".format(a) for a in requirements])
    print(" regular", ["{0:2d}".format(a) for a in r])
    print("   extra", ["{0:2d}".format(a) for a in x])
    print("    cost", ["{0:2d}".format(a) for a in cost])
    print("total cost =", sum(cost))


def plan2(d, m, h, c):
    D = sum(d)

    CostStock = collections.namedtuple('CostStock', ['cost', 'stock'])
    cost = [[CostStock(float('inf'), 0)]*(D+1) for i in range(len(d))]

    for month in range(len(d)-1, -1, -1):
        for lms in range(0, sum(d[month:])+1):
            for tms in range(max(lms - d[month], 0), sum(d[month+1:])+1):
                further_cost = cost[month+1][tms].cost if month < (len(d) - 1) else 0
                curr_cost = current_month_cost(d, c, h, m, month, lms, tms) + further_cost

                if curr_cost < cost[month][lms].cost:
                    cost[month][lms] = CostStock(curr_cost, tms)

    return cost
