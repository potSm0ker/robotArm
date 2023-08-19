## To Do List

## How will robot trim the bud with scissors?
- use yolov5?
- using oak d camera/yolov5, get the x,y,z coordinates of the leaves that need to be cut.
- scan bud and determine locations of leaf
- use the 'z' coordinate to create a boundary at the scissors, when the bud leaf crosses the threshold, the scissors should close.
- spatial calculation- get distance and location of bud to direct the claw holding the scissors
  



- Use yolov5 custom model to get coordinates of branch/bud in frame.

- create virtual environments with python3.8(at least) to install requirements 
  

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
 - www.xometry.com

</details>
