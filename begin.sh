#! /bin/sh
#sudo pd-tone
#sudo py-tone
sudo pd-extended -nogui -alsa sound_ver9.pd &
sudo python2 motion_button_ver4.py
