import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10 * np.pi, 1000)


flail_signal = np.sin(x) * 0.5 
plt.plot(flail_signal, label='Left_Right_Joint Signal', color='orange')
plt.legend()
plt.grid()
plt.show()
