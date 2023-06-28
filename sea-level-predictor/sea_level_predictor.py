import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def plot_sea_level(data_file):
    # Read the data from the CSV file
    data = pd.read_csv(data_file)

    # Scatter plot of Year vs. CSIRO Adjusted Sea Level
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Actual Data')

    # Perform linear regression
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050
    years = range(1880, 2051)
    sea_level = [slope * year + intercept for year in years]
    plt.plot(years, sea_level, color='red', label='Best Fit Line')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save and show the plot
    plt.savefig('sea_level_plot.png')
    plt.show()

def plot_sea_level_since_2000(data_file):
    # Read the data from the CSV file
    data = pd.read_csv(data_file)

    # Filter data from year 2000 onwards
    data_since_2000 = data[data['Year'] >= 2000]

    # Scatter plot of Year vs. CSIRO Adjusted Sea Level (since 2000)
    plt.scatter(data_since_2000['Year'], data_since_2000['CSIRO Adjusted Sea Level'], label='Actual Data')

    # Perform linear regression (since 2000)
    slope, intercept, _, _, _ = linregress(data_since_2000['Year'], data_since_2000['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 (since 2000)
    years = range(2000, 2051)
    sea_level = [slope * year + intercept for year in years]
    plt.plot(years, sea_level, color='red', label='Best Fit Line')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save and show the plot
    plt.savefig('sea_level_since_2000_plot.png')
    plt.show()
