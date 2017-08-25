FROM ubuntu:16.04

# Get sudo working
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
        sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && echo "swuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/swuser \
    && echo "Defaults env_reset" >> /etc/sudoers.d/swuser \
    && echo "Defaults env_keep = \"http_proxy https_proxy no_proxy\"" >> /etc/sudoers.d/swuser \
    && hash -r

# Switch to a user:
RUN groupadd -r swuser -g 1000 && \
    mkdir /home/swuser && \
    useradd -u 1000 -r -g swuser -d /home/swuser -s /sbin/nologin \
         -c "Docker image user" swuser && \
    chown -R swuser:swuser /home/swuser && \
    echo "swuser:swuser" | chpasswd && \
    adduser swuser sudo
WORKDIR /home/swuser
USER swuser
