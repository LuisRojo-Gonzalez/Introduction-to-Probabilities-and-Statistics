import numpy as np, pandas as pd, os
from scipy import stats
here=os.path.dirname(__file__)
rng=np.random.default_rng(1212)
N=400
turno=rng.choice(["Dia","Noche"],N,p=[0.55,0.45])
# tipo depende del turno (noche mas B)
tipo=[]
for t in turno:
    if t=="Dia": tipo.append(rng.choice(["A","B","C"],p=[0.5,0.3,0.2]))
    else:        tipo.append(rng.choice(["A","B","C"],p=[0.3,0.5,0.2]))
tipo=np.array(tipo)
prov=rng.choice(["P1","P2","P3"],N,p=[0.4,0.35,0.25])
# gravedad depende de proveedor (P2 mas grave)
grav=[]
for p in prov:
    pg={"P1":0.2,"P2":0.4,"P3":0.25}[p]
    grav.append("Grave" if rng.random()<pg else "Leve")
grav=np.array(grav)
d=pd.DataFrame({"registro_id":np.arange(1,N+1),"turno":turno,"tipo_defecto":tipo,
   "proveedor":prov,"gravedad":grav})
d.to_csv(f"{here}/defectos_piloto.csv",index=False)
d.to_excel(f"{here}/defectos_piloto.xlsx",sheet_name="defectos",index=False)
dic=pd.DataFrame({"variable":["registro_id","turno","tipo_defecto","proveedor","gravedad"],
 "descripcion":["Identificador del registro","Turno (Dia/Noche)","Tipo de defecto (A/B/C)",
   "Proveedor (P1/P2/P3)","Gravedad del defecto (Leve/Grave)"],
 "tipo":["id","categorica","categorica","categorica","categorica"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
# independencia turno x tipo
ct=pd.crosstab(d.turno,d.tipo_defecto); chi,p,dof,exp=stats.chi2_contingency(ct,correction=False)
print("turno x tipo:\n",ct); print("chi2=",r(chi),"gl=",dof,"p=",r(p))
n=ct.values.sum(); V=np.sqrt(chi/(n*(min(ct.shape)-1))); print("V Cramer=",r(V))
# homogeneidad proveedor x gravedad
ct2=pd.crosstab(d.proveedor,d.gravedad); chi2,p2,dof2,exp2=stats.chi2_contingency(ct2,correction=False)
print("proveedor x gravedad:\n",ct2); print("chi2=",r(chi2),"gl=",dof2,"p=",r(p2))
# bondad de ajuste tipo vs (0.4,0.4,0.2)
obs=d.tipo_defecto.value_counts().reindex(["A","B","C"]).values
expp=np.array([0.4,0.4,0.2])*N; chi3,p3=stats.chisquare(obs,expp)
print("tipo obs=",obs.tolist(),"esp=",expp.tolist(),"chi2_gof=",r(chi3),"p=",r(p3))
