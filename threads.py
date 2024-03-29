import time


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user, {time.time() - start}")


def complex_calculation():
    start = time.time()
    print("Started calculating...")
    [x**2 for x in range(200000)]
    print(f"complex calculation, {time.time() - start}")


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')