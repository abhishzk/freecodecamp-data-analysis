from unittest import main
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Draw the categorical plot
draw_cat_plot()

# Draw the heatmap
draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)