FROM symengine/ubuntu_base

RUN sudo apt-get update && DEBIAN_FRONTEND=noninteractive \
    sudo apt-get install -yq --no-install-recommends \
        wget bzip2 \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && hash -r

ENV	PATH="/home/swuser/conda_root/bin:$PATH"

RUN wget --no-check-certificate https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p $HOME/conda_root && \
    rm miniconda.sh && \
	conda config --set always_yes yes --set changeps1 no && \
	conda config --add channels conda-forge --force && \
	conda info -a && \
	conda update -q -n root conda && \
    conda clean --all
