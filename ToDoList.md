# Actions required to create a pair of robot arms that can trim cannabis

<details>

<summary>To Do List</summary>

- mount the robot arm on a linear actuator slide rail(1000mm). Mount the slide rail to the wall vertically, it will move up and down the wall, this way the robot will be able to reach into a bin on the floor. (see linearActuatorInfo.MD)
- robot arm vertically mounted on a wall, a bin full of branches on the floor, the wall arm reaches dpwn into the bin, then moves up into position where a table with a tray and a second robot arm holding scissors will complete the trim

- The yahboom robot is tiny(18 inches tall pointing straight in the air). Approximately 12 inches of reach Can barely pick up a branch from tabletop. The branches can be more than 24 inches long. Arm needs to be able to reach into a bin and move end-effector holding branch above a tray for fan leaf removal.
- ***how to communicate between two arms and linear slide rail, one arm will move along rail and grasp branch, then move on rail again to get to position for scissor arm to complete the task 


- Create custom data sets for individual buds and branches.
- The camera will identify the branch closest to the end effector and send the coordinates to the branch arm to pick up and hold. There will be many other branches that look similar and will be close together.
  - https://shop.luxonis.com/  for cameras
  - 3d print sites
   - www.markforged.com


  - create annotation boxes for dataset 
  - https://www.cvat.ai/
  - https://github.com/heartexlabs/label-studio
  - https://github.com/heartexlabs/labelImg
  - https://github.com/scalabel/scalabel
  - https://github.com/ryouchinsa/Rectlabel-support
  - https://www.makesense.ai/    -browser based, no download, no install
  - https://github.com/ultralytics/ultralytics
  - https://www.roboflow.com
  - 
</details>
