#! /bin/sh
#sudo pd-tone
#sudo py-tone
sudo pd-extended -nogui -alsa sound_ver8.pd &
sudo python2 motion_button_ver3b.py
