## To Do List
- i want to recreate the motion of two human arms, one connected to a pair of scissors, the other holding a branch. I will focus on the scissor arm first, when that is able to cut through branches and leaves correctly, I will work on the holding arm.
******* 

- Use a buck down converter [such as](https://www.amazon.com/DROK-Adjustable-Converter-Transformer-Protective/dp/B07JZ2GQJF/ref=sr_1_5?keywords=buck%2Bconverter%2B5a&qid=1577364346&sr=8-5&th=1) with 12v supply to provide 8.4v to scissor_servo
- 3 other servos only require 5 volts, however i want to plug everything into one pwm servo hat if possible
- The tip of the scissor gap must have sufficient torque to cut the branch and seperate the bud from branch
- physical trim test performed with 55kg servo, leaves can be trimmed, however the tip of the scissors are not getting enough torque to cut through the branch at the branch/bud intersection.
- may need to redesign end effector
- yolov8 segmentation? combined with oak d multiple nn detections
- how to identify and return position of leaves that need to be trimmed
- range for oak d camera- Ideal range: 70cm - 8m, MinZ: ~20cm (400P, extended), ~35cm (400P OR 800P, extended), ~70cm (800P)
- i attached camera to an extension rod and steel flat bar(14 inches), it is approximately 18 in from scissors, in a fixed location behind the scissors
- for best results using spatial detection, the camera should be perpendicular with scissors, the spatial detection fails with distance of less than 11 inches  
- using custom yolov5s model and Oak D camera, i created a script that would open and close scissors when a bud is detected within 600mm(z coord) of the camera.  

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
