import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('test.csv')
#print(df)
#print(df.describe())
df.plot()
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
