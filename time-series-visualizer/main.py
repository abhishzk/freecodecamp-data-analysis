import time_series_visualizer

# Path to the data file
data_file = 'fcc-forum-pageviews.csv'

# Generate and save the line plot
time_series_visualizer.draw_line_plot(data_file)

# Generate and save the bar plot
time_series_visualizer.draw_bar_plot(data_file)

# Generate and save the box plots
time_series_visualizer.draw_box_plot(data_file)
