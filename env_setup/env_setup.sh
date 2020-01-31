#!/usr/bin/env bash

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

install_virt_pckgs() {
    succ_msg="Installed virtualenv"
    failure_msg=""
    pip3 install virtualenv >&2 > /dev/null && pip install virtualenv >&2 > /dev/null && echo -e "$COL_GREEN Installed virtualenv $RST" || echo -e "$COL_RED Failed to install virtualenv$RST"
    pip3 install virtualenvwrapper >&2 > /dev/null && pip install virtualenvwrapper >&2 > /dev/null && echo -e "$COL_GREEN Installed virtualenvwrapper $RST" || echo -e "$COL_RED Failed to install virtualenvwrapper$RST"
}


# echo "Do you to perform pre_setup?"
# echo -e "!!!! PRE_SETUP:\nThis will make python3 and pip3 as default versions\n\t+\nit will install virtualenv and virtualenvwrapper\n!!!!\n"
# echo -e "-- Enter the number for your selection and press enter!"
# select yn in "Yes" "No"; do
#     case $yn in
#         Yes ) bash $(echo $PWD)/pre_setup.sh; break;;
#         No ) echo -e "You selected \"NO\" so make sure that you have python3 and pip3 installed otherwise script will fail"; exit;;
#     esac
# done


add_virtualenvwrppaer_env_var() {
    FILE=$1
    CONTENTS=$2
    echo -e "$CONTENTS" >> $FILE
}

install_virt_pckgs

### update environement vars
curr_term=$(echo $SHELL)
PROFILE_FILE=""
echo "$curr_term"
if [ "$curr_term" == "/bin/zsh" ]; then
    PROFILE_FILE="$HOME/.zshrc"
else
    PROFILE_FILE="$HOME/.bash_profile"
fi

Contents=""
if [ "$(echo $VIRTUALENV_PYTHON)" != "$(which python3)" ]; then
    Contents+="export VIRTUALENV_PYTHON=$(which python3) \n"
fi


if [ "$(echo $WORKON_HOME)" != "$HOME/Envs" ]; then
    Contents+="export WORKON_HOME=~/Envs \n"
    mkdir -p $HOME/Envs
fi

if [ "$Contents" != "" ];then
    Contents+="source $(which python3)/virtualenvwrapper.sh\n"
    add_virtualenvwrppaer_env_var $PROFILE_FILE "\n\n$Contents"
    # add_virtualenvwrppaer_env_var $a "\n\n$Contents"
fi


### virtualenv setup
echo "Do you wish to continue and allow the script to create virtualenv for you?"
echo -e "-- Enter the number for your selection and press enter!"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) echo -e "Creating virtualenv"; break;;
        No ) echo -e "You selected \"NO\" so you have to create the virtualenv and install all the dependecies and libs with the required versions"; exit;;
    esac
done

# creating virtualenv using virtualenvwrapper
mkvirtualenv yomeal >&2 > /dev/null
echo "$COL_GREEN -- new virtualenv named \"yomeal\" has been created$RST --"
# Installing dependencies/libs in the virtualenv
workon yomeal
requirements_file="$PWD/requirements.txt"
if [ -f "$requirements_file" ]; then
    echo "$requirements_file exist; so installing the requirements"
    pip3 install -r $requirements_file >&2 > /dev/null
fi

echo -e "\n\n$COL_GREEN!!!!!!!!!!!!!!!!!!! Completed !!!!!!!!!!!!!!!!!!!$RST\n\n"
echo -e "$COL_GREEN Confirm Folloiwng steps before moving further$RST"
echo -e "$COL_YELLOW - Make Sure your virtualenv has been created. You can confirm by going into \'~/Envs/\' and confirm if \"yomeal\" dir exists."
echo -e "$COL_YELLOW - Execute \'source ~/.zsh_rc\' or \'source ~/.bash_profile\' or close&reopen terminal"
echo -e "$COL_YELLOW - Goto your project directory and confimr if you are able to access the virtual env by executing \'workon yomeal\'"
echo -e "$COL_YELLOW - If you require pre_setup.sh or not$RST"
