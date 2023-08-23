## To Do List

## Physical trim test with scissors on end effector(claw)
- [servo adapter](https://www.helidirect.com/products/micro-ikon-brain-servo-adapter-standard-jr-futaba-connector-to-jst?currency=USD&utm_source=googleads&utm_campaign=17920518873&utm_medium=ad&utm_content=614199139432&utm_term=&gclid=Cj0KCQjw3JanBhCPARIsAJpXTx4ntVsp2woGyBfCZQ4ViIqE4ZeD16KjYCa8sjP82epke8_H2l83EFoaAvKqEALw_wcB)
- i need to get a JR Female To JST 50mm to replace servo, i need a male JR connectro to micro jst adapter to connect the 35kg servo the yahboom robot servos, the cord connections do not match
- using custom yolov5s model and Oak D camera, i created a script that would open and close scissors when a bud is detected within 600mm of the camera.  
- attempted to trim leaves and cut buds from branches
- the scissors will not close with enough torque to remove the bud from the stem(branch). some of the leaves can be trimmed
- the servo on the end effector currently is 6kg according to yahboom specs 
- I will replace the servo motor that controls the scissors with a [25KG Metal Digital Servo](https://category.yahboom.net/products/high-torque-servo?variant=44011229511996). may try 35kg and 45kg if i need more torque.

## How will robot trim the bud with scissors?
- get distance between camera and scissors, when detected leaf matches the distance of the scissors the scissors should close, then open and repeat until leaves are not detected
- using oak d camera/yolov5, get the x,y,z coordinates of the leaves that need to be cut.
- scan bud and determine locations of leaf
- use the 'z' coordinate to create a boundary at the scissors, when the bud leaf crosses the threshold, the scissors should close.

- spatial calculation- get distance and location of bud to direct the claw holding the scissors
- use yolov5?

  



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
