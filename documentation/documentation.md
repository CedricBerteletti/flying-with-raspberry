# Documentation

## Raspberry Pi Zero 2

Pin header 2x20 2,54mm


## Adafruit 9-DOF Absolute Orientation IMU Fusion Breakout - BNO055 - STEMMA QT / Qwiic

If you've ever ordered and wire up a 9-DOF sensor, chances are you've also realized the challenge of turning the sensor data from an accelerometer, gyroscope, and magnetometer into actual "3D space orientation"! Orientation is a hard problem to solve. The sensor fusion algorithms (the secret sauce that blends accelerometer, magnetometer, and gyroscope data into stable three-axis orientation output) can be mind-numbingly difficult to get right and implement on low-cost real-time systems.

Bosch is the first company to get this right by taking a MEMS accelerometer, magnetometer, and gyroscope, and putting them on a single die with a high-speed ARM Cortex-M0 based processor to digest all the sensor data, abstract the sensor fusion and real-time requirements away, and spit out data you can use in quaternions, Euler angles or vectors.

Behold the Adafruit 9-DOF Absolute Orientation IMU Fusion Breakout - BNO055 in Stemma QT format! We also have this breakout in a non-Stemma shape and size. The use is identical between the two breakouts: same library and software will work on both. The QT version is a bit smaller and has plug-and-play I2C connectors on either side for no-solder-required uses! QT Cable is not included, but we have a variety in the shop.

Rather than spending weeks or months fiddling with algorithms of varying accuracy and complexity, you can have meaningful sensor data in minutes thanks to the BNO055 - a smart 9-DOF sensor that does the sensor fusion all on its own!  You can read the data right over I2C and Bob's yer uncle.

The BNO055 can output the following sensor data:
- Absolute Orientation (Euler Vector, 100Hz) Three axis orientation data based on a 360° sphere
- Absolute Orientation (Quaternion, 100Hz) Four point quaternion output for more accurate data manipulation
- Angular Velocity Vector (100Hz) Three axis of 'rotation speed' in rad/s
- Acceleration Vector (100Hz) Three axis of acceleration (gravity + linear motion) in m/s^2
- Magnetic Field Strength Vector (20Hz) Three axis of magnetic field sensing in micro Tesla (uT)
- Linear Acceleration Vector (100Hz) Three axis of linear acceleration data (acceleration minus gravity) in m/s^2
- Gravity Vector (100Hz) Three axis of gravitational acceleration (minus any movement) in m/s^2
- Temperature (1Hz) Ambient temperature in degrees celsius

Use is simple, with I2C support that is 3 or 5 Volt logic safe. We also break out the interrupt pins and address-selection jumpers in case you want two BNO-055's on one I2C bus. We've got both Arduino (C/C++) and CircuitPython libraries available so you can use it with any microcontroller or computer board and get data readings in under 5 minutes. Four mounting holes make for a secure connection.


## Adafruit Mini GPS PA1010D - UART and I2C - STEMMA QT

This miniature GPS breakout is only 1" x 1" (~ 25mm x 25mm) but houses a complete GPS/GNSS solution with both I2C and UART interfaces. There's even an antenna on top, so it's plug and play!
- Support for GPS, GLONASS, GALILEO, QZSS
- -165 dBm sensitivity, up to 10 Hz updates
- Up to 210 PRN channels with 99 search channels and 33 simultaneous tracking channels
- 5V friendly design and only 30mA current draw
- Breadboard-able, with 4 mounting holes
- UART and I2C interfaces, pick whichever you like most!
- RTC battery-compatible
- PPS output on fix ±20ns jitter
- Internal patch antenna
- Low-power and standby mode with WAKE pin

The breakout is built around the MTK3333 chipset, a reliable, high-quality GPS module that can handle up to 33 simultaneous tracking channels, has an excellent high-sensitivity receiver (-165 dBm tracking!), and a built-in antenna. It can do up to 10 location updates a second for high speed, high sensitivity logging or tracking. Power usage is incredibly low, only 30 mA during navigation.

Best of all, we added all the extra goodies you could ever want: an ultra-low dropout 3.3V regulator so you can power it with 3.3-5VDC in, 5V level safe inputs on UART and I2C, a footprint for optional CR1220 coin cell to keep the RTC running and allow warm starts, a green power LED and a tiny red PPS LED. The LED blinks at about 1Hz when a fix is found and is off when no fix.

Unlike our Ultimate GPS modules, this module does not have the ability to connect an external antenna, it's designed to be as small as possible for compact projects.

As with all Adafruit breakouts, we've done the work to make this GPS module super easy to use. We've put it on a breakout board with the required support circuitry and connectors to make it easy to work with, and is now a trend we've added SparkFun Qwiic compatible STEMMA QT JST SH connectors that allow you to get going without needing to solder. Just use a STEMMA QT adapter cable, plug it into your favorite micro or Blinka-supported SBC and you're ready to rock! QT Cable is not included, but we have a variety in the shop. 

Comes with one fully assembled and tested module, a piece of header you can solder to it for breadboarding, and a CR1220 coin cell holder. A CR1220 coin cell is not included, but we have them in the shop if you'd like to use the GPS's RTC

We have a nice fancy library for GPS usage for both Arduino and Python usage. A full tutorial is also available, which has tons of information about the module, how to use the data logger, example code for both CircuitPython & Arduino, and more
https://learn.adafruit.com/adafruit-mini-gps-pa1010d-module