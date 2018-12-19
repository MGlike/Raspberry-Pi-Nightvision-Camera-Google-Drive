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
Infrared Nightvision Camera for Raspberry Pi (just search Raspberry Pi Infrared Camera, you can have a ~70° and a 130° angle camera): 
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

Coming soon...

#### Software

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

Install the crontab by copying all the contents of the crontab file (from the repository) into the file opening after the following command

```
sudo crontab -e
```

#### Google Drive API

Coming soon...

## Running the tests

Look at your Google Drive Account. All pictures will be uploaded there in a time frame of 15 minutes.


## Built With

* [Python 2.7](https://www.python.org/downloads/release/python-2715/) - Python 2.7.15


## Authors

* **MGlike** - *Initial work* - [Raspberry-Pi-Nightvision-Camera-Google-Drive](https://github.com/MGlike/Raspberry-Pi-Nightvision-Camera-Google-Drive)
