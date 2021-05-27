# example-screenshot-taker

Example screenshot taker is a simple robot which works in the background. It takes screen shots of the primary display and saves that in the `output` directory.

## Installation

Just clone this repo. In Windows that should be all you need to do. 

However, Screenshot functionality requires the Pillow module. OS X uses the `screencapture` command, which comes with the operating system. Linux uses the `scrot` command, which can be installed by running sudo `apt-get install scrot`.

## Using it

 - Get the robot from github: https://github.com/robocorp/example-screenshot-taker.git
 - Install RCC from: https://github.com/robocorp/rcc#installing-rcc-from-command-line
 - Start by running: rcc run --robot robot.yaml
 - Stop running with Ctrl + C (or it will automatically stop in three hours.)