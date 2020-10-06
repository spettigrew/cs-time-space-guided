
# why do we have big O notation?
# To evaluate performance.
# to find out the time it takes to complete a function (releative to other input sizes) 
# different computers run at different speeds
# efficiency

# O(n) --> linear time. Algo increases the number of operations it performs as long as it performs as long a log-linear function of the input size n
# O(n^2) -- quadratic. Squared - Also increases the number of operations it performs quad function of the input size n
# O(1) -- constant -- the performance doesn't change regardless of input. Best Runtime. Any input size, it performs the same number of operations.
# O(log n) -- logarithmic -- every time we double the input size, we only add one extra step. Number of operation performs as log function of the input size n. Binary search.
# O(2^n) -- exponential. Worst Runtime. Number of operations it performs as input size increases is limited.
# factorial
# O(n log n) -- linearithmic


# Classification	    Description
# Constant O(1)	The runtime is entirely unaffected by the input size. This is the ideal solution.
# Logarithmic O(log n)	As the input size increases, the runtime will grow slightly slower. This is a pretty good solution.
# Linear O(n)	As the input size increases, the runtime will grow at the same rate. This is a pretty good solution.
# Polynomial O(n^c)	As the input size increases, the runtime will grow at a faster rate. This might work for small inputs but is not a scalable solution.
# Exponential O(c^n)	As the input size increases, the runtime will grow at a much faster rate. This solution is inefficient.
# Factorial O(n!)	As the input size increases, the runtime will grow astronomically, even with relatively small inputs. This solution is exceptionally inefficient.