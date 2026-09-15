import numpy as np, pandas as pd, os
from scipy import stats
here=os.path.dirname(__file__)
rng=np.random.default_rng(1010)
nA,nB=180,170
tA=np.round(rng.normal(5.2,1.1,nA),3); tB=np.round(rng.normal(4.7,1.0,nB),3)
dA=(rng.random(nA)<0.08).astype(int); dB=(rng.random(nB)<0.04).astype(int)
df=pd.DataFrame({"orden_id":np.arange(1,nA+nB+1),
   "proveedor":["A"]*nA+["B"]*nB,
   "tiempo_entrega":np.concatenate([tA,tB]),
   "defecto":np.concatenate([dA,dB])})
df.to_csv(f"{here}/proveedores_piloto.csv",index=False)
df.to_excel(f"{here}/proveedores_piloto.xlsx",sheet_name="proveedores",index=False)
dic=pd.DataFrame({"variable":["orden_id","proveedor","tiempo_entrega","defecto"],
 "descripcion":["Identificador de la orden","Proveedor (A/B)","Tiempo de entrega (dias)",
   "1 si la orden llego con defecto"],"tipo":["id","categorica","continua","binaria"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
print("A: n=",nA,"media=",r(tA.mean()),"sd=",r(tA.std(ddof=1)),"pdef=",r(dA.mean()))
print("B: n=",nB,"media=",r(tB.mean()),"sd=",r(tB.std(ddof=1)),"pdef=",r(dB.mean()))
tt=stats.ttest_ind(tA,tB,equal_var=False)
print("Welch t=",r(tt.statistic),"p_bilat=",r(tt.pvalue),"p_unilat=",r(tt.pvalue/2))
# dos proporciones (pooled z)
x1,x2=dA.sum(),dB.sum(); n1,n2=nA,nB
pc=(x1+x2)/(n1+n2); z=(dA.mean()-dB.mean())/np.sqrt(pc*(1-pc)*(1/n1+1/n2))
print("pc=",r(pc),"z_prop=",r(z),"p_unilat=",r(1-stats.norm.cdf(z)))
