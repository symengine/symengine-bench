# SymEngine Benchmarks

Here is how to build and run the benchmarks:
```
docker build -t symengine/ubuntu_base ./ubuntu_base
docker build -t symengine/conda_base ./conda_base
docker build -t symengine/symengine --build-arg COMMIT=master ./symengine
docker run -it -p 8888:8888 symengine/symengine jupyter notebook --ip='*' --no-browser
```
Then open the `Plots.ipynb` notebook and execute it. It will produce graphs of
the benchmarks.

## Compare two commits

We can compare two commits as follows. The commit 398a3f39 should be faster
than fdf132fc.

```
COMMIT=398a3f39
docker build -t symengine/symengine:$COMMIT --build-arg COMMIT=$COMMIT ./symengine
docker run -t -v `pwd`:/opt/ symengine/symengine:$COMMIT bash run_copy.sh
cp data.json data-$COMMIT.json
COMMIT=fdf132fc
docker build -t symengine/symengine:$COMMIT --build-arg COMMIT=$COMMIT ./symengine
docker run -t -v `pwd`:/opt/ symengine/symengine:$COMMIT bash run_copy.sh
cp data.json data-$COMMIT.json
```
