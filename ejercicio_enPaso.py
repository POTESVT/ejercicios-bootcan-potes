from cmu_graphics import *
Rect(0,0,400,400,relleno=gradiente('rojoOscuro','rojoOscuro','negro', inicio='inferior'))
Estrella(20, 50, 5, 8, relleno='oro', redondez=40)
Estrella(280, 30, 5, 5, relleno='oro')
Estrella(170, 300, 5, 8, relleno='oro', redondez=40)
Estrella(340, 150, 5, 5, relleno='oro')
Estrella(50, 350, 5, 8, relleno='oro', redondez=40)
Estrella(250, 220, 5, 5, relleno='oro')
Estrella(380, 380, 5, 5, relleno='oro')
Estrella(75, 100, 5, 8, relleno='oro', redondez=40)
Estrella(80, 210, 5, 8, relleno='oro', redondez=40)
Estrella(175, 80, 5, 8, relleno='oro', redondez=40)
def onMouseMove(x, y):
    

    app.fondo = 'negro'
    
Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))

tierra = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    )
marte = Grupo(
    Círculo(200, 200, 120, relleno=None, borde='grisOscuro'),
    Círculo(200, 80, 10, relleno=gradiente('carmesí','rojoOscuro','carmesí', inicio='izquierda-superior'))
    )
jupiter = Grupo(
    Círculo(200, 200, 180, relleno=None, borde='grisOscuro'),
    Círculo(200, 20, 20, relleno=gradiente('ladrillo','rojoOscuro'))
    )
tierra.dirección = 'sentido-horario'

c1=Grupo(
    Poligono(12,22,5,10,15,14,15,2,29,14,relleno=gradiente('naranja','amarillo','naranja')),
    Circulo(20,20,10,relleno=gradiente('negro','rojoOscuro',inicio='derecha'),borde='naranja',anchuraDeBorde=1))
c1.dx=6
c1.dy=5

c2=Grupo(
Poligono(12,22,5,10,15,14,15,2,29,14,relleno=gradiente('naranja','amarillo','naranja')),
Circulo(20,20,10,relleno=gradiente('negro','rojoOscuro',inicio='derecha'),borde='naranja',anchuraDeBorde=1))
c2.dx=6
c2.dy=4
    
c2.centroX=350
def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
        marte.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'
        marte.dirección = 'sentido-antihorario'
def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 2
        marte.rotarÁngulo += 5
        jupiter.rotarÁngulo += 1
    else:
        tierra.rotarÁngulo -= 2
        marte.rotarÁngulo -= 5
        jupiter.rotarÁngulo -= 1
    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1
    #
    c1.centroX +=c1.dx
    c1.centroY +=c1.dy
    c2.centroX +=c2.dx
    c2.centroY +=c2.dy
    if ((c1.superior < 0) or (c1.inferior > 400)):
        c1.dy=-c1.dy
    
    elif((c1.izquierda < 0) or (c1.derecha > 400)):
        c1.dx=-c1.dx
    
    
    elif ((c2.superior < 0) or (c2.inferior > 400)):
        c2.dy=-c2.dy
    
    elif((c2.izquierda < 0) or (c2.derecha > 400)):
        c2.dx=-c2.dx
cmu_graphics.run()