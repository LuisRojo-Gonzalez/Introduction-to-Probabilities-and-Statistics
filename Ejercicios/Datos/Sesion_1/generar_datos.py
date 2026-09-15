# Genera el caso integrador de la Unidad 2 (probabilidad basica)
import numpy as np, pandas as pd, os
rng = np.random.default_rng(2026)
N = 400
zona = rng.choice(["Norte","Centro","Sur"], N, p=[0.30,0.45,0.25])
ruta = rng.choice(["Rapida","Normal"], N, p=[0.40,0.60])
urgente = (rng.random(N) < 0.28).astype(int)
inspeccionado = (rng.random(N) < 0.50).astype(int)
# defecto depende de inspeccion (se detecta mas si se inspecciona) y zona
base_def = np.where(zona=="Sur",0.12,0.07)
defecto = (rng.random(N) < base_def).astype(int)
# atraso depende de ruta y urgencia
p_atr = 0.10 + 0.15*(ruta=="Normal") + 0.12*(urgente==1)
atrasado = (rng.random(N) < p_atr).astype(int)
# danado depende levemente de ruta rapida (manipulacion) 
p_dan = 0.06 + 0.05*(ruta=="Rapida")
danado = (rng.random(N) < p_dan).astype(int)
df = pd.DataFrame({"pedido_id":np.arange(1,N+1),"zona":zona,"ruta":ruta,
    "urgente":urgente,"inspeccionado":inspeccionado,"defecto":defecto,
    "atrasado":atrasado,"danado":danado})
os.makedirs(os.path.dirname(__file__), exist_ok=True)
here=os.path.dirname(__file__)
df.to_csv(os.path.join(here,"pedidos_piloto.csv"), index=False)
df.to_excel(os.path.join(here,"pedidos_piloto.xlsx"), sheet_name="pedidos", index=False)
dicc = pd.DataFrame({
 "variable":["pedido_id","zona","ruta","urgente","inspeccionado","defecto","atrasado","danado"],
 "descripcion":["Identificador del pedido","Zona de despacho (Norte/Centro/Sur)",
   "Ruta asignada (Rapida/Normal)","1 si el pedido es urgente","1 si el pedido fue inspeccionado",
   "1 si se registro defecto de producto","1 si la entrega llego atrasada","1 si el pedido llego danado"],
 "tipo":["id","categorica","categorica","binaria","binaria","binaria","binaria","binaria"]})
dicc.to_csv(os.path.join(here,"diccionario.csv"), index=False)
return_df=df
if __name__=="__main__":
    def r(x): return round(float(x),4)
    d=df
    print("N=",len(d))
    print("P(atrasado)=",r(d.atrasado.mean()),"P(urgente)=",r(d.urgente.mean()),
          "P(danado)=",r(d.danado.mean()),"P(defecto)=",r(d.defecto.mean()))
    print("P(atr|urg)=",r(d.atrasado[d.urgente==1].mean()),"P(atr|no urg)=",r(d.atrasado[d.urgente==0].mean()))
    print("P(atr|Normal)=",r(d.atrasado[d.ruta=='Normal'].mean()),"P(atr|Rapida)=",r(d.atrasado[d.ruta=='Rapida'].mean()))
    print("P(atr o dan)=",r(((d.atrasado==1)|(d.danado==1)).mean()),
          "P(atr y dan)=",r(((d.atrasado==1)&(d.danado==1)).mean()))
    print("P(defecto|Sur)=",r(d.defecto[d.zona=='Sur'].mean()))
    # total prob de atraso por zona (verificacion)
    tot=sum(d.atrasado[d.zona==z].mean()*(d.zona==z).mean() for z in ["Norte","Centro","Sur"])
    print("P(atr) via zonas=",r(tot))
    print("entrega OK (no atr y no dan) =",r(((d.atrasado==0)&(d.danado==0)).mean()))
    print("tabla ruta x atraso:"); print(pd.crosstab(d.ruta,d.atrasado))
