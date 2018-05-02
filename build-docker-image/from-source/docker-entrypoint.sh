#!/bin/bash
sed -i -e "s/localhost/"$REDIS_NAME"/g" $HOME/.occopus/occopus_config.yaml
mkdir $LOG_DIR
sed -i -e 's@occopus\.log@'"$LOG_DIR"'/occopus\.log@g' $HOME/.occopus/occopus_config.yaml
sed -i -e 's@occopus-data\.log@'"$LOG_DIR"'/occopus-data\.log@g' $HOME/.occopus/occopus_config.yaml
sed -i -e 's@occopus-events\.log@'"$LOG_DIR"'/occopus-events\.log@g' $HOME/.occopus/occopus_config.yaml
export HOST_IP=$(hostname --ip-address)
exec "$@"
