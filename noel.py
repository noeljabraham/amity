# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:28:07 2023
@author: AVITA
""" 
import math
import random
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
workbook = openpyxl.Workbook()
worksheet = workbook.active

PD1=[0.7,0.8,0.7]
PD2=[0.5,0.5,0.5]
PD3=[0.95,0.9,0.9]
PD4=[0.6,0.6,0.02]
PD5=[0.6,0.9,0.6]
PD6=[0.02,0.02,0.02]
PD7=[0.99,0.9,0.9]
PD8=[0.02,0.02,0.9]
PD9=[0.9,0.9,0.8]
tD1=[20,120,40]
tD2=[90,90,20]
tD3=[18,45,90]
tD4=[80,80,300]
tD5=[96,27,20]
tD6=[20,20,80]
tD7=[127,20,20]
tD8=[15,15,27]
tD9=[50,50,50]
tD_STD=0.3
timemean=300
time_sd=timemean*tD_STD
f = open ("CODE_II_Output.txt","w")

# Create a list to store all the values
output_values = []

# Initialize a list to store PI values
PI_values = []
i = 0
while i < 1000:
    i = i + 1
 
    # selection of PD in layer 1
    isum = 0
    PDL1 = [(1 - PD1[0]), (1 - PD1[1]), (1 - PD1[2])]
    PDL1sum = sum(PDL1, isum)
    probpe1 = PDL1[0] / PDL1sum
    probpe2 = PDL1[1] / PDL1sum
    probpe3 = PDL1[2] / PDL1sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD1[0] = PD1[1]
            PD1[0] = norm.ppf(rand_num, PD1[0], 0.1 * PD1[0])
            tD1[0] = tD1[1]
        elif rand_num > (probpe1 + probpe2):
            PD1[0] = PD1[2]
            PD1[0] = norm.ppf(rand_num, PD1[0], 0.1 * PD1[0])
            tD1[0] = tD1[2]
        else:
            PD1[0] = norm.ppf(rand_num, PD1[0], 0.1 * PD1[0])
    
    # selection of PD in layer 2
    isum = 0
    PDL2 = [(1 - PD2[0]), (1 - PD2[1]), (1 - PD2[2])]
    PDL2sum = sum(PDL2, isum)
    probpe1 = PDL2[0] / PDL2sum
    probpe2 = PDL2[1] / PDL2sum
    probpe3 = PDL2[2] / PDL2sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD2[0] = PD2[1]
            PD2[0] = norm.ppf(rand_num, PD2[0], 0.1 * PD2[0])
            tD2[0] = tD2[1]
        elif rand_num > (probpe1 + probpe2):
            PD2[0] = PD2[2]
            PD2[0] = norm.ppf(rand_num, PD2[0], 0.1 * PD2[0])
            tD2[0] = tD2[2]
        else:
            PD2[0] = norm.ppf(rand_num, PD2[0], 0.1 * PD2[0])
    
    # selection of PD in layer 3
    isum = 0
    PDL3 = [(1 - PD3[0]), (1 - PD3[1]), (1 - PD3[2])]
    PDL3sum = sum(PDL3, isum)
    probpe1 = PDL3[0] / PDL3sum
    probpe2 = PDL3[1] / PDL3sum
    probpe3 = PDL3[2] / PDL3sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD3[0] = PD3[1]
            PD3[0] = norm.ppf(rand_num, PD3[0], 0.1 * PD3[0])
            tD3[0] = tD3[1]
        elif rand_num > (probpe1 + probpe2):
            PD3[0] = PD3[2]
            PD3[0] = norm.ppf(rand_num, PD3[0], 0.1 * PD3[0])
            tD3[0] = tD3[2]
        else:
            PD3[0] = norm.ppf(rand_num, PD3[0], 0.1 * PD3[0])
    
    # selection of PD in layer 4
    isum = 0
    PDL4 = [(1 - PD4[0]), (1 - PD4[1]), (1 - PD4[2])]
    PDL4sum = sum(PDL4, isum)
    probpe1 = PDL4[0] / PDL4sum
    probpe2 = PDL4[1] / PDL4sum
    probpe3 = PDL4[2] / PDL4sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD4[0] = PD4[1]
            PD4[0] = norm.ppf(rand_num, PD4[0], 0.1 * PD4[0])
            tD4[0] = tD4[1]
        elif rand_num > (probpe1 + probpe2):
            PD4[0] = PD4[2]
            PD4[0] = norm.ppf(rand_num, PD4[0], 0.1 * PD4[0])
            tD4[0] = tD4[2]
        else:
            PD4[0] = norm.ppf(rand_num, PD4[0], 0.1 * PD4[0])
     
    # selection of PD in layer 5
    isum = 0
    PDL5 = [(1 - PD5[0]), (1 - PD5[1]), (1 - PD5[2])]
    PDL5sum = sum(PDL5, isum)
    probpe1 = PDL5[0] / PDL5sum
    probpe2 = PDL5[1] / PDL5sum
    probpe3 = PDL5[2] / PDL5sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD5[0] = PD5[1]
            PD5[0] = norm.ppf(rand_num, PD5[0], 0.1 * PD5[0])
            tD5[0] = tD5[1]
        elif rand_num > (probpe1 + probpe2):
            PD5[0] = PD5[2]
            PD5[0] = norm.ppf(rand_num, PD5[0], 0.1 * PD5[0])
            tD5[0] = tD5[2]
        else:
            PD5[0] = norm.ppf(rand_num, PD5[0], 0.1 * PD5[0])
    
    # selection of PD in layer 6
    isum = 0
    PDL6 = [(1 - PD6[0]), (1 - PD6[1]), (1 - PD6[2])]
    PDL6sum = sum(PDL6, isum)
    probpe1 = PDL6[0] / PDL6sum
    probpe2 = PDL6[1] / PDL6sum
    probpe3 = PDL6[2] / PDL6sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD6[0] = PD6[1]
            PD6[0] = norm.ppf(rand_num, PD6[0], 0.1 * PD6[0])
            tD6[0] = tD6[1]
        elif rand_num > (probpe1 + probpe2):
            PD6[0] = PD6[2]
            PD6[0] = norm.ppf(rand_num, PD6[0], 0.1 * PD6[0])
            tD6[0] = tD6[2]
        else:
            PD6[0] = norm.ppf(rand_num, PD6[0], 0.1 * PD6[0])
    
    # selection of PD in layer 7
    isum = 0
    PDL7 = [(1 - PD7[0]), (1 - PD7[1]), (1 - PD7[2])]
    PDL7sum = sum(PDL7, isum)
    probpe1 = PDL7[0] / PDL7sum
    probpe2 = PDL7[1] / PDL7sum
    probpe3 = PDL7[2] / PDL7sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD7[0] = PD7[1]
            PD7[0] = norm.ppf(rand_num, PD7[0], 0.1 * PD7[0])
            tD7[0] = tD7[1]
        elif rand_num > (probpe1 + probpe2):
            PD7[0] = PD7[2]
            PD7[0] = norm.ppf(rand_num, PD7[0], 0.1 * PD7[0])
            tD7[0] = tD7[2]
        else:
            PD7[0] = norm.ppf(rand_num, PD7[0], 0.1 * PD7[0])
    
    # selection of PD in layer 8
    isum = 0
    PDL8 = [(1 - PD8[0]), (1 - PD8[1]), (1 - PD8[2])]
    PDL8sum = sum(PDL8, isum)
    probpe1 = PDL8[0] / PDL8sum
    probpe2 = PDL8[1] / PDL8sum
    probpe3 = PDL8[2] / PDL8sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD8[0] = PD8[1]
            PD8[0] = norm.ppf(rand_num, PD8[0], 0.1 * PD8[0])
            tD8[0] = tD8[1]
        elif rand_num > (probpe1 + probpe2):
            PD8[0] = PD8[2]
            PD8[0] = norm.ppf(rand_num, PD8[0], 0.1 * PD8[0])
            tD8[0] = tD8[2]
        else:
            PD8[0] = norm.ppf(rand_num, PD8[0], 0.1 * PD8[0])
    
    # selection of PD in layer 9
    isum = 0
    PDL9 = [(1 - PD9[0]), (1 - PD9[1]), (1 - PD9[2])]
    PDL9sum = sum(PDL9, isum)
    probpe1 = PDL9[0] / PDL9sum
    probpe2 = PDL9[1] / PDL9sum
    probpe3 = PDL9[2] / PDL9sum
    rand_num = random.random()
    if rand_num > probpe1:
        if rand_num < (probpe1 + probpe2):
            PD9[0] = PD9[1]
            PD9[0] = norm.ppf(rand_num, PD9[0], 0.1 * PD9[0])
            tD9[0] = tD9[1]
        elif rand_num > (probpe1 + probpe2):
            PD9[0] = PD9[2]
            PD9[0] = norm.ppf(rand_num, PD9[0], 0.1 * PD9[0])
            tD9[0] = tD9[2]
        else:
            PD9[0] = norm.ppf(rand_num, PD9[0], 0.1 * PD9[0])
    
    # Print PD values
    print("The PD Values are:",PD1[0], PD2[0], PD3[0], PD4[0], PD5[0], PD6[0], PD7[0], PD8[0], PD9[0])
    
    # Print tD values
    print("The TD Values are:",tD1[0], tD2[0], tD3[0], tD4[0], tD5[0], tD6[0], tD7[0], tD8[0], tD9[0])
    
    # Calculate sd values
    sd1 = tD1[0] * tD_STD
    sd2 = tD2[0] * tD_STD
    sd3 = tD3[0] * tD_STD
    sd4 = tD4[0] * tD_STD
    sd5 = tD5[0] * tD_STD
    sd6 = tD6[0] * tD_STD
    sd7 = tD7[0] * tD_STD
    sd8 = tD8[0] * tD_STD
    sd9 = tD9[0] * tD_STD
    
    # Calculate pndet values
    pndet1 = 1 - PD1[0]
    pndet2 = (1 - PD2[0]) * pndet1
    pndet3 = (1 - PD3[0]) * pndet2
    pndet4 = (1 - PD4[0]) * pndet3
    pndet5 = (1 - PD5[0]) * pndet4
    pndet6 = (1 - PD6[0]) * pndet5
    pndet7 = (1 - PD7[0]) * pndet6
    pndet8 = (1 - PD8[0]) * pndet7
    pndet9 = (1 - PD9[0]) * pndet8
    
    # Calculate pfirst values
    pfirst1 = PD1[0]
    pfirst2 = PD2[0] * pndet1
    pfirst3 = PD3[0] * pndet2
    pfirst4 = PD4[0] * pndet3
    pfirst5 = PD5[0] * pndet4
    pfirst6 = PD6[0] * pndet5
    pfirst7 = PD7[0] * pndet6
    pfirst8 = PD8[0] * pndet7
    pfirst9 = PD9[0] * pndet8
    
    # Calculate cumd and cumv values
    cumd9 = tD9[0]
    cumd8 = tD8[0] + cumd9
    cumd7 = tD7[0] + cumd8
    cumd6 = tD6[0] + cumd7
    cumd5 = tD5[0] + cumd6
    cumd4 = tD4[0] + cumd5
    cumd3 = tD3[0] + cumd4
    cumd2 = tD2[0] + cumd3
    cumd1 = tD1[0] + cumd2
    cumv9 = sd9 * sd9
    cumv8 = cumv9 + (sd8 * sd8)
    cumv7 = cumv8 + (sd7 * sd7)
    cumv6 = cumv7 + (sd6 * sd6)
    cumv5 = cumv6 + (sd5 * sd5)
    cumv4 = cumv5 + (sd4 * sd4)
    cumv3 = cumv4 + (sd3 * sd3)
    cumv2 = cumv3 + (sd2 * sd2)
    cumv1 = cumv2 + (sd1 * sd1)
    
    # Calculate truecdm and truecv values
    truecdm9 = 1.0 * tD9[0]
    truecdm8 = (0.5 * tD8[0]) + cumd9
    truecdm7 = (1.0 * tD7[0]) + cumd8
    truecdm6 = (0.5 * tD6[0]) + cumd7
    truecdm5 = (0.5 * tD5[0]) + cumd6
    truecdm4 = (0.5 * tD4[0]) + cumd5
    truecdm3 = (0.5 * tD3[0]) + cumd4
    truecdm2 = (0.5 * tD2[0]) + cumd3
    truecdm1 = (1.0 * tD1[0]) + cumd2
    truecv9 = 1.0 * sd9 * 1.0 * sd9
    truecv8 = (0.5 * sd8 * 0.5 * sd8) + cumv9
    truecv7 = (1.0 * sd7 * 1.0 * sd7) + cumv8
    truecv6 = (0.5 * sd6 * 0.5 * sd6) + cumv7
    truecv5 = (0.5 * sd5 * 0.5 * sd5) + cumv6
    truecv4 = (0.5 * sd4 * 0.5 * sd4) + cumv5
    truecv3 = (0.5 * sd3 * 0.5 * sd3) + cumv4
    truecv2 = (0.5 * sd2 * 0.5 * sd2) + cumv3
    truecv1 = (1.0 * sd1 * 1.0 * sd1) + cumv2
    
    # Calculate sq values
    sq9 = math.sqrt(truecv9 + (time_sd * time_sd))
    sq8 = math.sqrt(truecv8 + (time_sd * time_sd))
    sq7 = math.sqrt(truecv7 + (time_sd * time_sd))
    sq6 = math.sqrt(truecv6 + (time_sd * time_sd))
    sq5 = math.sqrt(truecv5 + (time_sd * time_sd))
    sq4 = math.sqrt(truecv4 + (time_sd * time_sd))
    sq3 = math.sqrt(truecv3 + (time_sd * time_sd))
    sq2 = math.sqrt(truecv2 + (time_sd * time_sd))
    sq1 = math.sqrt(truecv1 + (time_sd * time_sd))
    
    # Calculate zv values
    zv1 = ((truecdm1 - timemean) / sq1)
    zv2 = ((truecdm2 - timemean) / sq2)
    zv3 = ((truecdm3 - timemean) / sq3)
    zv4 = ((truecdm4 - timemean) / sq4)
    zv5 = ((truecdm5 - timemean) / sq5)
    zv6 = ((truecdm6 - timemean) / sq6)
    zv7 = ((truecdm7 - timemean) / sq7)
    zv8 = ((truecdm8 - timemean) / sq8)
    zv9 = ((truecdm9 - timemean) / sq9)
    
    # Calculate prob values using the cumulative distribution function
    prob1 = norm.cdf(zv1)
    prob2 = norm.cdf(zv2)
    prob3 = norm.cdf(zv3)
    prob4 = norm.cdf(zv4)
    prob5 = norm.cdf(zv5)
    prob6 = norm.cdf(zv6)
    prob7 = norm.cdf(zv7)
    prob8 = norm.cdf(zv8)
    prob9 = norm.cdf(zv9)
    
    # Calculate pnormal values
    pnormal1 = pfirst1 * prob1
    pnormal2 = pfirst2 * prob2
    pnormal3 = pfirst3 * prob3
    pnormal4 = pfirst4 * prob4
    pnormal5 = pfirst5 * prob5
    pnormal6 = pfirst6 * prob6
    pnormal7 = pfirst7 * prob7
    pnormal8 = pfirst8 * prob8
    pnormal9 = pfirst9 * prob9

 # Calculate PI (the final result)
    PI = pnormal1 + pnormal2 + pnormal3 + pnormal4 + pnormal5 + pnormal6 + pnormal7 + pnormal8 + pnormal9
    PI_values.append(PI)

    # Append PD and TD values to the output_values list
    output_values.append([PD1[0], PD2[0], PD3[0], PD4[0], PD5[0], PD6[0], PD7[0], PD8[0], PD9[0],
                          tD1[0], tD2[0], tD3[0], tD4[0], tD5[0], tD6[0], tD7[0], tD8[0], tD9[0]])

# Print the first 1000 PI values as an example
if len(PI_values) <= 1000:
    print("First 1000 PI values:\n", PI_values)
else:
    print("First 1000 PI values:\n", PI_values[:1000])

# Write all values to the output.txt file
with open('output.txt', 'w') as f:
    for i in range(len(output_values)):
        f.write(f"PD Values: {', '.join(map(str, output_values[i][:9]))}\n")
        f.write(f"TD Values: {', '.join(map(str, output_values[i][9:]))}\n")
        f.write(format(PI_values[i], '.8f'))
        f.write("\n")

# Create a histogram for all PI values
plt.hist(PI_values, bins=500, alpha=0.5, edgecolor='m')

# Customize the plot (optional)
plt.title('Probability of Interruption')
plt.xlabel('PI')
plt.ylabel('Frequency')

# Display the plot
plt.show()

