#!/bin/sh -f

SCRIPT_DIR=`dirname $0`
SCRIPT_RUN=$SCRIPT_DIR/../run-scripts
SCRIPT_CLAS=$SCRIPT_DIR/../lib/packages/lund/PhysicsFilter.py

$SCRIPT_RUN $SCRIPT_CLAS $*

