from scipy.constants import G ;
from numpy import sqrt;

datos_planetas = {
    'Mercurio': {'masa': 3.3011e23, 'radio': 2.4397e6},
    'Venus': {'masa': 4.8675e24, 'radio': 6.0518e6},
    'Tierra': {'masa': 5.972e24, 'radio': 6.371e6},
    'Marte': {'masa': 6.4171e23, 'radio': 3.3895e6},
    'Júpiter': {'masa': 1.8982e27, 'radio': 6.9911e7},
    'Saturno': {'masa': 5.6834e26, 'radio': 5.8232e7},
    'Urano': {'masa': 8.6810e25, 'radio': 2.5362e7},
    'Neptuno': {'masa': 1.0243e26, 'radio': 2.4622e7},
    'Plutón': {'masa': 1.303e22, 'radio': 1.1883e6}
}


##ve= sqrt(((2*G*M)/radio_tierra)) ##km segundos

def calcularEstaShit(datos_planetas):
    for i in datos_planetas.keys():
        masa = datos_planetas[i]["masa"]
        radio = datos_planetas[i]["radio"]
        ve=round((sqrt(((2*G*masa)/radio)))/1000,3)
        
        datos_planetas[i]["velocidad Escape"] = ve
    
    for i in datos_planetas.items():
        print(i)
        

calcularEstaShit(datos_planetas)
