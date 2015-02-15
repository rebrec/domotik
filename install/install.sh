#!/bin/sh

echo Copy of domotik startup script
cp domotik /etc/init.d

echo Adding Up start Script
update-rc.d domotik defaults
