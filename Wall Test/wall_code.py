# The size of snake is 20x20 pixels
# Purpose: ตรวจสอบว่าเมื่องูวิ่งชนกำแพง งูจะตายหรือไม่ ?
# Input:
#   ขนาดของหน้าจอซึ่งเท่ากับ 800, 600
#   ตำแหน่งของงู
# Output:
#   จริงหรือเท็จ
# Contract:
#   wall_of_dead(position_x, position_y, display_width, display_height) = True or False
# Example:
#   wall_of_dead(100, 0, 800, 600) == True
#   wall_of_dead(100, 600, 800, 600) == True
#   wall_of_dead(600, 300, 800, 600) == False

def wall_of_dead(position_x, position_y, display_width, display_height):

    return position_x >= display_width-20 or \
           position_x <= 0 or \
           position_y >= display_height-20 or \
           position_y <= 20

