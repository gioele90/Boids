import os
import yaml
from nose.tools import assert_equal
from ..boids import Boids
import numpy as np
from numpy import testing as npTest

def test_update_boids():
	fixture=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fix_boids_update.yml')))
	p_before=fixture["positions_before"]
	p_after=fixture["positions_after"]
	v_before=fixture["velocities_before"]
	v_after =fixture["velocities_after"]
	boids = Boids()
	boids.positions=np.array(p_before)
	boids.velocities=np.array(v_before)
	boids.update_boids()
	npTest.assert_array_almost_equal(boids.positions, np.array(p_after))
	npTest.assert_array_almost_equal(boids.velocities, np.array(v_after))

def test_separations():
	fixture=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fix_separations.yml')))
	positions=np.array(fixture["positions"])
	separations=fixture["separations"]
	boids=Boids()
	npTest.assert_array_equal(np.array(separations),boids.separations(positions))

def test_squared_distances():
	fixture=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fix_squared_distances.yml')))
	positions=np.array(fixture["positions"])
	squared_distances=np.array(fixture["squared_distances"])
	boids=Boids()
	npTest.assert_array_equal(squared_distances,boids.squared_distances(positions))

def test_fly_to_middle():
	fixture=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fix_fly_to_middle.yml')))
	velocities_after=np.array(fixture["velocities_after"])
	boids=Boids()
	boids.positions=np.array(fixture["positions"])
	boids.velocities=np.array(fixture["velocities_before"])
	boids.fly_to_middle()
	npTest.assert_array_almost_equal(boids.velocities,velocities_after)

def test_fly_away_from_boids():
	fixture=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fix_fly_away_from_boids.yml')))
	velocities_after=np.array(fixture["velocities_after"])
	boids=Boids()
	boids.positions=np.array(fixture["positions"])
	boids.velocities=np.array(fixture["velocities_before"])
	separations=boids.separations(boids.positions)
	squared_distances=boids.squared_distances(boids.positions)
	boids.fly_away_from_boids(separations,squared_distances)
	npTest.assert_array_almost_equal(boids.velocities,velocities_after)

def test_match_velocities():
	fixture=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fix_match_velocities.yml')))
	velocities_after=np.array(fixture["velocities_after"])
	boids=Boids()
	boids.positions=np.array(fixture["positions"])
	boids.velocities=np.array(fixture["velocities_before"])
	separations=boids.separations(boids.positions)
	velocity_separation=boids.separations(boids.velocities)
	squared_distances=boids.squared_distances(boids.positions)
	boids.match_velocities(velocity_separation,squared_distances)
	npTest.assert_array_almost_equal(boids.velocities,velocities_after)



	