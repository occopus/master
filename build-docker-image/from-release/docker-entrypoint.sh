#!/bin/bash
mkdir -p $LOG_DIR
CONF_PATH=$HOME/.occopus/occopus_config.yaml
sed -i -e "s/localhost/"$REDIS_NAME"/g" $CONF_PATH
if ! $(grep -q "$LOG_DIR"/occopus.log $CONF_PATH); then sed -i -e 's@occopus\.log@'"$LOG_DIR"'/occopus\.log@g' $CONF_PATH; fi
if ! $(grep -q "$LOG_DIR"/occopus-data.log $CONF_PATH); then sed -i -e 's@occopus-data\.log@'"$LOG_DIR"'/occopus-data\.log@g' $CONF_PATH; fi
if ! $(grep -q "$LOG_DIR"/occopus-events.log $CONF_PATH); then sed -i -e 's@occopus-events\.log@'"$LOG_DIR"'/occopus-events\.log@g' $CONF_PATH; fi
export HOST_IP=$(hostname --ip-address)
exec "$@"
