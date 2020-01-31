# ENV-Setup
***
### Introduction
Scripts to help developer in setting up the environment for the project of YoMeal. This script is very basic so may require few manual steps. Also, includes the manual steps.

### Written In
* BASH script

### What's included
```
env_setup/
  |-- env_setup.sh
  |-- pre_setup.sh
  |-- README.md
```

### Preq
If you are running the script then make sure you have python3 and pip3 installed on your machine.

#### Preq Install
* Install homebrew using `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
(https://brew.sh/)
* install python3 and pip3 using `brew install python3`

### env_setup.sh
* This will add required env var into the appropriate profile_file for the current shell (either in ~/.zshrc or in ~/.bash_profile) related to setting up virtualenv
* The script will also create the virtualenv and install the packages/libs usiing pip and requirements.txt

### pre_setup.sh
* This script will change python3 and pip3 as default python and pip.
* It will also install virtualenv and virtualenvwrapper using pip3

#### How to use it?
1. Open a terminal (or `iterm2` -- preferred)
2. Goto the directory where these files are located in
3. (Optional) Execute the command `bash pre_setup.sh` or `./pre_setup.sh`
4. Execute the command `bash env_setup.sh` or `./env_setup.sh`
5. Once, you have created the virtualenv using the above script or manully, you can work on the virtualenv by executing `workon yomeal` (or `workon $virtualenv_name`) in the appropriate dir
6. Then, install requirements in the virtualenv using `pip install -r requirements.txt` (If script ran without any error then it would perfom this step so you can skip this step.)

### FOR OTHER SYSTEM (MANUAL STEPS)
* Install python3 and pip3 (https://www.python.org/downloads/ , https://pip.pypa.io/en/stable/installing/)
* Install virtualenv and virtualenvwrapper (https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
* (Linux/Unix system only -- google steps for other system) open the environment profile file (Eg, .bashrc, .bash_profile, .zsh, etc) and add following lines
  ```
  export VIRTUALENV_PYTHON=$(which python3) # this to select python3 as default python version for virtualenv
  export WORKON_HOME=~/Envs # this is where virtual env will be setup
  source $(which python3)/virtualenvwrapper.sh
  ```

### Limitations
- Make sure you are using python3
- Only works with MacOS for now. (may work on linux environment by update the condition in the beginning of the script/s)
- This/These script/s may change your environment/terminal setup(which could break somthing) so use at your own risks.