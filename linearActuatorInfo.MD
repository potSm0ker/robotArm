## info is specific to this particular project, maybe used for other projects
- Needed for this project- slide rail(linear actuator lead screw) with a length of at least, 1000mm (3 feet), to increase reach of the robotic arm
- will be mounted vertically on a wall, with robot arm attached to slide rail on a plate.
-  lead screw-driven actuators with slide rail
- nema23 stepper motor connect to jetson nano
- Digital Stepper Driver 1.0-4.5A 18-50VDC for Nema 17, 23, 24 Stepper Motor $17.88
- for connection  USB to TTL Serial Cable or FTDI Serial TTL-232 USB Cable

 - Connect the motor driver to the Jetson Nano: usb to ttl cable. The motor driver will typically use digital input pins to receive control signals from the Jetson Nano. 


- websites
 - https://openbuildspartstore.com/
 - [How to Implement a Linear Stage With Raspberry Pi](https://www.digikey.com/en/articles/easy-build-how-to-implement-linear-stage-raspberry-pi-project)


### commercially available slide rails some assembly required

- [how to assemble slide rail from open build part store](https://www.youtube.com/watch?v=56RIplHaoQs&list=PLDeI80MYQtbqZahZvCIcOPhE0wO3RirvY)
- [OpenBuilds C-Beam Linear Actuator Lead Screw 1500mm](https://openbuildspartstore.com/c-beam-tension-xl-linear-actuator-bundle/) $261.97
- [nema 23 motor + controller with usb to ttl](https://excitron.com/secure/?itemid=585&set=x57-40m--nema23-controller-57mm-motor-kit-usb-cables-free-usa-shipping) $279.00 

- ## stepper motor drivers
- www.teknic.com
- [top choice - clear path motors](https://teknic.com/products/clearpath-brushless-dc-servo-motors/clearpath-sc/)
- [clear path motors youtube](https://www.youtube.com/watch?v=1S7etlhbuFY&list=PLuMmdjFz-3nzWAxdQWN__v9P9fYJkGCvS&index=2)
- [connect clear path motor  to arduino](https://www.youtube.com/watch?v=QZLwDnGSaeI&list=PLuMmdjFz-3nzWAxdQWN__v9P9fYJkGCvS&index=8)



 - [RTELLIGENT Nema 23 Stepper Closed Loop Servo Motor and Driver Kit 2 Phase 3.0NM(425 oz.in) with Encoder](https://www.amazon.com/RTELLIGENT-Stepper-Closed-57X57X119mm-Encoder/dp/B07ZLQL83N/ref=sr_1_16?content-id=amzn1.sym.9575273b-ecd8-4648-9bf0-15f20c657e0a&keywords=nema+23+stepper&pd_rd_r=bfd3c184-d4d5-492a-8843-20988e0a515b&pd_rd_w=0mXHf&pd_rd_wg=SttJW&pf_rd_p=9575273b-ecd8-4648-9bf0-15f20c657e0a&pf_rd_r=K38DQX35GG332E2PR5KC&qid=1688186884&sr=8-16)

 - [CNC Digital Microstep driver DM542 Stepper Motor Controller 2-phase Digital Stepper Motor Driver 20-50V DC Max 4.2A](https://www.amazon.com/Digital-Microstep-Stepper-Controller-2-phase/dp/B08GCFNQF2/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.6fd80408-71b6-44da-b059-082bba9089d3%3Aamzn1.sym.6fd80408-71b6-44da-b059-082bba9089d3&cv_ct_cx=nema+23+stepper&keywords=nema+23+stepper&pd_rd_i=B08GCFNQF2&pd_rd_r=29181c76-2db0-49b8-8353-6f936e6dc7a0&pd_rd_w=rbVwI&pd_rd_wg=F9XlV&pf_rd_p=6fd80408-71b6-44da-b059-082bba9089d3&pf_rd_r=ZPWCRPGR3PRTQTPX5NXZ&qid=1688186884&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-2-364cf978-ce2a-480a-9bb0-bdb96faa0f61-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1)

 - [STEPPERONLINE 1 Axis CNC Kit 3Nm(425oz.in) Nema 23 Stepper Motor & Driver](https://www.amazon.com/STEPPERONLINE-425oz-Stepper-Driver-Router/dp/B012QFRKAO/ref=sr_1_13?content-id=amzn1.sym.9575273b-ecd8-4648-9bf0-15f20c657e0a&keywords=nema+23+stepper&pd_rd_r=bfd3c184-d4d5-492a-8843-20988e0a515b&pd_rd_w=0mXHf&pd_rd_wg=SttJW&pf_rd_p=9575273b-ecd8-4648-9bf0-15f20c657e0a&pf_rd_r=K38DQX35GG332E2PR5KC&qid=1688186884&sr=8-13)

## power supply
- [DROK 36V Power Supply, AC 110V 220V to DC 0-36V 4A 150W Buck Converter](https://www.amazon.com/DROK-110V-220V-Converter-Adjustable-Transformer/dp/B0B18P6GKP/ref=pd_bxgy_img_sccl_1/144-0992491-2847419?pd_rd_w=euEJc&content-id=amzn1.sym.26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_p=26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_r=DA95T8K3B88VGM8KP0CK&pd_rd_wg=j6OPN&pd_rd_r=5d22f0ba-b30d-463b-868a-309cf0a6b8ec&pd_rd_i=B08GFQZFC1&th=1)

### Found diy video and parts list


[DIY slide rail assembly youtube](https://www.youtube.com/watch?v=bwkWi0-p5mU)
- parts list for a DIY linear rail
 - Aluminium profile T-Slot 30cm
 - Aluminium profile T-Slot 5cm
 - Linear guide rail MGN12H 30cm
 - T8 2mm pitch lead screw 30cm & anti backlash nut
 - NEMA 17HS8401 stepper motor
 - NEMA 17 fixed mount bracket
 - 5-8mm flexible coupler
 - M3 Female2male brass screw thread PCB stand
 - M5 hex screw + nut + flat washer
 - M3 hex screw + nut
 - Zip ties

 [mini jetson nano car](https://medium.com/@anandmohan_8991/jetbot-using-l298n-pwm-motor-a6556ed358d6)
