# ENV-Setup
***
### Introduction
Scripts to help developer in setting up the environment for the project of YoMeal.

### Written In
* BASH script

### What's included
```
env_setup/
  |-- env_setup.sh
  |-- pre_setup.sh
  |-- README.md
```

### env_setup
* This will add required env var into the appropriate profile_file for the current shell (either in ~/.zshrc or in ~/.bash_profile) related to setting up virtualenv
* The script will also create the virtualenv and install the packages/libs usiing pip and requirements.txt

### pre_setup
* This script will change python3 and pip3 as default python and pip.
* It will also install virtualenv and virtualenvwrapper using pip3

#### How to use it?
1. Open a terminal (or `iterm2` -- preferred)
2. Goto the directory where these files are located in
3. (Optional) Execute the command `bash pre_setup.sh` or `./pre_setup.sh`
4. (Optional) Execute the command `bash env_setup.sh` or `./env_setup.sh`
5. Once, you have created the virtualenv usiing the above script or manully, you can work on the virtualenv by executing `workon yomeal` (or `workon $virtualenv_name`) in the appropriate dir

### Limitations
- Make sure you are using python3
- Only works with MacOS for now. (may work on linux environment by update the condition in the beginning of the script/s)
- This/These script/s may change your environment/terminal setup(which could break somthing) so use at your own risks.