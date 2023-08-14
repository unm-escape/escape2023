![unm-escape header](header2.png)
#

## About
ESCAPE 2023 is a 2-week program designed to introduce participants to scientific
computing, Earth science and spatial data analysis in a fun, inclusive, collaborative environment.

[Lecture slides (OneDrive, read-only link)](https://unmm-my.sharepoint.com/:f:/g/personal/eol_unm_edu/Eow7Z0HhfThKmkPtX8kHF6YBR3QvPLdyrt0OpUqBqr27kg?e=SNnBEZ)

## Schedule

### Week 1

#### Day 1 (Aug 7): Introduction to programming
  * 9:30 – 11: Introduction to the course and icebreaker
  * 11:15 – 12: Lecture: **Intro to programming (Eric)**
  * 12 – 1: Lunch – Sahara
  * 1 – 2: Jupyter and python installation and demo
  * 2 – 4: Self-guided exercises: intro to Python notebook

#### Day 2 (Aug 8): Interacting with data
  * 9:30 – 11: Lecture / demo: **Reading data in python and making a plot (Eric)**
  * 11 - 12: Finish up assignments from yesterday
  * 12 – 1: Lunch - Dion's
  * 1 – 4: Self-guided exercises: reading data and making nice plots

#### Day 3 (Aug 9): Answering questions in plate tectonics
  * 9:30 – 11: Lecture: **Questions in Plate tectonics (Mousumi)**
  * 12 – 1: Lunch
  * 1 – 4: Self-guided exercises: Reading data from a file, comparison to a 2d plate cooling model

#### Day 4 (Aug 10): Seismology
  * 9:30 – 10:30: **What is seismology? (Brandon)**
  * 11 – 12: Discussion and exercises: **Date time in python (Andrew)**
  * 12 - 1: Lunch
  * 1 – 3 ObsPy demo & exercises
  * 3 – 4: Lecture: **Prep for active seismic survey (Lindsay)**

#### Day 5 (Aug 11): Field day
  * **8:30** – 12: Seismic survey at Alameda open space - meet at the loading dock. We will leave at 8:30!
  * Lunch –  in the field or after retrun
  * 1:30 – 2: Finish Obspy exercises
  * 2-3: Lecture: **Seismic reflection data and exploration (Andrew)**

###  Week 2

#### Day 6 (Aug 14): Reflection seismology
  * 9:30 - 10:30 Demo: **Plotting seismic reflection data and picking arrivals (Andrew and Lindsay)**
  * 11 - 12: Self-guided exercises: Seismic reflection
  * 12 - 1: Lunch
  * 1 - 2: Exercises
  * 2 – 3: Lecture:  Lecture: **What is a "model" in geophysics? (Eric)** 
  * 3 - 4: Exercises

#### Day 7 (Aug 15): Modeling and parameter estimation
  * 9:30 - 11: Lecture: **Geodesy, satellites, GPS and InSAR (Eric)**
  * 11 - 12: Lecture: **Modeling an earthquake (Eric)**
  * 12 – 1: Lunch
  * 1 – 4: Self-guided exercises: modeling

#### Day 8 (Aug 16): Making maps and other figures
  * 9:30 - 10:30 Lecture: **Maps and data visualization (Eric)**
  * 11 - 12 Lecture: **Cartopy demo (Eric)**
  * 12 - 1: Lunch 
  * 1 – 4: Time for group projects

#### Day 9 (Aug 17): High performance computing & Group projects
  * **9:00** – 11: **Visit to UNM Center for Advanced Research Computing (CARC)**
  * 11 - 12: Group projects
  * 12 - 1: Lunch
  * 2 - 3 pm: Visit to the Meteorite Museum!
  * Group projects all afternoon

#### Day 10 (Aug 18): Last day!
  * 9:30 – 11: **Group presentations**
  * 11:15 – 12: Lecture: **Going to grad school, careers in geophysics**
  * 12pm onward: Join the EPS department for lunch on the lawn and ice cream social!

## Installation
Programming will be done within the Jupyter-Lab environment. This can be installed through conda (https://www.anaconda.com/).

To ensure your conda environment has all the packages needed for this course:
1) Download the escape2023.yml file (for example by cloning this repository)
2) Open an anaconda prompt, use 'cd' to move to the directory where this file is located, and then run `conda env create -f escape2023.yml`

Alternatively, you can create a mostly similar environment with the following commands:

    conda create --name escape2023 python=3.10
    conda activate escape2023
    conda install -c conda-forge jupyterlab numpy scipy pandas cartopy ipywidgets obspy plotly matplotlib

Finally, you can create the environment manually in Anaconda Navigator by finding the above list of packages and installing them individually.

Feel free to run the code for this course on your own laptop, but we will be working in the Northrop hall computer lab so you can use those computers if you prefer.

## Contributors
Eric Lindsey, Evans Onyango, Jeng Hann Chong, Lindsay Worthington, Mousumi Roy, Brandon Schmandt

[![DOI](https://zenodo.org/badge/501495854.svg)](https://zenodo.org/badge/latestdoi/501495854)

## Maintainers
Eric Lindsey, Lindsay Worthington

## Acknowledgements
This workshop was originally developed throug NSF funding (Award #2146272). Thanks to the UNM Earth & Planetary Sciences Dept. and the College of Arts & Sciences for making it possible to host the program again this year.


