from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml
import numpy as np

config=yaml.load(open("config.yaml"))
globals().update(config)

lower_limits=np.array(p_limits[0:1])
upper_limits=np.array(p_limits[2:3])
width=upper_limits-lower_limits

lower_v_limits=np.array(v_limits[0:2])
upper_v_limits=np.array(v_limits[1:3])
widthv=upper_v_limits-lower_v_limits

positions=lower_limits[:,np.newaxis]+np.random.rand(2,boids_count)*width[:,np.newaxis]
velocities=lower_v_limits[:,np.newaxis]+np.random.rand(2,boids_count)*widthv[:,np.newaxis]

def update_boids(positions,velocities):
	positions = positions
	velocities = velocities

# Fly towards the middle
	middle = np.mean(positions,1)
	direction_to_middle=positions-middle[:,np.newaxis]
	velocities -= direction_to_middle*middle_strength
	
# Fly away from nearby boids
	separations = positions[:,np.newaxis,:]-positions[:,:,np.newaxis]
	squared_displacements = separations*separations
	square_distances = np.sum(squared_displacements,0)
	far_away = square_distances > alert_distance
	separations_if_close = np.copy(separations)
	separations_if_close[0,:,:][far_away] = 0
	separations_if_close[1,:,:][far_away] = 0
	velocities += np.sum(separations_if_close, 1)
	
# Try to match speed with nearby boids
	very_far = square_distances > flocking_distance
	velocity_separation = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
	velocity_separation_if_close = np.copy(velocity_separation)
	velocity_separation_if_close[0,:,:][very_far] = 0
	velocity_separation_if_close[1,:,:][very_far] = 0
	velocities -= np.mean(velocity_separation_if_close, 1) * flocking_strength


# Move according to velocities
	positions += velocities

figure=plt.figure()
axes=plt.axes(xlim=(-1500,1500), ylim=(-1500,1500))
scatter=axes.scatter(positions[0],positions[1])

def animate(frame):
	update_boids(positions,velocities)
	scatter.set_offsets(positions.transpose())

anim = animation.FuncAnimation(figure,animate,frames=50,interval=50)
if __name__ == "__main__":
	plt.show()