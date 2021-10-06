from datetime import datetime 
import os 


#reinvertimos la fecha
def inv_fecha(fec):
    fen = datetime.strptime(fec,'%d/%m/%Y')
    return datetime.strftime(fen,'%Y-%m-%d')

#se hace el calculo del Bono1 y Bono2
def pago(sueldobase,horas,valor1,valor2):
    
    if int(horas) <= 5:
        SuelN= float(sueldobase) + float(sueldobase) / 0.05 * float(valor1)
    else:
        SuelN= float(sueldobase) + float(sueldobase) / 1.5 * float(valor2)
    return float(SuelN)

#datos a solicitar para calcular los bonos segun horas extras semanales
B1b1= input('Intoduzca bono General:')
B2b2 = input('Intoduzca bono Eficiencia:')


f = open("pago_nomina_12sep2021.py", "w")

#Leeo el archivo txt
with open("pagos.txt", "r") as pagos:
    for linea in pagos:

        campo = linea.split()

        
        if campo[0].isdigit():
            fec = inv_fecha(campo[1])
            suel = pago(campo[4].replace("$",""),campo[5],B1b1,B2b2)
        else:
            fec = campo[1]
            suel = campo[3]

        
      
        f.write(campo[0]+" ")
        f.write(fec+" ")
        f.write(campo[2]+" ")
        f.write(campo[3]+" ")
        f.write(campo[4]+" ")
        

       
        if campo[0].isdigit():
            f.write(campo[5]+" ")
            f.write(str(suel))
            f.write(os.linesep)
        else:
            f.write(os.linesep)
           
        

    f.close()




#file.write
