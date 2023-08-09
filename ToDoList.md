## To Do List

## computer vision how will robot detect and pick up branch?
# yolov5 with luxonis oak d pro depth camera
- spatial calculation- get distance and location of branch to direct the claw
- create a virtual env with python3.8-venv, install python3.8 and upgrade pip
- install requirements for yolov5
- Use google colab ultralytics to create custom data sets for individual buds and branches.
- Use yolov5 custom model to get coordinates of branch in frame.
- The camera will identify the branch closest to the end effector and return the coordinates to the branch arm to pick up and hold. There will be many other branches that look similar and will be close together. How can i decide which branch should be picked up?
  
  

https://colab.research.google.com/github/luxonis/depthai-ml-training/blob/master/colab-notebooks/YoloV5_training.ipynb

# Annotation box app for creating custom data set
- [Make Sense AI](https://www.makesense.ai/)    -browser based, no download, no install



## slide rail how should slide rail move?
- i will need a pair of arms to trim, but only one needs to be vertically mobile.
- get a second arm, hiwonder jetmax with slide rail 
- ***how can i program the slide rail to move the robot up and down when needed, automatically. it needs a signal when the arm needs to grab a branch, and it needs a signal when the branch has been trimmed. 
- arm sends signal to slide rail. 
- mount the robot arm on a linear actuator slide rail(1000mm). Mount the slide rail to the wall vertically, it will move up and down the wall, this way the robot will be able to reach into a bin on the floor. (see linearActuatorInfo.MD)
- robot arm vertically mounted on a wall, a bin full of branches on the floor, the wall arm reaches down into the bin, then moves up into position where a table with a tray and a second robot arm holding scissors will complete the trim



<details>

<summary>Web sites for resources</summary>

- ### Camera sites
 - Camera code - https://github.com/luxonis/depthai
 - https://shop.luxonis.com/  for cameras
  
- ### 3d print sites
 - www.markforged.com

</details>
