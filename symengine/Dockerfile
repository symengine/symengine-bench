FROM symengine/conda_base

RUN sudo apt-get update && DEBIAN_FRONTEND=noninteractive \
    sudo apt-get install -yq --no-install-recommends \
        git cmake make g++ libgmp-dev \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && hash -r

RUN conda install python=3.6 jupyter matplotlib && \
    conda clean --all

ARG COMMIT
RUN GIT_SSL_NO_VERIFY=true git clone https://github.com/symengine/symengine && \
    cd symengine && \
    git checkout $COMMIT && \
    cmake . && \
    make

COPY run_bench.py symengine/benchmarks
COPY run_copy.sh .
COPY Plots.ipynb .
