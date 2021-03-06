from operator import itemgetter

PizzaNumber, T2, T3, T4 = map(int, input().split())
Pizzas = {}
for i in range(PizzaNumber):
    P = input().split()
    P[0] = int(P[0])
    P.insert(0, i)
    Pizzas[i] = P

Pizzas = sorted(Pizzas.values(), key=itemgetter(1), reverse=True)
TeamNumber = 0
distributedPizzas = []
teamsNumber = T4+T3+T2


for i in range(teamsNumber):
    if len(Pizzas) < 2:
        break

    p = Pizzas.pop(0)
    teamPizzas = [p[0]]
    teamPizzaIngredients = [i for i in p[2:]]
    while True:
        if (len(teamPizzas) == 3 and T4 == 0) or \
                (len(teamPizzas) == 2 and T3 == 0 and len(teamPizzas) == 2 and T4 == 0) or \
                (len(Pizzas) == 0) or len(teamPizzas) == 4:
            break

        nextPizzaId = 0
        nextPizzaWasted = 10000000000
        nextPizzaNew = 0
        for k, v in enumerate(Pizzas):
            if len(v) < nextPizzaNew+2:
                continue
            curWaste = 0
            curNew = 0
            newIngredients = []
            for n in v[2:]:
                if n not in teamPizzaIngredients:
                    curNew += 1
                else:
                    curWaste += 1
            if curNew >= nextPizzaNew and curNew - curWaste > nextPizzaNew - nextPizzaWasted and curWaste < nextPizzaWasted:
                nextPizzaNew = curNew
                nextPizzaWasted = curWaste
                nextPizzaId = k
                newIngredients = v[2:]
        teamPizzaIngredients = list(set(teamPizzaIngredients+newIngredients))
        teamPizzas.append(Pizzas[nextPizzaId][0])
        Pizzas.pop(nextPizzaId)


    if len(teamPizzas) == 4:
        T4 -= 1
    elif len(teamPizzas) == 3:
        T3 -= 1
    elif len(teamPizzas) == 2:
        T2 -= 1

    teamPizzas.insert(0, len(teamPizzas))
    distributedPizzas.append(teamPizzas)

print(len(distributedPizzas))
for i in distributedPizzas:
    print(*i)