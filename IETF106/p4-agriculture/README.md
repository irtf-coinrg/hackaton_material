# P4 Prototype for Filtering Anomalous Agricultural Sensor Readings

## Description
A simple packet filtering P4 prototype. The P4 pipeline filters out sensor data that exceeds certain predefined thresholds and mirrors it to a different egress port for further analysis. <br>

h1 will act as the agricultural sensor sending data to h2, while h3 acts as the collector for mirrored sensor data which contains anomalous readings.

## Usage
### Step 1
Start the project with `make run`.
### Step 2
In a seperate terminal, launch bmv2's CLI with the command `simple_switch_CLI`. Configure port 3 as the mirroring port for mirror session ID 0 at the bmv2 switch, `mirroring_add 0 3`.
### Step 3
Launch h1 h2 h3's terminal in Mininet's console, `xterm h1 h2 h3`. <br>
Start up the receiver script at h2 h3 with `./receive.py`. <br>
### Step 4
In h1's terminal, start up the sender script with the destination address targetted at h2, `./send.py 10.0.1.2`. <br>
Upon starting the sender script, you will see the following prompt:
```
Enter pH value: 7.5
Enter temperature (degree Celcius): 37.5
```
### Step 5
The P4 program has match action rules pre-installed, where `1 <= pH <= 6 OR temp >= 25.0 degree Celcius` will trigger the action, causing the packet to be mirrored. <br>
You can play around with the script with different pH and temperature values. <br>
Have fun!