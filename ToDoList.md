
<details>

<summary> ## To Do List </summary>

## slide rail how should slide rail move?

- ***how can i program the slide rail to move the robot up and down when needed, automatically. it needs a signal when the arm needs to grab a branch, and it needs a signal when the branch has been trimmed. 
- arm sends signal to slide rail. 
- mount the robot arm on a linear actuator slide rail(1000mm). Mount the slide rail to the wall vertically, it will move up and down the wall, this way the robot will be able to reach into a bin on the floor. (see linearActuatorInfo.MD)
- robot arm vertically mounted on a wall, a bin full of branches on the floor, the wall arm reaches down into the bin, then moves up into position where a table with a tray and a second robot arm holding scissors will complete the trim

## computer vision how will robot detect and pick up branch?

- Create custom data sets for individual buds and branches.
- yolov5 is compatible with yahboom robot arm
- The camera will identify the branch closest to the end effector and send the coordinates to the branch arm to pick up and hold. There will be many other branches that look similar and will be close together.
  
  

https://colab.research.google.com/github/luxonis/depthai-ml-training/blob/master/colab-notebooks/YoloV5_training.ipynb
- use this for creating annotion boxes - [make sense AI](https://www.makesense.ai/)    -browser based, no download, no install

</details>

<details>

<summary>Web sites for resources</summary>

- ### Camera sites
 - Camera code - https://github.com/luxonis/depthai
 - https://shop.luxonis.com/  for cameras
  
- ### 3d print sites
 - www.markforged.com

- ### other sources to create annotation boxes for dataset 
 - https://www.cvat.ai/
 - https://github.com/heartexlabs/label-studio
 - https://github.com/heartexlabs/labelImg
 - https://github.com/scalabel/scalabel
 - https://github.com/ryouchinsa/Rectlabel-support
 - https://github.com/ultralytics/ultralytics
 - https://www.roboflow.com 

## websites

- [mini jetson nano car](https://medium.com/@anandmohan_8991/jetbot-using-l298n-pwm-motor-a6556ed358d6)
- tech support from yahboom - support@yahboom.com
- [official yahboom website] (https://www.yahboom.net/home)

</details>
