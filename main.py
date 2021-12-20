# Main directory to call for functions

# Imports
# Global

# Local
from importCSV import *
from analysis import *
from generate_graphs import *

# Paths
pathdir2d = r".\Desktop\IR_data\2d_csv"

# Transform original directory with files in wrong position to correct files
# Uncomment if first time
# Correctdir(pathdir3d)

# Import files and analyse them
# norm_df = AnalysisAoA(pathdir3d)

# Analyse through images the transition line
list_2d = []
for file in os.listdir(pathdir2d):
    # Goes through each file
    path = pathdir2d + '\\' + file
    # Designs the transition line
    TransitionLine(path, list_2d)
# Arranges the points considering hysteresis
arr_2d = arrangeList(list_2d)
# Plots transition points
arr_2d_correct = correct_array_for_chord(arr_2d)
arr2CSV(arr_2d_correct, '2d')
get_graph(arr_2d_correct, '2D')