import numpy as np, pandas as pd, os
here=os.path.dirname(__file__)
rng=np.random.default_rng(808)
N=5000
# poblacion asimetrica con media ~20 y sd ~6
k=11.111; theta=1.8
tiempo=np.round(rng.gamma(k,theta,N),3)   # mean=20, var=36
atrasado=(tiempo>24).astype(int)
d=pd.DataFrame({"id":np.arange(1,N+1),"tiempo":tiempo,"atrasado":atrasado})
d.to_csv(f"{here}/poblacion_tiempos.csv",index=False)
d.to_excel(f"{here}/poblacion_tiempos.xlsx",sheet_name="poblacion",index=False)
dic=pd.DataFrame({"variable":["id","tiempo","atrasado"],
 "descripcion":["Identificador de la observacion","Tiempo de atencion (min), poblacion asimetrica",
   "1 si el tiempo supera 24 min"],"tipo":["id","continua","binaria"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
mu=tiempo.mean(); sd=tiempo.std(ddof=0)
print("N=",N,"mu=",r(mu),"sigma=",r(sd),"p(atrasado)=",r(atrasado.mean()))
for n in [9,36,144]:
    print(f"EE teorico n={n}: {r(sd/np.sqrt(n))}")
# P(xbar>21.5) con n=36 (aprox normal)
from math import erf,sqrt
def Phi(z): return 0.5*(1+erf(z/sqrt(2)))
z=(21.5-mu)/(sd/6); print("P(xbar>21.5) n=36 ~",r(1-Phi(z)),"z=",r(z))
