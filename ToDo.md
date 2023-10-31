
- i want to recreate the motion of two human arms, one connected to a pair of scissors, the other holding a branch/bud while the scissor arm trims the leaves from the bud
******* 

- i obtained a 3d printer and will print a modified version of bnc3d moveo robot arm
- i will redesign the scissor arm to use a nema 17 stepper motor to open and close the scissors, this should provide sufficient torque and precision. 

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


- [Make Sense AI](https://www.makesense.ai/)    -browser based, no download, no install
