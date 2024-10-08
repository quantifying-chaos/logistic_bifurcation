# Logistic Bifurcation

This repository contains several independent python scripts on logistic functions.

The script `./logistic_bifurcation.py` reproduce the logistic bifurcation diagram similar to figure 2.11 in [EO] (see references).

## Build and Run instructions

1. (Optional) Create and activate a python virtual environment with `python -m venv .venv; source .venv/bin/activate`
1. Install required packages with `pip install -r requirements.txt`
1. Run the program with `python <filename>.py`

You may also copy and paste the source code into a Jupyter Notebook

### Wayland

To run on linux-wayland environment, set `QT_QPA_PLATFORM=xcb` before calling python.

## References

[EO]: Chaos in Dynamical Systems , Edward Ott, Cambridge University Press, 2002
