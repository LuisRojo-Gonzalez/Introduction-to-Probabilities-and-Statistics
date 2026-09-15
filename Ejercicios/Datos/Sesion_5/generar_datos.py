import numpy as np, pandas as pd, os
here=os.path.dirname(__file__)
rng=np.random.default_rng(606)
N=300
diametro=np.round(rng.normal(50,0.2,N),3)
t_rep=np.round(rng.exponential(5,N),3)        # media 5 h -> lambda=0.2
t_lleg=np.round(rng.uniform(0,2,N),3)         # horas tras las 8:00
peso=np.round(rng.normal(100,2,N),3)
d=pd.DataFrame({"pieza_id":np.arange(1,N+1),"diametro":diametro,"tiempo_reparacion":t_rep,
   "hora_llegada":t_lleg,"peso":peso})
d.to_csv(f"{here}/mediciones_piloto.csv",index=False)
d.to_excel(f"{here}/mediciones_piloto.xlsx",sheet_name="mediciones",index=False)
dic=pd.DataFrame({"variable":["pieza_id","diametro","tiempo_reparacion","hora_llegada","peso"],
 "descripcion":["Identificador de la pieza","Diametro de la pieza (mm)","Tiempo hasta reparar un equipo (h)",
   "Hora de llegada del camion (horas tras las 8:00)","Peso del producto (g)"],
 "tipo":["id","continua","continua","continua","continua"]})
dic.to_csv(f"{here}/diccionario.csv",index=False)
def r(x):return round(float(x),4)
print("diametro: media=",r(diametro.mean()),"sd=",r(diametro.std(ddof=0)))
print("P(diam<=50.3) emp=",r((diametro<=50.3).mean()))
print("P(49.6<=diam<=50.4) emp=",r(((diametro>=49.6)&(diametro<=50.4)).mean()))
print("t_rep: media=",r(t_rep.mean()),"P(<=3) emp=",r((t_rep<=3).mean()))
print("hora_llegada: media=",r(t_lleg.mean()),"P(<=0.75) emp=",r((t_lleg<=0.75).mean()))
print("peso: P(>103) emp=",r((peso>103).mean()))
