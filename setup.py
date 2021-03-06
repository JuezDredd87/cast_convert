from setuptools import setup
from sys import version_info
from cast_convert import __version__


MIN_PYTHON_VERSION = (3, 5)
OLD_PYTHON_REQUIREMENTS = ['mypy-lang']

with open('requirements.txt', 'r') as file:
    requirements = [line.strip() for line in file]

if version_info < MIN_PYTHON_VERSION:
    requirements.extend(OLD_PYTHON_REQUIREMENTS)

setup(name="cast_convert",
      version=__version__,
      description="Convert and inspect video for Chromecast playback",
      url="https://github.com/thismachinechills/cast_convert",
      author="thismachinechills (Alex)",
      license="AGPL 3.0",
      packages=['cast_convert'],
      zip_safe=True,
      install_requires=requirements,
      keywords=requirements,
      entry_points={"console_scripts": ["cast_convert = cast_convert:command"]})
