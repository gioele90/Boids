from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml
import numpy as np

config=yaml.load(open("config.yaml"))
globals().update(config)

class Boids(object):

	def __init__(self,boids_count=50,p_limits=[-450.0, 300.0, 50.0, 600.0]
,v_limits=[0, -20.0, 10.0, 20.0],alert_distance=100,flocking_distance=1000,flocking_strength=0.125,middle_strength=0.01):

		self.boids_count=boids_count
		self.alert_distance=alert_distance
		self.flocking_distance=flocking_distance
		self.flocking_strength=flocking_strength
		self.middle_strength=middle_strength
		self.positions=self.newflock(boids_count,np.array(p_limits[0:1])
,np.array(v_limits[1:3]))
		self.velocities=self.newflock(boids_count,np.array(v_limits[0:2]),np.array(v_limits[1:3]))

#Create new set of positions/velocities for the flock

	def newflock(self,boids_count,lower_limits,upper_limits):
		width=upper_limits-lower_limits
		return(lower_limits[:,np.newaxis]+np.random.rand(2,boids_count)*width[:,np.newaxis])

	def separations(self,positions):
		separations = positions[:,np.newaxis,:]-positions[:,:,np.newaxis]
		return(separations)

	def squared_distances(self,positions):
		separations=self.separations(positions)
		squared_displacements = separations*separations
		square_distances = np.sum(squared_displacements,0)
		return(square_distances)

#Fly towards middle

	def fly_to_middle(self,positions,velocities):
		middle = np.mean(positions,1)
		direction_to_middle=positions-middle[:,np.newaxis]
		velocities -= direction_to_middle*self.middle_strength

# Fly away from nearby boids
	def fly_away_from_boids(self,velocities,separations,square_distances):
		far_away = square_distances > self.alert_distance
		separations_if_close = np.copy(separations)
		separations_if_close[0,:,:][far_away] = 0
		separations_if_close[1,:,:][far_away] = 0
		velocities += np.sum(separations_if_close, 1)

# Try to match speed with nearby boids
	def match_velocities(self,velocities,velocity_separation,square_distances):
		very_far = square_distances > self.flocking_distance
		velocity_separation_if_close = np.copy(velocity_separation)
		velocity_separation_if_close[0,:,:][very_far] = 0
		velocity_separation_if_close[1,:,:][very_far] = 0
		velocities -= np.mean(velocity_separation_if_close, 1)*self.flocking_strength

	def update_boids(self,positions,velocities):
		separations=self.separations(positions)
		velocity_separation=self.separations(velocities)
		square_distances=self.squared_distances(positions)
		self.fly_to_middle(positions,velocities)
		self.fly_away_from_boids(velocities,separations,square_distances)
		self.match_velocities(velocities,velocity_separation,square_distances)

# Move according to velocities
		positions += velocities

boids=Boids(boids_count,p_limits,v_limits,alert_distance,flocking_distance,flocking_strength,middle_strength)
figure=plt.figure()
axes=plt.axes(xlim=(-1500,1000), ylim=(-1500,1000))
scatter=axes.scatter(boids.positions[0],boids.positions[1])

def animate(frame):
	boids.update_boids(boids.positions,boids.velocities)
	scatter.set_offsets(boids.positions.transpose())

anim = animation.FuncAnimation(figure,animate,frames=50,interval=50)
if __name__ == "__main__":
	plt.show()