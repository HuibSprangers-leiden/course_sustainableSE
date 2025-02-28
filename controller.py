# This file contains runs the experiments and collects the results in a CSV file

import subprocess
import random
import time

from constants import NUM_EXPERIMENTS, REST_TIME


def pretty_print(energy, duration):
    """
    Pretty prints the energy consumption and duration of an experiment
    """
    print(f"Energy consumption (J): {energy}; Execution time (s): {duration}")


def _process_stdout(output):
    """
    Extracts energy consumption and duration from the output of the energibridge tool
    """

    lines = str(output).split("\n")
    for line in lines:
        if "Energy consumption in joules: " in line:
            parts = line.split(":")
            energy_str, seconds_str = parts[1].strip().split(" for ")
            energy_consumption = float(energy_str)
            duration = float(seconds_str.split(" sec")[0])
            return energy_consumption, duration
    return None, None


def run(cmd):
    """
    Runs a command and returns the output
    """

    return subprocess.check_output(
        f"C:/Users/simon/Documents/EnergiBridge/energibridge.exe --summary -o results.csv {cmd}",
        shell=True,
    )


print("Warmup")
start = time.time()
for _ in range(10):  # warmup
    run("python -m experiment mysql")
    run("python -m experiment sqlite")
end = time.time()
print(f"Elapsed time: {end - start} s")

order = ["mysql", "sqlite"] * NUM_EXPERIMENTS
random.shuffle(order)  # shuffle order of execution

# print(order)
# print(len(order))

print("Starting experiments")

for db in order:
    # print(db)
    output = run(f"python -m experiment {db}")

    energy, duration = _process_stdout(output)
    with open("output.csv", "a") as file:
        file.write(f"{db},{energy},{duration}\n")
    # pretty_print(energy, duration)
    time.sleep(REST_TIME)  # rest
