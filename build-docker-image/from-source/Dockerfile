FROM python:2.7-slim

#Set default values
ENV REDIS_NAME localhost
ENV HOST_IP localhost
ENV LOG_DIR /var/log/occopus

#Install Occopus dependencies
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev \
    iputils-ping \
    git \
    curl && \
    pip install --upgrade pip && \
    git clone https://github.com/occopus/master.git /occopus.src --recursive && \
    cd /occopus.src \
    && git submodule foreach git checkout devel && \
    cd /occopus.src/api \
    && pip install --upgrade pip setuptools wheel && \
    cd /occopus.src/api \
    && pip install -r requirements_test.txt --find-links http://pip.lpds.sztaki.hu/packages --trusted-host pip.lpds.sztaki.hu && \
#Download default configuration
    mkdir -p $HOME/.occopus \
    && curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/occopus_config.yaml -o $HOME/.occopus/occopus_config.yaml \
    && curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/auth_data.yaml -o $HOME/.occopus/auth_data.yaml && \
    apt-get remove --purge -y libc6-dev perl-modules perl libssl-dev linux-libc-dev python-pip curl git git-man && \
    apt-get autoremove -y && \
    rm -rf occopus.src/.git && \
    rm -rf /var/lib/apt/lists/* 

COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

CMD occopus-rest-service --parallelize --auth_data_path /opt/auth_data.yaml --host "$HOST_IP"
