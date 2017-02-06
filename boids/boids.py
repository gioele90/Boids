from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml

config=yaml.load(open("config.yaml"))
globals().update(config)

boids_x=[random.uniform(xmin,xmax) for x in range(boids_count)]
boids_y=[random.uniform(ymin,ymax) for x in range(boids_count)]
boid_x_velocities=[random.uniform(vxmin,vxmax) for x in range(boids_count)]
boid_y_velocities=[random.uniform(vymin,vymax) for x in range(boids_count)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	xs,ys,xvs,yvs=boids
# Fly towards the middle
	for i in range(boids_count):
		for j in range(boids_count):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*middle_strength/len(xs)
			yvs[i]=yvs[i]+(ys[j]-ys[i])*middle_strength/len(xs)

# Fly away from nearby boids

	for i in range(boids_count):
		for j in range(boids_count):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < alert_distance:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])

# Try to match speed with nearby boids
	for i in range(boids_count):
		for j in range(boids_count):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < flocking_distance:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*flocking_strength/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*flocking_strength/len(xs)

# Move according to velocities
	for i in range(boids_count):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
	update_boids(boids)
	scatter.set_offsets(list(zip(boids_x,boids_y)))

anim = animation.FuncAnimation(figure,animate,frames=50,interval=50)
if __name__ == "__main__":
	plt.show()