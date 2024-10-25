import pybullet as p
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time
import matplotlib.pyplot as plt
if not p.isConnected():
    physicsClient = p.connect(p.GUI)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("worm_robot.urdf", [0, 0, 0.5], p.getQuaternionFromEuler([0, 0, 0]))  # Adjust height to lie on the ground


duration = 100000 
ps.Prepare_To_Simulate(robotId)

x = np.linspace(0, 100 * np.pi, 10000)
flail_signal = np.sin(x) * 0.5 
# plt.plot(flail_signal, label='Left_Right_Joint Signal', color='orange')
# plt.legend()
# plt.grid()
# plt.show()

for i in range(duration):
    
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName=b'Left_Right_Joint', 
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=flail_signal[i],  
                           maxForce=500)

    p.stepSimulation()
    time.sleep(1 / 240)  


p.disconnect()