def kWeakestRows(mat: [[int]], k: int) -> [int]:
    Soldiers, Values, Weakest = [], [], []
    SetValues = set()
    for row in mat:
        power = row.count(1)
        Soldiers.append(power)
        SetValues.add(power)

    while SetValues:
        Values.append(SetValues.pop())
    Values.sort(reverse=True)

    while Values and k > 0:
        weakest = Values.pop()
        for i, power in enumerate((Soldiers)):
            if power == weakest:
                Weakest.append(i)
    print(Weakest[0:k])
    return Weakest[0:k]


inp = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]

kWeakestRows(inp, 3)
