import numpy as np
import scipy as sc


def __moves__(sigma,time_step):
    u=np.exp(sigma*np.sqrt(time_step))
    d=np.exp(np.negative(sigma)*np.sqrt(time_step))
    return [u,d]




def binomial(S,K,r,T,time_step=None,n_steps=None,u=None,d=None,sigma=None,option_type="call"):
    r = r/100
    if time_step!=None:
        n_steps = int(T/time_step)
    elif n_steps!=None:
        time_step = T/n_steps
    if u!=None and d!=None:
        pass
    elif sigma!=None:
        move=__moves__(sigma,time_step)
        u=move[0]
        d=move[1]
    
    
        

    #price tree    
    prob = (np.exp(r*time_step)-d)/(u-d)
    nodes = np.zeros([n_steps+1,n_steps+1])
    nodes[0][0]=S
    for i in range(1,n_steps+1):
        nodes[i][0]=nodes[i-1][0]*u
        nodes[i, 1:i+1] = nodes[i-1, 0:i] * d


   
    #terminal node calculation
    for i in range(n_steps+1):
        if option_type=="call":    
            nodes[-1,i]=max(nodes[-1,i]-K,0)
        elif option_type=="put":        
            nodes[-1,i]=max(K-nodes[-1,i],0)

    

    #reverse calculation
    
    for i in reversed(range(1,n_steps+1)): 
        for j in range(i):
                    nodes[i-1][j]=np.exp(-r * time_step) * (prob * nodes[i, j] + (1 - prob) * nodes[i, j+1])


    return round(nodes[0,0],2)




if __name__=="__main__":
     for i in [2,50,100,1000]:
         print(binomial(S=50,K=52,r=5,T=2,u=1.2,d=0.8,option_type="put",n_steps=i))







