import pandas as pd
import numpy as np
from numpy import reshape

t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list("abc"), columns=list("XYZW"))

print(t1)

