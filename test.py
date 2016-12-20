a = 1

b = a * 4
b

c = (a+b)**b
c

import matplotlib.pyplot as plt
from random import randint
#import seaborn as sns
plt.plot(range(1000),[randint(0,1000) for i in range(1000)])
plt.show()
