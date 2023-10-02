To make the robot arm (with raspberry pi 4) do what I need to do, I will use off the shelf parts whenever possible. All parts will be mounted to a metal plate.

# Current parts list

### The base of the arm [2 DoF Pan Tilt Digital Servo Kit](https://www.amazon.com/Digital-Bracket-Building-Raspberry-unassembled/dp/B0B6PP8NFD/ref=sr_1_2?crid=14A3RCG5Q13P3&keywords=2+DoF+Pan+Tilt+Digital+Servo+Kit&qid=1696217128&s=toys-and-games&sprefix=2+dof+pan+tilt+digital+servo+kit%2Ctoys-and-games%2C110&sr=1-2)
 - uses 2 pwm servos for 2 dof 
 - attached a 20kg dual output servo to give it 3 Dof
 - attached the end effector from yahboom robot arm to the 20kg servo to achieve 4 dof.

#### Raspberry Pi 4 with geeekpi ice tower cooling fan, 16 pwm servo hat and extra tall case
 - using [raspberry pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) for computing and to control servos
 - pwm  16 [servo hat](https://www.adafruit.com/product/2327) from adafruit
 - [geekpi ice tower cooling fan](https://www.amazon.com/GeeekPi-Raspberry-Low-Profile-Cooling-Heatsink/dp/B07ZV1LLWK/ref=asc_df_B07ZV1LLWK/?tag=&linkCode=df0&hvadid=416672671431&hvpos=&hvnetw=g&hvrand=15694554880292079333&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9029971&hvtargid=pla-871699005978&ref=&adgrpid=95587150204&th=1)
- [rpi4 case](https://www.amazon.com/ElectroCookie-Raspberry-Aluminum-Cooling-Changing/dp/B09QG349ZL/ref=sr_1_7_sspa?keywords=extra+tall+rpi4+case&qid=1696197104&sr=8-7-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1)

### digital pwm servos 55kg coreless, 35kg coreless, and 20kg(dual output)
 - I am using digital pwm servos, not serial servos. Digital servos are easier for me to control and have more precise movement. 
 - [55kg servo](https://www.amazon.com/Coreless-Steering-Aluminum-Waterproof-Shockproof/dp/B0C2Z9YX7H/ref=asc_df_B0C2Z9YX7H/?tag=hyprod-20&linkCode=df0&hvadid=673668631339&hvpos=&hvnetw=g&hvrand=4761762259582424309&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9029977&hvtargid=pla-2204960019756&psc=1&gclid=CjwKCAjwseSoBhBXEiwA9iZtxpNmnpm6wy0of9JX4FwsqFhEEBvt9jGdUQd8fY0Nr3gyQa495heLxxoCNS4QAvD_BwE)

### Vision - Oak-D pro camera(manual focus) from [Luxonis](https://shop.luxonis.com/products/oak-d-pro)
 - detection model can run on camera, inference results will be sent to nano
 - will use yolov5 custom model to identify leaves and direct scissors to trim leaves
 - yolov5 for locating and picking branches from bin
 - created custom bracket in blender to mount camera to robot
 - custom bracket 3d printed on [Xometry.com](https://www.xometry.com/)

#### yahboom robot arm end effector and baseplate, stripped everything else off
 - I attached scissors to end effector and upgraded servo on bottom of end effector 
 - started with this [robot arm kit](https://www.amazon.com/Yahboom-Raspberry-Building-Programmable-Electronic/dp/B09V7H7V9Q/ref=asc_df_B09V7H7V9Q/?tag=hyprod-20&linkCode=df0&hvadid=673818249115&hvpos=&hvnetw=g&hvrand=11886040620678903792&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9029977&hvtargid=pla-2401058327752&psc=1&gclid=CjwKCAjwseSoBhBXEiwA9iZtxvgBvlNrhx7YjR7deNZ5poqzRaRxqfmWdkdNQDw5p8ll-8gpVQGwcxoCNZEQAvD_BwE) 
 - from yahboom, however I could not update jetson nano, nor use the serial servos it came with. Also, the brackets for the arm only fit the servos from yahboom
 
#### [scissors CHIKAMASA B-500SF Stainless Steel](https://www.amazon.com/Chikamasa-Stainless-Scissors-Fluorine-Resin-resistant/dp/B00JSYB9I6/ref=asc_df_B00JSYB9I6/?tag=hyprod-20&linkCode=df0&hvadid=229261240507&hvpos=&hvnetw=g&hvrand=7797966275015044966&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9029977&hvtargid=pla-393545955103&psc=1)



**** As of August 2023 - no longer using the parts below ****

#### Jetson nano developer kit attached to yahboom expansion board
 - started with a jetson nano, it was difficult to do anything with the jetson nano. the expansion board it was attached to had no documentation that I could find, so I switched to a raspberry pi 4 with 8 gb ram and pwm servo hat to drive the servos.

#### Increase storage  SAMSUNG T7 Portable SSD 500GB
 - I used win32disk imager to write the custom jetson image provided by yahboom for the robot arm
 - running operations on the jetson nano is much faster using an external ssd via usb3 rather than a micro usb drive.
 - run  gparted    in the terminal to see partitions and expand the file system partion to use the entire 500 gb SSD, in my case it was /dev/sda1 
 - boot from usb [jetsonhacks.com](https://jetsonhacks.com/2021/03/10/jetson-nano-boot-from-usb/)
 - create backups of critical files before attempting, loss of data may occur when trying to remount file system

#### Upgrade cooling fan and heat sink - GeeekPi 5V PWM Low-Profile CPU Cooler
 - I upgraded to [Ice tower cooling fan](https://www.amazon.com/GeeekPi-Low-Profile-Horizontal-Radiator-Colorful/dp/B07ZYW6ZVR/ref=sr_1_3?crid=2GY7QMQU6IJJ&keywords=ice+tower+cooling+fan+jetson+nano&qid=1690327939&sprefix=ice+tower+cooling+fan+jetson+nano%2Caps%2C132&sr=8-3) from amazon.com
