import requests
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

# Use ggplot chart styles
matplotlib.style.use('ggplot')

# Get API data
parameters = {"$$app_token": "NK7rjpziuElwqAceliB68O4X3",
              "$limit": 50000}
results = requests.get("https://data.cityofchicago.org/resource/6zsd-86xi.json",
                       params=parameters)
results = results.json()

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

# Filter by incident description and date
filter = "GUN"
df = df[df['description'].str.contains(filter)]
df = df[df['year'] == "2017"]

# Set figure size
plt.figure(figsize=(12, 9))

# Make sure date variable is in correct format
df.loc[:, 'date'] = pd.to_datetime(df['date'])
