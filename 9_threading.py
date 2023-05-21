import threading
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def calculate_sum(n):
    fib_sum = 0
    for i in range(n):
        fib_sum += fibonacci(i)
    return fib_sum


def run_in_thread(n):
    start_time = time.time()
    result = calculate_sum(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Sum for n =", n, "is:", result)
    print("Execution time:", execution_time, "seconds")


# Создаем два потока
thread1 = threading.Thread(target=run_in_thread, args=(35,))
thread2 = threading.Thread(target=run_in_thread, args=(37,))

# Запускаем потоки
thread1.start()
thread2.start()

# Ожидаем завершения потоков
thread1.join()
thread2.join()

print("Both threads have finished execution.")

# # Run w/o threading (it is faster then above)
# run_in_thread(35)
# run_in_thread(37)

# print("Finished execution.")
