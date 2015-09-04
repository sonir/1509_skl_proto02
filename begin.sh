#! /bin/sh
#sudo pd-tone
#sudo py-tone
sudo pd-extended -nogui -alsa -audioindev 3 -audiooutdev 3 sound_ver14.pd &
sudo python2 motion_button_ver7.py
