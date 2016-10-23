#    Copyright 2016 Aurora Taraba 
#
#    This file is part of the PoolPump project.
#
#    PoolPump is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PoolPump is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PoolPump.  If not, see <http://www.gnu.org/licenses/>.

from gpiozero import *
from signal import pause
from time import sleep
from datetime import datetime,time

Run1 = time (8,30)  #run every day at 08h30
Run2 = time (20,30) #run every day at 20h30

PoolPump = DigitalOutputDevice(24)
PoolPump.off()

LedRed = LED(17)
LedRed.off()

LedYellow = LED(27)
LedYellow.off()

LedGreen = LED(22)
LedGreen.off()

BlueButton = Button(pin=18, pull_up=False)
BlueButton.hold_time = 0.1

OnOffSwitch = DigitalInputDevice(pin=23, pull_up=False)
while True:
    if  OnOffSwitch.is_active == False:
        #ON/OFF switch is set to OFF
        LedRed.on()     #Program running turn RED LED on
        LedYellow.off() #Poolpump will not start, turn YELLOW LED off
        LedGreen.off()  #Poolpump is not running, turn GREEN LED off
        PoolPump.off()  #Turn poolpump oOFF
    else:
        #ON/OFF switch is set to ON
        LedYellow.on() #Pump is "armed"
        LedRed.on()    #Program running
        if BlueButton.is_held:                                 #blue button pushed
            if not PoolPump.is_active:                         #poolpump not running
                PoolPump.blink(on_time=3600, off_time=0, n=1)  #run pump for an hour
        if Run1 == time(datetime.now().hour, datetime.now().minute) or Run2 == time(datetime.now().hour, datetime.now().minute): #Time to run pump
            if not PoolPump.is_active:                                                                                           #Pump not running yet
                PoolPump.blink(on_time=3600, off_time=0, n=1)                                                                    #Run pump for an hour
        if PoolPump.is_active: #Pump running
             LedGreen.on()     #then turn on green LED
        else:
             LedGreen.off()    #Pump not running, green LED off 
    sleep(0.05)

      
