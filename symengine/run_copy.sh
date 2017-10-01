#!/bin/bash

set -e
set -x

cd symengine/benchmarks
python run_bench.py
cp data.json ../..
sudo cp data.json /opt/
