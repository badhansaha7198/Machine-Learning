import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
w = numpy.mean(speed)
x = numpy.std(speed)
y = numpy.median(speed)
z = stats.mode(speed)
a = numpy.percentile(speed, 80)
print(w)
print(x)
print(y)
print(z)
print(a)