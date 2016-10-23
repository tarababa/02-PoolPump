# 02-PoolPump
Poolpump control with a Raspberry Pi Zero. Hardcoded two times daily when the pump will start and run for an hour. The finished product looks a bit crude but this is due to the fact that all parts where repurposed / scavanged from other projects. The python program was written by Aurora.

## Functions
1. Red LED indicates pool pump program is running
2. Yellow LED indicates pool pump is "armed" i.e. the pump may be turned i.e. switch 4. is in the on position.
3. Green LED indicates pool pump is running
4. On/Off Switch, the pool pump can only come on when this switch is in the ON position 
5. Ad-Hoc switch, runs pool pump for an hour when pressed.

## Run PoolPump.py on startup
Edit /etc/rc.local and add the following lines. (Obviously they must match the path to the `PoolPump.py` script).

```
# Run PoolPump timer
(python3 /home/pi/PoolPump/PoolPump.py)&
```

<img src="https://github.com/tarababa/02-PoolPump/blob/master/img/Poolpump-timer.png" width="800">
