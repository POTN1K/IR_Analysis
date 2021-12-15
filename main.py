# Main directory to call for functions

# Imports
# Global

# Local
from importCSV import *
from analysis import *
from generate_graphs import *

# Paths
pathdir3d = r"C:\Users\ricke\Desktop\IR_data\3d_csv"

# Transform original directory with files in wrong position to correct files
# Uncomment if first time
# Correctdir(pathdir3d)

# Import files and analyse them
norm_df = AnalysisAoA(pathdir3d)

# Analyse through images the transition line
list_3d = []
for file in os.listdir(pathdir3d):
    # Goes through each file
    path = pathdir3d + '\\' + file
    # Designs the transition line
    TransitionLine(path, list_3d)
# Arranges the points considering hysteresis
arr_3d = arrangeList(list_3d)
# Plots transition points
arr_3d_correct = correct_array_for_chord(arr_3d)
arr2CSV(arr_3d_correct, '3d')
get_graph(arr_3d_correct, '3D')
