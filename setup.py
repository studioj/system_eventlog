from os import path
from platform import python_version

from setuptools import setup

from system_eventlog import __version__

version = __version__
long_description = ""
test_requirements = []

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()
with open("test_requirements.txt") as f:
    test_requirements = f.read().splitlines()
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="system_eventlog",
    version=version,
    description="helper library which reads the system event log and presents that log as a list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jef Neefs",
    author_email="neefsj@gmail.com",
    url="https://github.com/studioj/system_event_log",
    packages=["system_eventlog"],
    tests_require=test_requirements,
    install_require=requirements,
    license="GPL",
    platforms="Posix; MacOS X; Windows",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
