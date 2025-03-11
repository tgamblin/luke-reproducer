#!/usr/bin/env spack-python

import spack.environment as ev

env = ev.Environment("./env")

print("ACTIVATE")
with env:
    print("INSIDE")

print("DEACTIVATE")
