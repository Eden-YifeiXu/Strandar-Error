import numpy as np
import random
from math import sqrt
population=list(range(0,10000))
n=[10,20,50,100,200,500,1000,5000]
print("Sample Size\tMean\tStandard Error")
for i in n:
    sample=random.sample(population,i)
    mean_original=np.mean(sample)
    mean_round=round(mean_original,2)

    std=np.std(sample,ddof=1)
    se_original=std/sqrt(i)
    se_round=round(se_original,2)

    print(i,"\t",mean_round,"\t",se_round)

