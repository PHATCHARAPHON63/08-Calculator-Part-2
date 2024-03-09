"""Test package."""

# Append the src directory to the system path.
import sys
import os.path as pth

sys.path.append(pth.realpath(pth.join(pth.dirname(__file__), '../src')))
