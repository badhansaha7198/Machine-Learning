# Data Distribution.

# import numpy
# import matplotlib.pyplot as plt
# x = numpy.random.uniform(0.0, 5.0, 25000)
# # print(x)
# plt.hist(x, 100)
# plt.show()

# Normal data distribution.
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()
