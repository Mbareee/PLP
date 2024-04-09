# minimum dimensions 
#import numpy as np 
#a = np.array([1, 2, 3,4,5], ndmin = 6) 
#print(a)

# import numpy as np
#a = np.arange(0,60,5)
#a = a.reshape(3,4)
#print('Original array is:')
#print(a)
#print('\n')
#print('Modified array is:')
#for x in np.nditer(a):
 #  print(x)


#import numpy as np 
#a = np.arange(0,60,5) 
#a = a.reshape(3,4) 
#print('Original array is:')
#print(a)
#print('\n')
#print('Transpose of the original array is:')
#b = a.T 
#print(b) 
#print('\n')  
#print ('Modified array is:')
#for x in np.nditer(b): 
#   print(x)


#import pandas as pd
#import numpy as np

#df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
#for row_index,row in df.iterrows():
#   print(row_index,row)


#from matplotlib import pyplot as plt
#import numpy as np
#import math #needed for definition of pi
#x = np.arange(0, math.pi*2, 0.05)
#y = np.sin(x)
#plt.plot(x,y)
#plt.xlabel("angle")
#plt.ylabel("sine")
#plt.title('sine wave')
#plt.show()

phi = (1 + (5)**0.5) / 2
print(int((phi**2 - (1-phi)**2) / (5)**0.5))

