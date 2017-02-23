BOIDS 1.0
==============

This software displays a set of points on a graph that move in imitation of a flock of birds. The "boids" (birds) adjust their
speeds in such a way to remain close to the middle of the flock, avoid other birds and match other birds speed.

INSTALLATION
------------

To install the program, move to the boids_project folder with the terminal or Command Prompt and run the code:

python setup.py install

On Mac/Linux root access might be required, in which case do

sudo python setup.py install

On Windows the Command Prompt should be opened with administrator privileges.

RUN THE PROGRAM
---------------

The appropriate invocation to run this program is:

python -m boids --config [CONFIG]

[CONFIG] is an optional parameter that specifies a configuration file containing all the parameters governing the flock behaviour
and the appearance of the graph. The config file should look as follows:

"boids_count: 50 #number of birds
p_limits: [-450.0, 300.0, 50.0, 600.0] #range of initial positions
v_limits: [0, -20.0, 10.0, 20.0] #range of initial speeds
alert_distance: 100 #collisions avoidance distance
flocking_distance: 10000 #maximum distance from the middle of the flock
flocking_strength: 0.125 #this parameter determines the accelleration of the birds when trying to match other birds speeds
middle_strength: 0.01 #this parameter determines the accelleration of the birds toward the centre of the flock
frames: 50 #total number of frames of the animation
interval: 50 #interval between frames (in milliseconds)
xlim: [-500,1000] #x axis limits
ylim: [-500,1000] #y axis limits"

If the argument [CONFIG] is not provided, i.e. if the code is executed with the command

python -m boids

default values are applied. A configuration file is provided in the Boids package (./boids/config.yaml)