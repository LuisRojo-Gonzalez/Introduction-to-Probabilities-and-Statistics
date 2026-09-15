import numpy as np, pandas as pd, os
from scipy import stats
here=os.path.dirname(__file__)
rng=np.random.default_rng(909)
n=200
tiempo=np.round(rng.normal(32,7,n),2)
a_tiempo=(rng.random(n)<0.88).astype(int)
error_doc=(rng.random(n)<0.07).astype(int)
turno=rng.choice(["Dia","Noche"],n,p=[0.55,0.45])
d=pd.DataFrame({"orden_id":np.arange(1,n+1),"turno":turno,"tiempo_armado":tiempo,
   "a_tiempo":a_tiempo,"error_doc":error_doc})
d.to_csv(f"{here}/armado_piloto.csv",index=False)
d.to_excel(f"{here}/armado_piloto.xlsx",sheet_name="armado",index=False)
dic=pd.DataFrame({"variable":["orden_id","turno","tiempo_armado","a_tiempo","error_doc"],
 "descripcion":["Identificador de la orden","Turno (Dia/Noche)","Tiempo de armado (min)",
   "1 si la orden se completo a tiempo","1 si la orden tuvo error de documentacion"],
 "tipo":["id","categorica","continua","binaria","binaria"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
xbar=d.tiempo_armado.mean(); s=d.tiempo_armado.std(ddof=1)
tcrit=stats.t.ppf(0.975,n-1)
lo=xbar-tcrit*s/np.sqrt(n); hi=xbar+tcrit*s/np.sqrt(n)
print("n=",n,"xbar=",r(xbar),"s=",r(s),"t*=",r(tcrit))
print("IC95 media=",(r(lo),r(hi)))
# prueba H0 mu=30 vs mu>30
t0=(xbar-30)/(s/np.sqrt(n)); print("t (mu0=30)=",r(t0),"p_unilat=",r(1-stats.t.cdf(t0,n-1)))
ph=d.a_tiempo.mean(); ee=np.sqrt(ph*(1-ph)/n)
print("p_hat a_tiempo=",r(ph),"IC95 prop=",(r(ph-1.96*ee),r(ph+1.96*ee)))
pe=d.error_doc.mean(); print("p_hat error_doc=",r(pe))
