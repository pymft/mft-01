import math
import time

t1 = time.time()
c = math.factorial(10000)
t2 = time.time()
print(c)
t3 = time.time()
diff_calc = t2 - t1
diff_print = t3 - t2
print(f"elapsed time [calculation]= {diff_calc}")
print(f"elapsed time [print      ]= {diff_print}")

