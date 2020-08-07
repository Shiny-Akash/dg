#!/bin/bash

line='------------------------'

# function for handling result of a process
check_result () {
	echo $line
	if [ $1 -ne 0 ]; then
		echo $2
		echo $line
		exit
	else
		echo $3
		echo $line
	fi
}

# handling pyinstaller installtion
echo "Installing pyinstaller ..."
python3 -m pip install pyinstaller > out.log
check_result $? "Cannot Install Pyinstaller" "Pyinstaller installed successfully"

# using pyinstaller to create executable app
echo "Creating App ..."
python3 -m PyInstaller app.py --onefile 2>>out.log
check_result $? "Cannot Create App" "App Created Successfully"

# cleaning unwanted files and folders
mv dist/app .
rm -r dist/ build/ app.spec
