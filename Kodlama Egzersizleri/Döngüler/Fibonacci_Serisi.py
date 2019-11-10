"""fibonacci serisi 1,1,2,3,5,8,13,21,.......
kendinden önceki iki sayının toplamıdır."""

a=1
b=1

fibonacci=[a,b]

for i in range(5):
    print("a:",a,"b:",b)
    a,b = b,a+b
    fibonacci.append(b)
    print("a:", a, "b:", b)
print(fibonacci)