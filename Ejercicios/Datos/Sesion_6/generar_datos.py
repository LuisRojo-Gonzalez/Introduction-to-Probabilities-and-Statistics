import numpy as np, pandas as pd, os
from scipy import stats
here=os.path.dirname(__file__)
rng=np.random.default_rng(707)
N=250
suc=rng.choice(["A","B","C"],N,p=[0.4,0.35,0.25])
tiempo=np.round(rng.gamma(2.5,3.0,N)+2,2)     # asimetrica derecha
gasto=np.round(rng.normal(25000,8000,N),0).clip(2000)
satisfecho=(rng.random(N)<0.78).astype(int)
d=pd.DataFrame({"cliente_id":np.arange(1,N+1),"sucursal":suc,"tiempo_atencion":tiempo,
   "gasto":gasto.astype(int),"satisfecho":satisfecho})
d.to_csv(f"{here}/atencion_piloto.csv",index=False)
d.to_excel(f"{here}/atencion_piloto.xlsx",sheet_name="atencion",index=False)
dic=pd.DataFrame({"variable":["cliente_id","sucursal","tiempo_atencion","gasto","satisfecho"],
 "descripcion":["Identificador del cliente","Sucursal (A/B/C)","Tiempo de atencion (min)",
   "Gasto del cliente (CLP)","1 si el cliente quedo satisfecho"],
 "tipo":["id","categorica","continua","continua","binaria"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
t=d.tiempo_atencion
print("tiempo: media=",r(t.mean()),"mediana=",r(t.median()),"sd=",r(t.std(ddof=1)),
      "asimetria=",r(stats.skew(t)),"curtosis_exceso=",r(stats.kurtosis(t)))
print("prop satisfecho=",r(d.satisfecho.mean()))
print("gasto: media=",r(d.gasto.mean()),"mediana=",r(d.gasto.median()))
print("n por sucursal:",dict(d.sucursal.value_counts()))
