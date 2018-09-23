from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator, FormatStrFormatter)

plt.figure()
ax=plt.subplot(111)
ax.set_ylim(-200,100)
ax.set_xlim(-9,0)

majorLocator_x=MultipleLocator(3)
majorLocator_y=MultipleLocator(100)
minor_locator_x = AutoMinorLocator(4)
minor_locator_y = AutoMinorLocator(4)
ax.yaxis.set_minor_locator(minor_locator_y)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.xaxis.set_major_locator(majorLocator_x)
ax.yaxis.set_major_locator(majorLocator_y)
#ax.set_yticks([100,0,-100,200])
#ax.set_xticks([0,-3,-6,-9])
plt.show()

