import time

def calcProd():
    product = 1
    for i in range(1, 10000):
        product *= i
    return product

def calcProdPrint():
    product = 1
    for i in range(1, 10000):
        product *= i
        print(product)
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

startTimePrint = time.time()
prodPrint = calcProdPrint()
endTimePrint = time.time()


print(f"The result is {len(str(prod))} digits long")
print(f"Task completed in {endTime - startTime} seconds")

print(f"The result is {len(str(prodPrint))} digits long")
print(f"Task completed in {endTimePrint - startTimePrint} seconds")