import numpy as np, pandas as pd, os
here=os.path.dirname(__file__)
rng=np.random.default_rng(404)
N=300
linea=rng.choice(["A","B"],N,p=[0.5,0.5])
# linea A: menos fallas y menos variabilidad; B mas
fallas=np.where(linea=="A", rng.choice([0,1,2,3,4],N,p=[0.5,0.3,0.13,0.05,0.02]),
                             rng.choice([0,1,2,3,4],N,p=[0.35,0.25,0.20,0.13,0.07]))
tiempo=np.round(rng.gamma(4,2.0,N)+2,2)   # media ~10
costo=500+20*fallas
d=pd.DataFrame({"turno_id":np.arange(1,N+1),"linea":linea,"fallas":fallas,
   "tiempo_ciclo":tiempo,"costo":costo})
d.to_csv(f"{here}/operacion_piloto.csv",index=False)
d.to_excel(f"{here}/operacion_piloto.xlsx",sheet_name="operacion",index=False)
dic=pd.DataFrame({"variable":["turno_id","linea","fallas","tiempo_ciclo","costo"],
 "descripcion":["Identificador del turno","Linea de produccion (A/B)","Numero de fallas menores en el turno",
   "Tiempo de ciclo promedio del turno (min)","Costo del turno = 500 + 20*fallas (USD)"],
 "tipo":["id","categorica","conteo","continua","continua"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
print("fallas: media=",r(d.fallas.mean()),"var_pob=",r(d.fallas.var(ddof=0)),"sd=",r(d.fallas.std(ddof=0)),
      "cv=",r(d.fallas.std(ddof=0)/d.fallas.mean()))
print("E[costo]=",r(d.costo.mean()),"sd[costo]=",r(d.costo.std(ddof=0)))
print("tiempo: media=",r(d.tiempo_ciclo.mean()),"sd=",r(d.tiempo_ciclo.std(ddof=0)),
      "cv=",r(d.tiempo_ciclo.std(ddof=0)/d.tiempo_ciclo.mean()))
for L in ["A","B"]:
    s=d.fallas[d.linea==L]; print(f"linea {L}: media={r(s.mean())} sd={r(s.std(ddof=0))}")
# Chebyshev: fraccion dentro de mu +- 2 sd (tiempo)
m=d.tiempo_ciclo.mean(); s=d.tiempo_ciclo.std(ddof=0)
print("frac dentro 2sd (tiempo)=",r(((d.tiempo_ciclo>m-2*s)&(d.tiempo_ciclo<m+2*s)).mean()))
