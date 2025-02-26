# Sustainable Software Engineering (CS4415) - Group 12

We are comparing MySQL and SQLite in the context of sustainability, this comparison will focus on energy consumption, using **[EnergiBridge](https://github.com/tdurieux/EnergiBridge)** to measure and analyze the energy usage of both databases in a local testing environment.

## Setup

`(This project has been developed and tested on Windows 11 and requires Python 3)`

- Clone this repo: `git clone https://github.com/HuibSprangers-leiden/course_sustainableSE && cd course_sustainableSE`

- Install Python packages:

  ```
  # Create virtual environment (optional)
  # python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  ```

- Run setup

  ```
  python setup.py
  ```

- Install EnergiBridge

- Install and setup MySQL

- Install and setup SQLite

## Run experiments

- ```
  python -m controller
  ```
  measurements are saved in `output.csv`
