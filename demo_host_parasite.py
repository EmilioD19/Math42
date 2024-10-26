
#%% Logistic growth of population x(n) = (1 + r)*x(n-1), where r = R*(1 - x(n-1)/K) 


# Import packages
import pandas as pd
import matplotlib.pyplot as plt


#%% Parameters
 
R = 1   # Intrinsic growth rate of host population
K = 100 # Carrying capacity of host population
Q = 0.02 # efficiency of converting prey for predator's reproduction
C = 0.01 # Predator's efficiency


#%% Pre-loop

N0 = 50 # Initial host population
P0 = 0.2 # Initial parasite population

N_generation = 50 # number of generations that we track

data = [] # initialize a empty list to store rows

row = {"Time" : 0, 
       "Host" : N0, 
       "Parasite" : P0}  

data.append(row) # Save the initial values


#%% Looping over years

N = N0 # Initialize host population (variable) by its initial value

P = P0 # Initialize parasite population (variable) by its initial value

for k in range(1,N_generation):
    
    # Logistic growth rate of host population
    r = R*(1 - N0/K)
    
    # Update host population 
    N = (1. + r)*N0 - C*P0*N0
    
    # Update parasite population
    P = Q*P0*N0
    
    # Save current solution for next iteration
    N0, P0 = N, P
    
    # Save data 
    row = {"Time" : k, 
           "Host" : N, 
           "Parasite" : P}    
    data.append(row)
    

## Aggregate the collected rows in a dataframe structure
df = pd.DataFrame(data)


#%% Plot

fig, ax = plt.subplots(1,1, dpi=400)
ax.plot(df["Time"], df["Host"], "-o", markersize=3, label="Host")
ax.plot(df["Time"], df["Parasite"], "--s", markersize=3, label="Parasite")
ax.set_xlabel("Time (number of generation)", fontsize=15)
ax.set_ylabel("Population", fontsize=15)
# ax.set_yticks([0,K], ["0", "K=%s"%K])
plt.legend(fontsize=15)
plt.grid(visible=True, alpha=0.2)


#%% Save results as csv file named "logistic.csv"

## uncomment below to save
# df.to_csv("logistic.csv")