from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Boids
import yaml
import numpy as np

config=yaml.load(open("config.yaml"))
globals().update(config)

boids=Boids(boids_count,p_limits,v_limits,alert_distance,flocking_distance,flocking_strength,middle_strength)
figure=plt.figure()
axes=plt.axes(xlim=(-1500,1000), ylim=(-1500,1000))
scatter=axes.scatter(boids.positions[0],boids.positions[1])

def animate(frame):
	boids.update_boids()
	scatter.set_offsets(boids.positions.transpose())

anim = animation.FuncAnimation(figure,animate,frames=50,interval=50)
if __name__ == "__main__":
	plt.show()