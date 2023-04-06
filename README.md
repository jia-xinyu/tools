<div align="center">

# Development Tools
</div>

## Introduction
This repository collects some useful development tools.

* `UDP` : UDP communication protocol (C++, Python)
* `CSV` : csv file writer/reader (C++)
* `TXT` : csv, txt file reader (Python)
* `Filters` : digital filters (MATLAB)

## UDP
Before testing UDP on PC and Teensy, set the former as a client that sends Teensy's IP. The computer's own IP must be different from that in client.c.


**1)** Make sure in the `UDP` folder. For a client, compile and run
```
sudo gcc client.c -o client -lm
./client
```

**2)** Similarly, for a server
```
sudo gcc server.c -o server -lm
./server
```

* If testing both on one PC, use the loop address `127.0.0.1`.

* `udp_send.py` and `udp_recv.py` are Python version.


## CSV

**1)** Make sure in the `CSV` folder. Compile and run
```
sudo g++ write.cpp -o write -lm
./write
```

**2)** Make sure the file `test.csv` exists. Compile and run
```
sudo g++ read.cpp -o read -lm
./read
```

## TXT

* `plot_ctrl.py` - csv reader

* `plot_joint.py` - txt reader

## Filters

* First-order low/high pass filter

* Second-order command filter

* Second-order Butterworth filter

* One-dimensional Kalman filter

## Notes

* For the permission error when running Python files in Linux, run
```
sudo chmod u+x ./tools -R
```