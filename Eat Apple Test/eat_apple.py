# ในเกมกำหนดค่า block_size ของตัวงูเท่ากับ 20 และ apple_thickness เท่ากับ 30

# Purpose: ตรวจสอบว่างูกินแอปเปิ้ลหรือไม่ ?
# Input:
#   ตำแหน่งของงู
#   ตำแหน่งของแอปเปิ้ล
#   ความหนาของแอปเปิ้ล
#   ขนาดของงู
# Output:
#   จริงหรือเท็จ
# Contract:
#   eat_apple(position_x, position_y, apple_x, apple_y, apple_thickness, block_size) = True or False
# Example:
#   eat_apple(400, 300, 400, 300, 30, 20) == True
#   eat_apple(420, 420, 400, 400, 30, 20) == True
#   eat_apple(500, 400, 480, 300, 30, 20) == False
#   eat_apple(300, 300, 250, 240, 30, 20) == False

def eat_apple(position_x, position_y, apple_x, apple_y, apple_thickness, block_size):

    return (position_x > apple_x and position_x < apple_x + apple_thickness or position_x + block_size > apple_x and position_x + block_size < apple_x + apple_thickness) and \
           (position_y > apple_y and position_y < apple_y + apple_thickness or position_y + block_size > apple_y and position_y + block_size < apple_y + apple_thickness)

