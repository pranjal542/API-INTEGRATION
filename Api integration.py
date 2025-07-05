import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API endpoint for COVID-19 data
URL = "https://corona.lmao.ninja/v3/covid-19/countries"

# Fetch the data
response = requests.get(URL)


if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to retrieve data: {response.status_code}")
    data = []


country_data = []
for country in data:
    country_data.append({
        "Country": country["country"],
        "Cases": country["cases"],
        "Deaths": country["deaths"],
        "Recovered": country["recovered"]
    })


df = pd.DataFrame(country_data)


df = df.sort_values(by="Cases", ascending=False).head(10)  # Top 10 countries by cases


print(df)


sns.set(style="whitegrid")


fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot Cases
sns.barplot(x='Cases', y='Country', data=df, ax=axes[0], palette="Blues_d")
axes[0].set_title('Top 10 Countries by Total Cases')
axes[0].set_xlabel('Total Cases')

# Plot Deaths
sns.barplot(x='Deaths', y='Country', data=df, ax=axes[1], palette="Reds_d")
axes[1].set_title('Top 10 Countries by Total Deaths')
axes[1].set_xlabel('Total Deaths')

# Plot Recovered
sns.barplot(x='Recovered', y='Country', data=df, ax=axes[2], palette="Greens_d")
axes[2].set_title('Top 10 Countries by Total Recovered')
axes[2].set_xlabel('Total Recovered')


plt.tight_layout()
plt.show()


