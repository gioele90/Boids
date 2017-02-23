from matplotlib import pyplot as plt
from matplotlib import animation
from boids_class import Boids
from argparse import ArgumentParser
import yaml
import numpy as np

def main():
	parser = ArgumentParser(description = "This program runs a simulation of a flock of birds flying")
	parser.add_argument('--config',help='Specify a configuration file with constants describing the flocking behaviour')
	if parser.parse_args().config==None:
		boids=Boids()
		boids.fly()
	else:
		config=yaml.load(open(parser.parse_args().config))
		globals().update(config)
		boids=Boids(boids_count,p_limits,v_limits,alert_distance,flocking_distance,flocking_strength,middle_strength,frames,interval,xlim,ylim)
		boids.fly()

if __name__ == "__main__":
    main()