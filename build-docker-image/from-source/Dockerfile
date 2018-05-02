FROM ubuntu:16.04

#Install Occopus dependencies
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    libffi-dev \
    libssl-dev \
    python-pip \
    iputils-ping \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*
#RUN apt-get install -y --no-install-recommends curl

#Set default values
ENV REDIS_NAME localhost
ENV HOST_IP localhost
ENV LOG_DIR /var/log/occopus

#Install Occopus from source
RUN pip install --upgrade pip 
RUN git clone https://github.com/occopus/master.git /occopus.src --recursive
RUN cd /occopus.src \
    && git submodule foreach git checkout devel
RUN cd /occopus.src/api \
    && pip install --upgrade pip setuptools wheel
RUN cd /occopus.src/api \
    && pip install -r requirements_test.txt --find-links http://pip.lpds.sztaki.hu/packages --trusted-host pip.lpds.sztaki.hu

#Download default configuration
RUN mkdir -p $HOME/.occopus \
    && curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/occopus_config.yaml -o $HOME/.occopus/occopus_config.yaml \
    && curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/auth_data.yaml -o $HOME/.occopus/auth_data.yaml 

COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

CMD occopus-rest-service --parallelize --auth_data_path /opt/auth_data.yaml --host "$HOST_IP"
