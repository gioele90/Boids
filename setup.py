from setuptools import setup, find_packages
with open("README.txt", "rb") as f:
	long_descr = f.read().decode("utf-8")
setup(
	name="boids",
	packages=find_packages("boids",exclude=["test"]),
	scripts = ['scripts/boids'],
	version="1.1",
	description="Run a simulation of birds flying",
	long_description=long_descr,
	author="Gioele Consani",
	install_requires=['argparse','numpy','matplotlib','pyyaml'],
	include_package_data=True
	)