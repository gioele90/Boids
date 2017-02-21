from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Boids
import yaml
import numpy as np

config=yaml.load(open("config.yaml"))
globals().update(config)

if __name__ == "__main__":
	boids=Boids(boids_count,p_limits,v_limits,alert_distance,flocking_distance,flocking_strength,middle_strength,frames,interval,xlim,ylim)
	boids.fly()