import sea_level_predictor

# Path to the data file
data_file = 'epa-sea-level.csv'

# Generate and save the first plot
sea_level_predictor.plot_sea_level(data_file)

# Generate and save the second plot
sea_level_predictor.plot_sea_level_since_2000(data_file)
