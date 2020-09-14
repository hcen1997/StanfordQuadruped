# this file should be some python code
# to handle http request and send msg to JoystickInterface.py

# import UDPComms
# msg = self.udp_handle.get()
# the msg from JoyStick should be like below.
# l1 r1 x :  {0,1}
# ly lx rx ry : [-1,-0.14]U[0,0]U[0.14,1]
# dpady dpadx :  {-1,0,1}
# MESSAGE_RATE = 20
# msg = {
#         "ly": left_y,
#         "lx": left_x,
#         "rx": right_x,
#         "ry": right_y,
#         "R1": R1,
#         "L1": L1,
#         "dpady": dpady,
#         "dpadx": dpadx,
#         "x": x,
#         "message_rate": MESSAGE_RATE,
#     }

#  reason for ly lx rx ry
# def deadzones(values):
#     deadzone = 0.14
#     if math.sqrt(values['left_analog_x'] ** 2 + values[
#         'left_analog_y'] ** 2) < deadzone:
#         values['left_analog_y'] = 0.0
#         values['left_analog_x'] = 0.0
#     if math.sqrt(values['right_analog_x'] ** 2 + values[
#         'right_analog_y'] ** 2) < deadzone:
#         values['right_analog_y'] = 0.0
#         values['right_analog_x'] = 0.0
#     return values
#
# for key in ["left_analog_x", "left_analog_y",
#             "right_analog_x", "right_analog_y"]:
#     new_out[key] = 2 * (new_out[key] / 255) - 1
#
# new_out = self.deadzones(new_out)
