import numpy as np
import matplotlib.pyplot as plt
from orbitdeterminator.util import (read_data, rkf78)
from orbitdeterminator.kep_determination import (lamberts_kalman)


data = read_data.load_data("orbit.csv")

data[:, 1:4] = data[:, 1:4] / 1000

state_vector = np.zeros((6, len(data)))
process_value = np.zeros((6, len(data)))

for i in range(0, 5):

	x1_new = [1, 1, 1]
	x1_new[:] = data[i, 1:4]
	x2_new = [1, 1, 1]
	x2_new[:] = data[i+1, 1:4]
	time = data[i+1, 0] - data[i, 0]

	print(x1_new)
	traj = lamberts_kalman.orbit_trajectory(x1_new, x2_new, time)

	v1 = lamberts_kalman.lamberts(data[i, :], data[i+1, :], traj)

	state_vector[0:3, i] = x1_new[:]
	state_vector[3:6, i] = v1[:]

	x = np.zeros((6,1))
	x[:, 0] = (state_vector[:, i])

	process_value[:, i+1] = np.ravel(rkf78.rkf78(6, 0, time, time/20.0, 1e-08, x))

print(process_value[0,0:5])



##Ayth h orbit mallon einai xwris 80rybo


