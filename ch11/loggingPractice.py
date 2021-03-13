import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
#logging.disable(logging.CRITICAL)

logging.debug("Start")

def factorial(n):
    logging.debug(f"Start of factorial {n}")
    total = 1
    for i in range (1, n + 1):
        total *= i
        logging.debug(f"i is {i}, total is {total}")
    logging.debug(f"return value is {total}")
    return total

print(factorial(5))

logging.debug("Finish")