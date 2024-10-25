import pyrosim.pyrosim as ps

l = 3  
w = 1  
h = 1  

x = 0
y = 0
z = 0


def Create_Robot():
    ps.Start_URDF("worm_robot.urdf")
    
    # Define positions for the two body parts
    left_body_position = [x - 1.5, y, z]  
    right_body_position = [x + 1.5, y, z]  
    joint_position = [x, y, z]  # Position for the joint

   
    ps.Send_Cube(name="Left_Body", pos=left_body_position, size=[l, w, h])
    ps.Send_Cube(name="Right_Body", pos=right_body_position, size=[l, w, h]) 
    ps.Send_Joint(name="Left_Right_Joint", 
                  parent="Left_Body", 
                  child="Right_Body", 
                  type="revolute", 
                  position=joint_position)
    
    ps.End()


Create_Robot()
