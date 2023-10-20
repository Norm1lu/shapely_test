import os
from HitbotInterface import HitbotInterface
import time
import codecs
import libscrc
import binascii
import struct
import numpy as np

# id of robot arm decided by its product id
robot_id = 190
robot = HitbotInterface(robot_id)
# initial the connection through the shared library
lib_folder = "./python/lib"
robot.net_port_initial(lib_folder)
ret = robot.initial(1, 240)
robot.com485_initial(115200)
# check if the robot is connected
ret = robot.is_connect()
while ret != 1:
    time.sleep(0.1)
    ret = robot.is_connect()
print("The scara arm is connected!")
# robot.joint_home(4)
# check the joint state
# joint1_state = robot.check_joint(1, False)
# joint2_state = robot.check_joint(2, False)
# joint3_state = robot.check_joint(3, False)
# joint4_state = robot.check_joint(4, False)
# print("joint 1 state: ", joint1_state)
# print("joint 2 state: ", joint2_state)
# print("joint 3 state: ", joint3_state)
# print("joint 4 state: ", joint4_state)

# # arm motion control
# robot.set_allow_distance_at_target_position(0.1, 0.1, 0.1, 0.1)


# check the control of the e-claw
# make sure the e-claw is connected to the scara arm
return_state=robot.new_movej_xyz_lr(180.77, 63.74, -34, 100, 70, 0, 1)
print(return_state)
robot.wait_stop()
time.sleep(5)
robot.new_movej_xyz_lr(220, 60, -34, 30, 100, 0.4, 1)
robot.wait_stop()
time.sleep(5)
robot.new_movej_xyz_lr(121.8, 60, -34, 0, 120, 0.4, 1)
robot.wait_stop()
close = b"\x01\x10\x00\x02\x00\x02\x04\x00\x00\x00\x00\x72\x76"
open = b"\x01\x10\x00\x02\x00\x02\x04\x41\xA0\x00\x00\x66\x68"


# print("start_time:  ", start_time)
move_dis_cmd = b"\x01\x10\x00\x02\x00\x02\x04"
move_dis = 10.00
str = struct.pack(">f", move_dis)
# print('length: ', len(str))         # length:  8
move_dis_cmd += str
# print(move_dis_cmd)
command_crc = libscrc.modbus(move_dis_cmd).to_bytes(2, "little")
move_dis_cmd += command_crc
print(move_dis_cmd)
start_time = time.perf_counter()
robot.com485_send(move_dis_cmd, 13)
stop_time = time.perf_counter()
# print("stop_time:  ", stop_time)
run_time = stop_time - start_time
print("running_time:  ", run_time)

# robot.new_movej_xyz_lr(-39.34, -374, -5, -159.75, 120, 0, -1)
robot.wait_stop()
move_dis_cmd = b"\x01\x10\x00\x02\x00\x02\x04"
move_dis = 20.00
str = struct.pack(">f", move_dis)
# print('length: ', len(str))         # length:  8
move_dis_cmd += str
# print(move_dis_cmd)
command_crc = libscrc.modbus(move_dis_cmd).to_bytes(2, "little")
move_dis_cmd += command_crc
print(move_dis_cmd)
robot.com485_send(move_dis_cmd, 13)
# return_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'
return_bytes = 0
return_length = 8

# robot.com485_recv(return_bytes)
# print("return: ", return_bytes)


# print("set speed")
# ret=robot.com485_send(v_cmd,13)
# time.sleep(1)

# print("close the claw")
# ret=robot.com485_send(close,13)


# print("open the claw")
# ret=robot.com485_send(open,13)
