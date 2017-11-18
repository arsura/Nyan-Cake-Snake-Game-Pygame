#Feature: ตรวจสอบว่างูกินแอปเปิ้ลหรือไม่ ?
#Story:
#    ในฐานะที่ฉันเป็นผู้ใช้งาน
#    ฉันต้องการตรวจสอบว่างูกินแอปเปิ้ลหรือไม่
#    เพื่อให้รู้ว่าเงื่อนไขการกินแอปเปิ้ลของฉันนั้นถูกต้อง
from eat_apple import eat_apple
# ในเกมกำหนดค่า block_size ของตัวงูเท่ากับ 20 และ apple_thickness เท่ากับ 30

#Scenario 1:
#    ให้ตำแหน่งของงูคือ 400, 300 และตัวงูมีขนาด 20x20 pixels
#    เมื่อตำแหน่งของแอปเปิ้ลคือ 400, 300 และขนาดของแอปเปิ้ลคือ 30x30 pixels
#    แล้วงูจะกินอาหารสำเร็จ

def test_eat_apple_1():
    assert eat_apple(400, 300, 400, 300, 30, 20) == True

#Scenario 2:
#    ให้ตำแหน่งของงูคือ 420, 420 และตัวงูมีขนาด 20x20 pixels
#    เมื่อตำแหน่งของแอปเปิ้ลคือ 400, 400 และขนาดของแอปเปิ้ลคือ 30x30 pixels
#    แล้วงูจะกินอาหารสำเร็จ

def test_eat_apple_2():
    assert eat_apple(420, 420, 400, 400, 30, 20) == True

#Scenario 3:
#    ให้ตำแหน่งของงูคือ 500, 400 และตัวงูมีขนาด 20x20 pixels
#    เมื่อตำแหน่งของแอปเปิ้ลคือ 480, 30 และขนาดของแอปเปิ้ลคือ 30x30 pixels
#    แล้วงูจะกินอาหารไม่สำเร็จ

def test_eat_apple_3():
    assert eat_apple(500, 400, 480, 300, 30, 20) == False

#Scenario 4:
#    ให้ตำแหน่งของงูคือ 300, 300 และตัวงูมีขนาด 20x20 pixels
#    เมื่อตำแหน่งของแอปเปิ้ลคือ 250, 240 และขนาดของแอปเปิ้ลคือ 30x30 pixels
#    แล้วงูจะกินอาหารไม่สำเร็จ

def test_eat_apple_4():
    assert eat_apple(300, 300, 250, 240, 30, 20) == False


#def eat_apple(position_x, position_y, apple_x, apple_y, apple_thickness, block_size):
#
#    return (position_x > apple_x and position_x < apple_x + apple_thickness or position_x + block_size > apple_x and position_x + block_size < apple_x + apple_thickness) and \
#           (position_y > apple_y and position_y < apple_y + apple_thickness or position_y + block_size > apple_y and position_y + block_size < apple_y + apple_thickness)
#
#assert eat_apple(500, 400, 480, 300, 30, 20) == False
#    500 > 480 and 500 < 510 or 520 > 480 and 520 < 530 and \
#    400 > 300 and [400 < 330] or 420 > 300 and [430 < 330]
