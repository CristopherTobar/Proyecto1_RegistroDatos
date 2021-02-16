import pyautogui as pygu
import time
opt = 0

confi = pygu.confirm(text='INICIAR', title='BUSCAR', buttons=['OK', 'CANCEL'])
if confi == 'CANCEL':
    pygu.alert('FINALIZANDO')
    opt = 0
if confi == 'OK':
    pygu.alert('PROGRAMA CARGADO')
    opt = 1
while opt != 0:
    nomb = pygu.prompt(text="Ingrese nombre:", title="NOMBRE", default="NOMBRE(s) + APELLIDO(s)")
    mail = pygu.prompt(text="Ingrese su correo, si no tiene, escriba: 'nc'", title="CORREO", default="correo@mail.exapmle")
    celn = pygu.prompt(text="Ingrese telefono, si no tiene, escriba: 'nc'", title="TELEFONO", default="EX: 81 #### ####")
    txt = open("correos.txt", "a")
    txt.write("Nombre: ")
    txt.write(nomb)
    txt.write("\n")
    txt.write("Correo: ")
    txt.write(mail)
    txt.write("\n")
    txt.write("Telefono: ")
    txt.write(celn)
    txt.write("\n")
    txt.write("------------------------------------")
    txt.write("\n")
    confi = pygu.confirm(text='¿SE AGREGARA OTRA PERSONA?', title='CONFIRMACION', buttons=['SI', 'NO'])
    if confi == 'NO':
        opt = 0
    if confi == 'SI':
        opt = 1
