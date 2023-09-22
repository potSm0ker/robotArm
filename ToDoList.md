## To Do List

## Physical trim test with scissors on end effector(claw), first arm
- how to identify and return position of leaves that need to be trimmed
- position, open and close the scissors to accurately and efficiently trim the leaves
- range for oak d camera- Ideal range: 70cm - 8m, MinZ: ~20cm (400P, extended), ~35cm (400P OR 800P, extended), ~70cm (800P)
- what position should the camera be in relation to the scissors? behind or in front of scissors? attached to arm or on a seperate stand
- yolo v5 image segmentation to identify the coordinates of trim leaves
- need algorithm to control position of scissors in relation to the bud
- use oak d camera determine positions of leaves on bud
  
- using custom yolov5s model and Oak D camera, i created a script that would open and close scissors when a bud is detected within 600mm of the camera.  

## How will robot trim the bud with scissors?
- get distance between camera and scissors, when detected leaf matches the distance of the scissors the scissors should close, then open and repeat until leaves are not detected
- use the 'z' coordinate to create a boundary at the scissors, when the bud leaf crosses the threshold, the scissors should close.

https://colab.research.google.com/github/luxonis/depthai-ml-training/blob/master/colab-notebooks/YoloV5_training.ipynb

# Annotation box app for creating custom data set
- [Make Sense AI](https://www.makesense.ai/)    -browser based, no download, no install



## for second arm that will pick up branches or buds slide rail how should slide rail move?

- [servo motor driver](https://roboteurs.com/products/slushengine?variant=19782069764) SlushEngine: Model X LT Stepper Motor Driver
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
