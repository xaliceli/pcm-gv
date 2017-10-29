from scatter import scatter_df as scatter_df
from data import plt as plt
import numpy as np
from matplotlib import animation

# Initialize plot objects
fig = plt.figure()
scat = plt.scatter([], [])
nframes = 100

# Set axes
xmin = scatter_df.min()['x_coordinate']
ymin = scatter_df.min()['y_coordinate']
xmax = scatter_df.max()['x_coordinate']
ymax = scatter_df.max()['y_coordinate']
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)


def animate(i, data, scat):
    """Animation function for scatterplot"""
    while i <= len(data):
        x = data.iloc[:i]['x_coordinate']
        y = data.iloc[:i]['y_coordinate']
        scat_data = np.hstack((x[:i, np.newaxis], y[:i, np.newaxis]))
        scat.set_offsets(scat_data)
        return scat,


# Run animation and save as mp4
scatter_anim = animation.FuncAnimation(fig, animate,
                                       frames=range(nframes),
                                       fargs=(scatter_df, scat))
scatter_anim.save('scatter_animated.mp4')
