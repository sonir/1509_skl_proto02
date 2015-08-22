#! /bin/sh
#sudo pd-tone
#sudo py-tone
sudo pd-extended -nogui -alsa -audioindev 3 -audiooutdev 3 sound_ver11.pd &
sudo python2 motion_button_ver5.py
