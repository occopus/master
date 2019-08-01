FROM ubuntu:16.04

#Install Occopus dependencies
RUN apt-get update && apt-get install -y python \
    python-dev \
    libffi-dev \
    libssl-dev \
    python-pip \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

ENV REDIS_NAME localhost
ENV HOST_IP localhost
ENV LOG_DIR /var/log/occopus

#Install Occopus
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && pip install --find-links http://pip.lpds.sztaki.hu/packages --no-index --trusted-host pip.lpds.sztaki.hu OCCO-API \
    && mkdir -p $HOME/.occopus \
#Download default configuration
    && curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/occopus_config.yaml -o $HOME/.occopus/occopus_config.yaml \
    && curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/auth_data.yaml -o $HOME/.occopus/auth_data.yaml \
#HOTFIX
    && curl https://raw.githubusercontent.com/occopus/enactor/devel/occo/enactor/downscale.py -o /usr/local/lib/python2.7/dist-packages/occo/enactor/downscale.py \
    && apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["--parallelize", "--host", "0.0.0.0"]
