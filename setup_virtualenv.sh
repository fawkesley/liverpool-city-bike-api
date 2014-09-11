#!/bin/bash -eux

THIS_SCRIPT=$(readlink -f $0)
THIS_DIR=$(dirname ${THIS_SCRIPT})

VENV_DIR=${THIS_DIR}/venv

function nuke_virtualenv {
    if [ -d "${VENV_DIR}" ]; then
        rm -rf ${VENV_DIR}
    fi
}

function setup_virtualenv {
    if [ -s "${THIS_DIR}/.python_version" ]; then
        virtualenv ${VENV_DIR} -p "$(cat ${THIS_DIR}/.python_version)"
    else
        virtualenv ${VENV_DIR} -p $(which python3)
    fi

    set +u
    source ${VENV_DIR}/bin/activate
    set -u
}

function install_dependencies {
    pip install -r ${THIS_DIR}/requirements.txt
}

nuke_virtualenv
setup_virtualenv
install_dependencies
