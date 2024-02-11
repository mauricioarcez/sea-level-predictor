import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

  # Create first line of best fit
  res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
  future_years = range(1880 , 2051)
  first = res.slope * future_years + res.intercept

  plt.plot(future_years, first, color='red')

  # Create second line of best fit
  years = range(2000,2051)
  df_filtered = df.loc[df['Year'] >= 2000, :]
  res2 = linregress(x=df_filtered['Year'], y=df_filtered['CSIRO Adjusted Sea Level'])
  second = res2.slope * years + res2.intercept
  plt.plot(years, second, color='red', linestyle='--',)

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()