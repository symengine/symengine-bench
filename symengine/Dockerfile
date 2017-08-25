FROM symengine/ubuntu_base

RUN sudo apt-get update && DEBIAN_FRONTEND=noninteractive \
    sudo apt-get install -yq --no-install-recommends \
        git cmake make g++ libgmp-dev \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && hash -r

RUN GIT_SSL_NO_VERIFY=true git clone https://github.com/symengine/symengine && \
    cd symengine && \
    cmake . && \
    make
