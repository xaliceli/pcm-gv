import pandas as pd
from sodapy import Socrata
import matplotlib
import matplotlib.pyplot as plt

# Use ggplot chart styles
matplotlib.style.use('ggplot')

# Client with app token
client = Socrata("data.cityofchicago.org",
                 "NK7rjpziuElwqAceliB68O4X3")

# Results returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("6zsd-86xi", limit=2000)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

# Filter by incident description
filter = "GUN"
incident_df = df[df['description'].str.contains(filter)]

# Basic incidents by date plot
plt.figure(figsize=(12, 9))

# This produces gibberish but pretty cool looking gibberish
# plt.plot(incident_df.date.values,
#         incident_df.id.values)

incident_df['date'] =  pd.to_datetime(incident_df['date'])

print(incident_df.info)

incident_df['year'].value_counts().plot()

plt.savefig("test.png", bbox_inches="tight")
