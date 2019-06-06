# Raspberry-Pi-Nightvision-Camera-Google-Drive
With this project you are routinely able to take pictures in a given time period and upload them to Google Drive.

The camera already automatically switches between day and nightmode (at least in newer camera models).

All taken pictures on your Raspberry Pi will be deleted (from the RAM-Disk) after a taken picture. Furthermore, all oldest files will then be deleted from your Google Drive, so that only the currently 10 most recent photos will be held online.

To minimize failures during runtime, write access to the SD card is minimized by using the RAM-Disk. Furthermore, the Raspberry Pi is rebooted periodically and also in case of an connection/authentication failure.

To further reduce failures you could disable swapping, setup a hardware watchdog (powered by the Broadcom BCM2708 Chip) that checks for systems' consistent functionality and maybe also cool the system/camera actively or passively.


## Getting Started

### Prerequisites
What Hardware you need

```
Raspberry Pi (tested on 1 b+)
SD Card (tested on Raspbian Stretch)
Sufficient Power Supply (tested on 2A)
Infrared Nightvision Camera for Raspberry Pi 
(just search Raspberry Pi Infrared Camera, you can have a ~70° and a 130° angle camera; I used the widescreen camera)
```

What things you need to install the software and how to install them
```
sudo apt -y update
sudo apt -y upgrade
sudo apt -y dist-upgrade
sudo apt autoremove
sudo raspi-config (go to '5 Enable Camera' and hit enter)
```

### Installing

#### Hardware

Assemble your nightvision camera and plug it into the Raspberry Pi.

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

Install the RAM-Disk by copying and pasting the content of the file fstab to your /etc/fstab. Don't forget to create the /var/pictures folder and set the permission according to the following. The RAM-Disk minimizes any access to the SD card.

```
sudo mv fstab /etc/fstab
sudo mkdir /var/pictures
sudo chown -R pi:pi /var/pictures
sudo chmod 0775 /var/pictures
sudo reboot
```

## Running the tests

Look at your Google Drive Account. All pictures will be uploaded there in a time frame of about 15 minutes and after a reboot of the device.
Of course you can also run the routine.py manually to upload a picture.


## Built With

* [Python 2.7.15](https://www.python.org/downloads/release/python-2715/)


## Authors

* **MGlike** - *Initial work* - [Raspberry-Pi-Nightvision-Camera-Google-Drive](https://github.com/MGlike/Raspberry-Pi-Nightvision-Camera-Google-Drive)
