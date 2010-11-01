import pilas

pilas.iniciar(usar_motor='pygame')

mono = pilas.actores.Mono()
mono.escala = 1
mono.rotacion = 0

def girar():
    mono.rotacion = mono.rotacion + 1
    return True

pilas.mundo.agregar_tarea(0, girar)

pilas.mundo.camara.x = pilas.interpolar([200, 0], duracion=10)
pilas.mundo.camara.y = pilas.interpolar([200, 0], duracion=10)

pilas.avisar("Moviendo la camara...")
pilas.ejecutar()
