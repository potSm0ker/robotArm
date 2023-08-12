To make the robot arm (with jetson nano 4gb) do what I need to do, it will need some upgrades. I will turn this toy into a tool.
A useful website for [jetson nano hacks](https://www.jetsonhacks.com/)

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
 - boot from usb [jetsonhacks.com](https://jetsonhacks.com/2021/03/10/jetson-nano-boot-from-usb/)
 - increase the storage space by copying and mounting the file system to a usb drive of your choice
 - create backups of boot device
 




### Upgrade cooling fan and heat sink
 - I upgraded to [Ice tower cooling fan](https://www.amazon.com/GeeekPi-Low-Profile-Horizontal-Radiator-Colorful/dp/B07ZYW6ZVR/ref=sr_1_3?crid=2GY7QMQU6IJJ&keywords=ice+tower+cooling+fan+jetson+nano&qid=1690327939&sprefix=ice+tower+cooling+fan+jetson+nano%2Caps%2C132&sr=8-3) from amazon.com
