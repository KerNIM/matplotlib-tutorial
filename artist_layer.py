from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas  # import FigureCanvas
from matplotlib.figure import Figure  # import Figure artist

fig = Figure()
canvas = FigureCanvas(fig)

import numpy as np

x = np.random.randn(10000)

ax = fig.add_subplot(111)  # create an axes artist

ax.hist(x, 100)  # gen histogram of the 10k numbers

ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
fig.savefig('matplotlib_histogram.png')