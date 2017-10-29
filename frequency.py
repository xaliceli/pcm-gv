from data import df as df
from data import plt as plt

# Frequency plot by date
df['date'].value_counts().plot()
plt.savefig("frequency.png", bbox_inches="tight")

# This produces gibberish but pretty cool looking gibberish
# plt.plot(incident_df.date.values,
#         incident_df.id.values)
