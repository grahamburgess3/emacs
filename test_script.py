# imports
import ranking_and_selection as rs
import queueing_model as qm
import math
import numpy as np
import json

# Opening JSON files
with open('data_as_is.json') as json_file:
    data_as_is = json.load(json_file)
with open('data_as_is_analytical.json') as json_file:
    data_as_is_analytical = json.load(json_file)

# setup
sol = [{'housing': [12, 12, 12, 12], 'shelter': [12, 12, 12, 12]}]
service_times = [2,3,4]
yrs = 3

# model
out = []
for i in range(len(service_times)):
    spc = rs.SolutionSpace(sol)
    spc.model_analytically(data_as_is, data_as_is_analytical, yrs, float(service_times[i]))
    out.append(spc.true_outputs_unsh[0])
    print('done ' + str(i))

print(out)
