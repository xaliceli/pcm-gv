from data import df as df
from data import plt as plt

# Scatterplot by coordinates
scatter_df = df[['x_coordinate', 'y_coordinate']].copy()
scatter_df = scatter_df.dropna(how='any')
scatter_df = scatter_df.astype(int)
scatter_df.plot.scatter(x='x_coordinate', y="y_coordinate")
plt.savefig("scatterplot.png", bbox_inches="tight")
