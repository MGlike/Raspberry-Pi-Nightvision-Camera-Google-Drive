# Raspberry-Pi-Nightvision-Camera-Google-Drive
With this project you are routinely able to take pictures in a given time period and upload them to Google Drive.

The camera will automatically switch between nightmode and daymode as soon as you have connected your camera to your Raspberry Pi GPIO.

All taken pictures on your Raspberry Pi will be deleted after a taken picture. Furthermore, all oldest files will then be deleted from your Google Drive, so that only the currently 10 most recent photos will be held online.


## Getting Started

### Prerequisites
What Hardware you need

```
Raspberry Pi (tested on 1 b+)
SD Card (tested on Raspbian Stretch)
Sufficient Power Supply (tested on 2A)
Infrared Nightvision Camera for Raspberry Pi 
(just search Raspberry Pi Infrared Camera, you can have a ~70° and a 130° angle camera)
```

What things you need to install the software and how to install them
```
sudo apt -y update
sudo apt -y upgrade
sudo apt -y dist-upgrade
sudo apt autoremove
sudo raspi-config (go to the very bottom where it says 'camera' and hit enter)
```

### Installing

#### Hardware

Assemble your nightvision camera.

Next, solder the male part of a female to male jumper cable to the small hole to the right of the camera.

To finish off, you only need to plug the female part to a GPIO port that can be controlled via software.

The solution I chose was the GPIO nearest to the USB, but on the far side of the Raspberry Pi (Pin 40). If you choose another port, you have to adapt that in the switchToDayVision and switchToNightVision.

#### Software

#### Google Drive API

Follow the guide [Drive API v3](https://developers.google.com/drive/api/v3/quickstart/python/) and setup Google's sample to check if everything is working. Afterwards just replace the sample by the code in this repository, also stated in the following section.

#### Raspberry Pi

Create a folder called Python_Projects and in that a folder called nightvision_camera.

```
cd /home/pi/Documents
mkdir Python_Projects
cd Python_Projects
mkdir nightvision_camera
```

Copy the three python files to your system and move them to the directory /home/pi/Documents/Python_Projects/nightvision_camera

```
mv *.py /home/pi/Documents/Python_Projects/nightvision_camera
```

Also don't forget to put your credentials.json and token.json from Google in this same working directory

```
mv *.json /home/pi/Documents/Python_Projects/nightvision_camera
```

Install the crontab by copying all the contents of the crontab file (from the repository) into the file opening after the following command

```
sudo crontab -e
```

## Running the tests

Look at your Google Drive Account. All pictures will be uploaded there in a time frame of 15 minutes.


## Built With

* [Python 2.7.15](https://www.python.org/downloads/release/python-2715/)


## Authors

* **MGlike** - *Initial work* - [Raspberry-Pi-Nightvision-Camera-Google-Drive](https://github.com/MGlike/Raspberry-Pi-Nightvision-Camera-Google-Drive)
