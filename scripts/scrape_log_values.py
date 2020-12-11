# open log file
filename = "logs/deeplift.log"
f = open(filename, "rt")

# define the values we're looking for
roc_auc_list = []
precision_list = []
loss_list = []
roc_auc_string = "validation roc_auc: "
precision_string = "validation average_precision: "
loss_string = "validation loss: "

# get the value from the line if this line contains it
def get_val(line, matching_str, val_list):
    if matching_str in line: 
        # find the location of the end of the marker
        start_loc = line.find(matching_str)
        end_loc = start_loc + len(matching_str)
        sub_str = line[end_loc: end_loc+5]
        val_list.append(float(sub_str))

# read values 
for line in f:
    get_val(line, roc_auc_string, roc_auc_list)
    get_val(line, precision_string, precision_list)
    get_val(line, loss_string, loss_list)

# print values
print("ROC AUC:", roc_auc_list)
print("PRECISION:", precision_list)
print("LOSS:", loss_list)