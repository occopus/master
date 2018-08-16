FROM python:2.7-slim

#Set default values
ENV REDIS_NAME localhost
ENV HOST_IP localhost
ENV LOG_DIR /var/log/occopus

#Install Occopus dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y libffi-dev iputils-ping git curl && \
    ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /usr/lib/x86_64-linux-gnu/libcrypto.so && \
    git clone --depth 1 https://github.com/occopus/master.git /occopus.src --recursive && \
    cd /occopus.src && \
    git submodule foreach git checkout devel && \
    cd /occopus.src/api && \
    pip install --upgrade pip setuptools wheel && \
    cd /occopus.src/api && \
    pip install -r requirements_test.txt --find-links http://pip.lpds.sztaki.hu/packages --trusted-host pip.lpds.sztaki.hu && \
    mkdir -p $HOME/.occopus && \
    curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/occopus_config.yaml -o $HOME/.occopus/occopus_config.yaml && \
    curl https://raw.githubusercontent.com/occopus/docs/devel/tutorial/.occopus/auth_data.yaml -o $HOME/.occopus/auth_data.yaml && \
    apt-get update && \
    apt-get remove --purge -y perl-modules perl curl git git-man && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -r /occopus.src/.git && \
    rm -r /occopus.src/docs && \
    rm -r /var/lib/apt/lists/* && \
    rm -r /root/.cache

COPY docker-entrypoint.sh /usr/local/bin
ENTRYPOINT ["docker-entrypoint.sh"]

CMD occopus-rest-service --parallelize --auth_data_path  $HOME/.occopus/auth_data.yaml --host "$HOST_IP"
