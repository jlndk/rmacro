#!/bin/bash

### Util functions
trim() {
    local var="$*"
    var="${var#"${var%%[![:space:]]*}"}"   # remove leading whitespace characters
    var="${var%"${var##*[![:space:]]}"}"   # remove trailing whitespace characters
}


##



if [ "$(whoami)" != "root" ]; then
    echo "This installer must run as superuser. Trying to rerun as root."
    echo "If promted for a password, please type it to continue."
    echo ""
    echo ""
    sudo su -s "$0"
    exit
fi


echo "========================================================================="
echo "                            RMACRO INSTALLER                             "
echo "========================================================================="
echo "This will download dependencies and install the program"
read -r -n 1 -p "Do you want to install rmacro? (y/n): " response
echo ""
echo ""
echo "" #Add some empty lines

response=${response,,}    # tolower

dir='/usr/etc/rmacro'

if [[ $response =~ ^[yY](es)* ]]; then

    echo "========================================================================="
    echo "                        CHOOSE INSTALLATION PATH                         "
    echo "========================================================================="
    echo "Where do you want to install rmacro? Default is $dir."

    read -r -p "Enter a valid path or press enter to use the default: " cpath

    echo ""

    trim $cpath

    if [[ "$cpath" != "" ]]; then
        if [ ! -d "$cpath" ]; then
            echo "Seems like the requested directory doesn't exist yet."
            read -r -n 1 -p "Do you want to have this directory created for you automaticly? (y/n): " response

            if [[ $cpath =~ ^[yY](es)* ]]; then
                mkdir $cpath
            else
                echo "Create this directory manually then and run the script again."
            fi
        fi

        dir="$cpath"
    else
        #Checking if the directory exists again since we dont want to ask users
        #when we create dir for the default path
        if [ ! -d "$dir" ]; then
            mkdir $dir
        fi
    fi


    echo "========================================================================="
    echo "                         PERFORMING INSTALLATION                         "
    echo "========================================================================="
    echo ""

    echo "Installing dependencies..."
    echo "------------------------------"
    apt-get install -y python-xlib
    echo ""

    echo "Installing rmacro..."
    cp -r * $dir

    echo ""


    echo "Finishing up..."
    cd $dir
    chmod +x keyutil.py
    chmod +x rmacro

    echo ""
fi


echo ""
