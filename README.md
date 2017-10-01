# SymEngine Benchmarks

Here is how to build and run the benchmarks:
```
docker build -t symengine/ubuntu_base ./ubuntu_base
docker build -t symengine/conda_base ./conda_base
docker build -t symengine/symengine ./symengine
docker run -it -p 8888:8888 symengine/symengine jupyter notebook --ip='*' --no-browser
```
Then open the `Plots.ipynb` notebook and execute it. It will produce graphs of
the benchmarks.
