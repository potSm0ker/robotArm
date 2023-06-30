# Robotic Arm Yahboom 6DOF with Jetson Nano 4gb

<details>

<summary> ***30,000 foot goal.*** Create a pair of electric robotic arms that can trim cannabis </summary>

Create a pair of electric robotic arms that can **automatically** trim dried cannabis flowers using a standard pair of trimming scissors. The arm uses servo motors to rotate the joints. For vision- open cv or other methods of object detection using camera. The arm will be able to grasp (using a two fingered-claw) a branch or bud from a bin full of branches, then hold the branch while a second arm with scissors attached (to the claw) will trim the buds. The finished buds will be dropped into a bucket when complete. **The target goal is to trim 1 pound of cannabis in 8 hours time.** The average human trimmer would trim for about 7.2 hours in a standard work day, 1 pound would be the expected minimum. 2 pounds would be a high amount for a human trimmer in a standard 8 hour work day.

</details>

I am using a Yahboom DOFBOT Robotic Arm with ROS and Jetson NANO 4GB(B01/SUB) purchased from [amazon.com](https://www.amazon.com/Yahboom-Controlled-Programmable-Robotics-Identity/dp/B09T96PS3S/ref=asc_df_B09T96PS3S/?tag=hyprod-20&linkCode=df0&hvadid=647177154660&hvpos=&hvnetw=g&hvrand=9522090457653424090&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9029977&hvtargid=pla-1948863623457&psc=1&gclid=CjwKCAjw-vmkBhBMEiwAlrMeF-Z9-dOB8Xg7fpWzmVdcTm2_Ga3R2E9iPS-FwKbWelSRKJymOayAkxoCRlYQAvD_BwE)
The official documentation/code for the arm is @ [6DOFBot-jetson_nano on github](https://github.com/YahboomTechnology/dofbot-jetson_nano.git)

- Here is a link  to a [YouTube playlist](https://www.youtube.com/playlist?list=PLcbaYozXcpF65uUvdCmepFYYjx4FZ4Iwq), these videos have info that may assist in completing the goal.
I will store the info I find useful in this repository. Some code maybe generated by chat-gpt or similar methods.

### See productExamples folder for visual definition of bud, branch, fan leaf and other items.

<details>

<summary> ****The pair of robot arms should do the following:**** </summary>

- trim = remove all fan leaves (see assets for product example photos)

- Able to grasp a branch or bud with pincer-type end effector(2 finger claw)

- Able to open and close a pair of standard trimming scissors, which will be securely attached to end effector(claw). Scissors will be detachable from claw for cleaning.

- Able to identify a single branch or bud in a bin full of similar items.

- Will need camera for object detection. 
    - using open-cv or other methods. python or c++ maybe used.
    - Yolo v5 is compatible with jetson nano.
- Able to work together as a pair of arms, one will hold the scissors(scissor arm), the other will hold a branch/bud(branch arm).

- Branch arm able to identify fan leaves on bud and coordinate with scissor arm to remove all fan leaves.

- Branch arm able to rotate the bud/branch while scissor arm opens and closes scissors to complete trim.

</details>

<details>

<summary>My 6-Degree Of Freedom(DOF) yahboom with jetson nano 4gb robotic arm system:</summary>

- Operating System: Ubuntu 18  64bit
- rosdistro: melodic
- rosversion: 1.14.13
- Im using a 17" HDMI monitor, wireless keyboard and mouse plugged into USB on the Jetson Nano, which is plugged into yahboom control board. Use the terminal to run python scripts directly on the robot. This is the easiest way and gives the user complete control over the robot.

</details>

<details>

<summary>Here are the ROS versions supported by Ubuntu:</summary>

- Ubuntu 16.04 / ROS Kinetic
- Ubuntu 18.04 / ROS Melodic
- Ubuntu 20.04 / ROS Noetic

</details>




