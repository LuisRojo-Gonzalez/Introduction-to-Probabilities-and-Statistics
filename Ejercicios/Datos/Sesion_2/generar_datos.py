import numpy as np, pandas as pd, os
here=os.path.dirname(__file__)
rng=np.random.default_rng(3007)
N=1000
falla=(rng.random(N)<0.10).astype(int)
# sensor 1 (alarma): sens 0.90, fa 0.08
alarma=(rng.random(N) < np.where(falla==1,0.90,0.08)).astype(int)
# sensor 2 independiente dado estado: sens 0.85, fa 0.10
sensor2=(rng.random(N) < np.where(falla==1,0.85,0.10)).astype(int)
turno=rng.choice(["Dia","Noche"],N,p=[0.55,0.45])
demanda=rng.choice(np.arange(6),N,p=[0.10,0.22,0.30,0.22,0.11,0.05])
d=pd.DataFrame({"equipo_id":np.arange(1,N+1),"turno":turno,"falla_real":falla,
   "alarma":alarma,"sensor2":sensor2,"demanda_repuestos":demanda})
d.to_csv(f"{here}/monitoreo_piloto.csv",index=False)
d.to_excel(f"{here}/monitoreo_piloto.xlsx",sheet_name="monitoreo",index=False)
dic=pd.DataFrame({"variable":["equipo_id","turno","falla_real","alarma","sensor2","demanda_repuestos"],
 "descripcion":["Identificador del equipo","Turno (Dia/Noche)","1 si el equipo esta realmente en falla",
   "1 si el sensor principal activa alarma","1 si un segundo sensor independiente alerta",
   "Repuestos demandados en el dia (conteo 0-5)"],
 "tipo":["id","categorica","binaria","binaria","binaria","conteo"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
print("P(falla)=",r(d.falla_real.mean()),"P(alarma)=",r(d.alarma.mean()))
print("P(falla|alarma)=",r(d.falla_real[d.alarma==1].mean()))
print("P(falla|alarma y sensor2)=",r(d.falla_real[(d.alarma==1)&(d.sensor2==1)].mean()))
print("conf sensor1:\n",pd.crosstab(d.falla_real,d.alarma))
vc=d.demanda_repuestos.value_counts(normalize=True).sort_index()
print("pmf demanda:",{int(k):r(v) for k,v in vc.items()})
print("E[dem]=",r(d.demanda_repuestos.mean()),"P(<=1)=",r((d.demanda_repuestos<=1).mean()),
      "P(>=3)=",r((d.demanda_repuestos>=3).mean()),"F(2)=",r((d.demanda_repuestos<=2).mean()))
