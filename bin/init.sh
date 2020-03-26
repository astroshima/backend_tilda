#!/bin/sh


export OFFLINE=${OFFLINE:=no}
export BIN_DIR=`dirname $0`
. ${BIN_DIR}/common.sh
#echo $PY_VERSION
if [ "${OFFLINE}" = "yes" ]; then
  setup no
else
  setup
fi


if [ ! -e "${BIN_DIR}/../migrations/main/001_initial.py" ]; then
  flask migration create initial
  flask migration run
fi
flask admin create
