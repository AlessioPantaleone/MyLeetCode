def fizzBuzz(n: int) -> [str]:
    solution = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            solution.append("FizzBuzz")
        elif (i % 3 == 0):
            solution.append("Fizz")
        elif (i % 5 == 0):
            solution.append("Buzz")
        else:
            solution.append(str(i))
    print(solution)
    return solution


fizzBuzz(15)

