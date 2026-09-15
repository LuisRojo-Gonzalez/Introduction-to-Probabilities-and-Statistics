import numpy as np, pandas as pd, os
from scipy import stats
here=os.path.dirname(__file__)
rng=np.random.default_rng(1111)
n=60
antes=np.round(rng.normal(20,4,n),2)
reduccion=rng.normal(2.5,2.0,n)
despues=np.round(antes-reduccion,2)
d=pd.DataFrame({"lote_id":np.arange(1,n+1),"tiempo_antes":antes,"tiempo_despues":despues})
d["d_reduccion"]=np.round(d.tiempo_antes-d.tiempo_despues,2)
d.to_csv(f"{here}/mejora_piloto.csv",index=False)
d.to_excel(f"{here}/mejora_piloto.xlsx",sheet_name="mejora",index=False)
dic=pd.DataFrame({"variable":["lote_id","tiempo_antes","tiempo_despues","d_reduccion"],
 "descripcion":["Identificador del lote (mismo lote antes y despues)","Tiempo antes de la mejora (min)",
   "Tiempo despues de la mejora (min)","Reduccion = antes - despues (min)"],
 "tipo":["id","continua","continua","continua"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
dd=d.d_reduccion
print("n=",n,"mean_d=",r(dd.mean()),"sd_d=",r(dd.std(ddof=1)))
t0=(dd.mean()-0)/(dd.std(ddof=1)/np.sqrt(n)); print("t (mu0=0)=",r(t0),"p_unilat=",r(1-stats.t.cdf(t0,n-1)))
t2=(dd.mean()-2)/(dd.std(ddof=1)/np.sqrt(n)); print("t (mu0=2)=",r(t2),"p_unilat=",r(1-stats.t.cdf(t2,n-1)))
tc=stats.t.ppf(0.975,n-1); lo=dd.mean()-tc*dd.std(ddof=1)/np.sqrt(n); hi=dd.mean()+tc*dd.std(ddof=1)/np.sqrt(n)
print("IC95 mu_d=",(r(lo),r(hi)),"dz=",r(dd.mean()/dd.std(ddof=1)))
