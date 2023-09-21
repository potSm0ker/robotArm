To make the robot arm (with raspberry pi 4) do what I need to do, it will need some upgrades. I will turn this toy into a tool.

### Raspberry Pi 4 with geeekpi ice tower cooling fan and servo hat
 - using [raspberry pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) for computing and to control servos
 - pwm  16 servo hat from adafruit
 - geekpi ice tower cooling fan

### Vision - Oak-D pro camera(manual focus) from [Luxonis](https://shop.luxonis.com/products/oak-d-pro)
 - detection model can run on camera, inference results will be sent to nano
 - will use yolov5 custom model to identify leaves and direct scissors to trim leaves
 - yolov5 for locating and picking branches from bin
 - created custom bracket in blender to mount camera to robot
 - custom bracket 3d printed on [Xometry.com](https://www.xometry.com/)
 - 3d model for custom Oak-D pro bracket available in Hardware Info folder

### Increase storage  SAMSUNG T7 Portable SSD 500GB
 - I used win32disk imager to write the custom jetson image provided by yahboom for the robot arm
 - running operations on the jetson nano is much faster using an external ssd via usb3 rather than a micro usb drive.
 - run  gparted    in the terminal to see partitions and expand the file system partion to use the entire 500 gb SSD, in my case it was /dev/sda1 
 - boot from usb [jetsonhacks.com](https://jetsonhacks.com/2021/03/10/jetson-nano-boot-from-usb/)
 - create backups of critical files before attempting, loss of data may occur when trying to remount file system

A useful website for [jetson nano hacks](https://www.jetsonhacks.com/) 




### Upgrade cooling fan and heat sink - GeeekPi 5V PWM Low-Profile CPU Cooler
 - I upgraded to [Ice tower cooling fan](https://www.amazon.com/GeeekPi-Low-Profile-Horizontal-Radiator-Colorful/dp/B07ZYW6ZVR/ref=sr_1_3?crid=2GY7QMQU6IJJ&keywords=ice+tower+cooling+fan+jetson+nano&qid=1690327939&sprefix=ice+tower+cooling+fan+jetson+nano%2Caps%2C132&sr=8-3) from amazon.com
