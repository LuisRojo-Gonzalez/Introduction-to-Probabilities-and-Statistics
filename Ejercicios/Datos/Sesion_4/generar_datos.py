import numpy as np, pandas as pd, os
here=os.path.dirname(__file__)
rng=np.random.default_rng(505)
N=250; n_insp=20
turno=rng.choice(["Dia","Noche"],N,p=[0.55,0.45])
p=np.where(turno=="Noche",0.09,0.05)
defect=rng.binomial(n_insp,p)
llamadas=rng.poisson(3.0,N)
d=pd.DataFrame({"muestra_id":np.arange(1,N+1),"turno":turno,"n_inspeccion":n_insp,
   "defectuosas":defect,"llamadas_soporte":llamadas})
d.to_csv(f"{here}/control_piloto.csv",index=False)
d.to_excel(f"{here}/control_piloto.xlsx",sheet_name="control",index=False)
dic=pd.DataFrame({"variable":["muestra_id","turno","n_inspeccion","defectuosas","llamadas_soporte"],
 "descripcion":["Identificador de la muestra","Turno (Dia/Noche)","Tamano de la muestra inspeccionada (20)",
   "Numero de piezas defectuosas en la muestra","Llamadas de soporte recibidas en la hora"],
 "tipo":["id","categorica","constante","conteo","conteo"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
md=d.defectuosas.mean(); print("defectuosas: media=",r(md),"var=",r(d.defectuosas.var(ddof=0)),
   "p_estimado=",r(md/n_insp))
print("P(>=1 defect en muestra)=",r((d.defectuosas>=1).mean()))
print("llamadas: media=",r(d.llamadas_soporte.mean()),"var=",r(d.llamadas_soporte.var(ddof=0)),
   "P(0)=",r((d.llamadas_soporte==0).mean()))
print("p por turno:",{t:r(d.defectuosas[d.turno==t].mean()/n_insp) for t in ["Dia","Noche"]})
