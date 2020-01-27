#!/usr/bin/env bash

# WARNING:
# This script will change python3 and pip3 as default python and pip.

# tput codes
RST="$(tput sgr0)"
COL_BLACK="$(tput setaf 0)"
COL_RED="$(tput setaf 1)"
COL_GREEN="$(tput setaf 2)"
COL_YELLOW="$(tput setaf 3)"
COL_BLUE="$(tput setaf 4)"
COL_WHITE="$(tput setaf 7)"
TXT_UNDERLINE="$(tput smul)"

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "$TXT_UNDERLINE---> MacOS detected so moving further with env_setup script. <---$RST\n"
else
    # exiting for now but later it can be updated
    echo "Currently, script only works with MacOS!!!!!"
    exit 1
fi


generate_err_and_exit() {
    echo "$1" >&2
    echo -e "!!! Exited with the Error Code !!!\n\n" >&2
    kill 0
}

if_pckg_installed() {
    pckg=$1
    is_insatlled=`which $pckg`
    [ -z "$is_insatlled" ] && echo "missing $pckg"
}

package_check() {
    pckg=$1
    local ret=$(if_pckg_installed $pckg)
    if [[ "$ret" == "missing $pckg" ]]; then
        generate_err_and_exit "$COL_RED\"$pckg\"$RST is not installed"
    else
        echo "$(which $pckg)"
    fi
}

install_using_pip() {
    pip install $1 >&2 > /dev/null
}

setup_pip3_as_default() {
    local pip_path=$(package_check pip)
    local pip3_path=$(package_check pip3)
    if [ "$pip_path" == "$pip3_path" ]; then
        echo -e "pip3 is already setup as pip"
    fi
    unlink $pip_path
    ln -s $pip3_path $pip_path
}

setup_python3_as_default() {
    local python_path=$(package_check python)
    local python3_path=$(package_check python3)
    if [ "$python_path" == "$python3_path" ]; then
        echo -e "python3 is already setup as python"
    fi
    unlink $python_path
    ln -s $python3_path $python_path
}


setup_python3_as_default
setup_pip3_as_default


### install virtualenev and virtualenvwrapper
install_using_pip virtualenv
install_using_pip virtualenvwrapper