import turtle #Libreria turtle
from tkinter import Y, Tk, Label, Button, Entry#Libreria

class Fractal:#clase fractal(los diferentes tipo de fractales heredan de aqui)
    def __init__(self, longitud, factor, angulo, caso_base, iteraciones, firstp, **kwargs):#Inicializa las variables del fractal
        super().__init__(**kwargs)#esto sirve para pasarle distintos argumentos (basicamente con esto consigo que mas abajo una classe herede de dos classes que heredan de esta pero que tienen distintos atributos)
        self.longitud = longitud
        self.factor = factor
        self.angulo = angulo
        self.caso_base = caso_base
        self.a = turtle.Turtle()

    def dame_longitud(self, longitud):#editar longitud
        self.longitud = longitud
    
    def dame_factor(self,factor):#editar factor
        self.factor = factor
        
    def dame_angulo(self,angulo):#editar angulo
        self.angulo = angulo
    
    def dame_caso_base(self, caso_base):#editar caso base
        self.caso_base = caso_base

class Alfombra(Fractal):
    def __init__(self, longitud, factor, angulo, caso_base, **kwargs):
        super().__init__(longitud, factor, angulo, caso_base, **kwargs)

    def alfombra(self):
        for i in range(4):
            self.a.begin_fill()
            self.a.forward(self.longitud) 
            self.a.left(90) 
            self.a.end_fill()
        
        
class Tree(Fractal):#fractal arbol
    def __init__(self, longitud, factor, angulo, caso_base, **kwargs):#inicializa variables y a su padre
        super().__init__(longitud, factor, angulo, caso_base, **kwargs)

    def arbol(self, len):#calculo del arbol
        if len >= self.caso_base:
            self.a.forward(len)
            l = len - self.factor
            self.a.left(self.angulo)
            self.arbol(l)
            self.a.right(self.angulo* 2)
            self.arbol(l)
            self.a.left(self.angulo)
            self.a.backward(len)

class Koch(Fractal):#fractal kock
    def __init__(self, longitud, factor, angulo, caso_base, iteraciones,**kwargs):#inicializa variables y a su padre
        super().__init__(longitud, factor, angulo, caso_base, iteraciones,**kwargs)
        self.iteraciones = iteraciones

    def dame_iteraciones(self, it):#edita iteraciones
        self.iteraciones = it

    def curva_koch(self,l,i):#calculo del koch
        if i == self.caso_base:
            self.a.forward(l)
        else:
            i = i -1
            leng = l / self.factor
            self.curva_koch(leng, i)
            self.a.left(self.angulo)
            self.curva_koch(leng, i)
            self.a.right(self.angulo * 2)
            self.curva_koch(leng, i)
            self.a.left(self.angulo)
            self.curva_koch(leng, i)

class Sqr:#cuadrado del fractal alfombra
    def __init__(self, l, cx, cy, w, a):
        self.l = l
        self.x = a
       
        self.cx = cx
        self.cy = cy
        self.x.goto(self.cx, self.cy) 
        self.x.pendown()
        self.w = w

        self.x.begin_fill()
        for i in range(4):
            self.x.forward(self.l)
            self.x.left(90)
        self.x.end_fill()
        self.x.penup()


class Alfombra(Fractal):#factal alfombra
    def __init__(self, longitud, factor, angulo, caso_base, firstP ,**kwargs):
        super().__init__(longitud, factor, angulo, caso_base,firstP ,**kwargs)
        self.fillC = self.a.fillcolor
        self.x = firstP
        self.y = firstP
        self.it = -1

    
    def dame_pos(self, p):#edita la primera posicion del fractal
        self.x = p
        self.y = p

    def alfombra(self,l, x, y, w):#calculo de donde van y cuanto miden los cubitos de la alfombra y instancia de cubos
         
        
        if self.caso_base < float(l):
            
            
            len_ = l/3
            nw = w+1
            
            if l < self.longitud:
                miLongitudX = l
                miLongitudY = l

                nx = x + (miLongitudX*4)
                mx = x - (l*4/2)
                ny = y + (miLongitudY)
                my = y - (l *2)

                d = Sqr(l, nx, ny,nw, self.a)
                self.alfombra(len_, nx, ny,nw)
                d = Sqr(l, nx, my,nw,self.a)
                self.alfombra(len_, nx, my,nw)
                d = Sqr(l, nx, ny + (l *3),nw,self.a)
                self.alfombra(len_, nx, ny + (l *3),nw)

                d = Sqr(l, mx, ny,nw,self.a)
                self.alfombra(len_, mx, ny,nw)
                d = Sqr(l, mx, my,nw,self.a)
                self.alfombra(len_, mx, my,nw)
                d = Sqr(l, mx, ny + (l *3),nw,self.a)
                self.alfombra(len_, mx, ny + (l *3),nw)

                d = Sqr(l, x + l, my,nw,self.a)
                self.alfombra(len_, x + l, my,nw)
                d = Sqr(l, x + l, ny + (l *3),nw,self.a)
                self.alfombra(len_, x + l, ny + (l *3),nw)
            else:
                d = Sqr(l,x, y,w,self.a)
                nw = w+1
                self.alfombra(len_, x, y,w)


class Pinta(Tree, Koch, Alfombra):#classe que modifica la linea turtle para pintar los fractales
    def __init__(self):#inicializa variables y a su padre
        self.a = turtle.Turtle()
        super().__init__(0, 0, 0, 0, iteraciones = 4, firstp = 3)

    def dame_oculta(self, oculta):#edita mostrar cursor
        if oculta:
            self.a.hideturtle()
        else:
            self.a.showturtle()

    def dame_rumbo(self, rumbo):#edita el rumbo
        self.a.setheading(rumbo)

    def dame_color(self, color):#edita el color de la linea
        self.a.color(color)

    def pinta_arbol(self):#llama a que se genere un arbol
        self.arbol(self.longitud)
    
    def pinta_koch(self):#llama a que se genere un koch
      
        for i in range(3):
            self.curva_koch(self.longitud, self.iteraciones)
            self.a.right(120)
    
    def pinta_Alfombra(self):#llama a que se genere una alfombra
        self.alfombra(self.longitud, self.x, self.y, self.it)
 
class Windows:#classe window(interfaz)
    def __init__(self, principal):#inicializa la interfaz generanzo botones, titulos, la ventana...(lo que le quieras poner nada mas empezar)
        self.Board = Pinta()#genera la ventana donde se pintaran los fractales(objeto de la classe pintar)
        self.principal = principal#genera la ventana principal
        
        principal.title("Fractales")#Crea un titulo para la ventana
        principal.configure(bg='#222021')#cambia el color de la ventana
        self.etiqueta = Label(principal, text=" Escoge qué fractal quieres crear ", fg = 'white', bd = '0', bg='#222021')#genera y configura una frase
        self.etiqueta.pack(padx=5, pady=5)#la carga en el sitio indicado(en este caso solo le indico margenes)
        
        self.botonA = Button(principal, bd = '0', text="Arbol", bg='white', fg = '#222021', command= self.V_Arbol)#genera y configura un boton(llama a generar un arbol)
        self.botonA.pack(padx=5, pady=5)#lo carga en el sitio indicado(en este caso solo le indico margenes)
        
        self.botonK = Button(principal, bd = '0', text="Koch", bg='white', fg = '#222021', command = self.V_Koch)#genera y configura un boton(llama a gnerar un koch)
        self.botonK.pack(padx=5, pady=5)#lo carga en el sitio indicado(en este caso solo le indico margenes)

        self.botonAL = Button(principal, bd = '0', text="Alfombra", bg='white', fg = '#222021', command = self.V_Alfombra)#genera y configura un boton(llama a gnerar una alfombra)
        self.botonAL.pack(padx=5, pady=5)#lo carga en el sitio indicado(en este caso solo le indico margenes)

        self.botonClear = Button(principal, bd = '0', text="Limpiar", bg='white', fg = '#222021', command = self.Board.a.clear)#genera y configura un boton(Utiliza la funcion de turtle que limpia la pantalla)
        self.botonClear.pack(padx=5, pady=5)#lo carga en el sitio indicado(en este caso solo le indico margenes)
        
        self.botonCerrar = Button(principal, bd = '0', text="Cerrar", bg='white', fg = '#222021', command = principal.quit)#genera y configura un boton(Utiliza la funcion de tkinter que detiene el proceso)
        self.botonCerrar.pack(padx=5, pady=5)#lo carga en el sitio indicado(en este caso solo le indico margenes)


#--------------------------------------------------------------------------------------------Cargar datos de los fractales-----------------------------------------------------------------------------------------
#Las tres funciones de acontinuacion son horribles pero es que tkinter o le modificaba dos veces las variables y lo hacia en otra funcion decia nono aqui los strings no se modifican.


    def cargarA(self):#Modifica los atriutos de la 'Pizarra' y indica que hay que imprimir un arbol
        g1 = self.e1.get()
        g2 = self.e2.get()
        g3 = self.e3.get()
        g4 = self.e4.get()
        g5 = self.e5.get()
        g6 = self.e6.get()
        g7 = self.e7.get()

        o1 = g1.upper() == 'S'
        o2 = float(g2)
        o3 = str(g3).lower()
        o4 = float(g4)
        o5 = float(g5)
        o6 = float(g6)
        o7 = int(g7)

        self.Board.dame_oculta(o1)
        self.Board.dame_rumbo(o2)
        self.Board.dame_color(o3)
        self.Board.dame_longitud(o4)
        self.Board.dame_caso_base(o5)
        self.Board.dame_factor(o6)
        self.Board.dame_angulo(o7)

        self.uiArbol.destroy()
        self.Board.pinta_arbol()

    def cargarK(self):#Modifica los atriutos de la 'Pizarra' y indica que hay que imprimir un koch
        g1 = self.e1.get()
        g2 = self.e2.get()
        g3 = self.e3.get()
        g4 = self.e4.get()
        g5 = self.e5.get()
        g6 = self.e6.get()
        g7 = self.e7.get()
        g8 = self.e8.get()

        o1 = g1.upper() == 'S'
        o2 = float(g2)
        o3 = str(g3).lower()
        o4 = float(g4)
        o5 = float(g5)
        o6 = float(g6)
        o7 = int(g7)
        o8 = int(g8)

        self.Board.dame_oculta(o1)
        self.Board.dame_rumbo(o2)
        self.Board.dame_color(o3)
        self.Board.dame_longitud(o4)
        self.Board.dame_caso_base(o5)
        self.Board.dame_factor(o6)
        self.Board.dame_angulo(o7)
        self.Board.dame_iteraciones(o8)

        self.uiArbol.destroy()
        self.Board.pinta_koch()

    def cargarAlf(self):#Modifica los atriutos de la 'Pizarra' y indica que hay que imprimir una alfombra

        g2 = self.e2.get()
        g3 = self.e3.get()
        g4 = self.e4.get()
        g5 = self.e5.get()
        g9 = self.e9.get()

        o2 = float(g2)
        o3 = str(g3).lower()
        o4 = float(g4)
        o5 = float(g5)
        o9 = float(g9)

        self.Board.dame_rumbo(o2)
        self.Board.dame_color(o3)
        self.Board.dame_longitud(o4)
        self.Board.dame_caso_base(o5)
        self.Board.dame_pos(o9)

        self.uiArbol.destroy()
        self.Board.pinta_Alfombra()
        
#------------------------------------------------------------------------------Ventana de introducir datos de los fractales por teclado en cuadros de texto-----------------------------------------------------------------------------
#Las proximas 3 funciones son para crear una interfaz que te permita introducir los datos de cada fractal por cuadros de texto


    def V_Arbol(self):
        self.uiArbol = Tk()
        self.uiArbol.title('Parametros Arbol')
        self.uiArbol.configure(bg='#222021')
        
        self.etiqueta = Label(self.uiArbol, text=" Introduce los datos de tu arbol. ", fg = 'white', bd = '0', bg='#222021')
        self.etiqueta.pack(padx=5, pady=5)

        
        self.l1 = Label(self.uiArbol, text="Show cursor(s/n) ", fg = 'white', bd = '0', bg='#222021')
        self.l1.pack(padx=5, pady=5)
        self.e1 = Entry(self.uiArbol)
        self.e1.pack(padx=5, pady=5)
        
        self.l2 = Label(self.uiArbol, text="Angulo de rumbo ", fg = 'white', bd = '0', bg='#222021')
        self.l2.pack(padx=5, pady=5)
        self.e2 = Entry(self.uiArbol)
        self.e2.pack(padx=5, pady=5)

        self.l3 = Label(self.uiArbol, text="Color (red/green/blue) ", fg = 'white', bd = '0', bg='#222021')
        self.l3.pack(padx=5, pady=5)
        self.e3 = Entry(self.uiArbol)
        self.e3.pack(padx=5, pady=5)
        
        self.l4 = Label(self.uiArbol, text="Longitud ", fg = 'white', bd = '0', bg='#222021')
        self.l4.pack(padx=5, pady=5)
        self.e4 = Entry(self.uiArbol)
        self.e4.pack(padx=5, pady=5)

        self.l5 = Label(self.uiArbol, text="Caso base ", fg = 'white', bd = '0', bg='#222021')
        self.l5.pack(padx=5, pady=5)
        self.e5 = Entry(self.uiArbol)
        self.e5.pack(padx=5, pady=5)

        self.l6 = Label(self.uiArbol, text="Factor ", fg = 'white', bd = '0', bg='#222021')
        self.l6.pack(padx=5, pady=5)
        self.e6 = Entry(self.uiArbol)
        self.e6.pack(padx=5, pady=5)

        self.l7 = Label(self.uiArbol, text="Angulo ",fg = 'white', bd = '0', bg='#222021')
        self.l7.pack(padx=5, pady=5)
        self.e7 = Entry(self.uiArbol)
        self.e7.pack(padx=5, pady=5)
        
 
        self.botonAceptar = Button(self.uiArbol, bd = '0', text="Guardar", bg='white', fg = '#222021', command = self.cargarA)
        self.botonAceptar.pack(padx=5, pady=5)


    def V_Koch(self):
        self.uiArbol = Tk()
        self.uiArbol.title('Parametros Koch')
        self.uiArbol.configure(bg='#222021')
        
        self.etiqueta = Label(self.uiArbol, text=" Introduce los datos de tu Koch. ", fg = 'white', bd = '0', bg='#222021')
        self.etiqueta.pack(padx=5, pady=5)

        
        self.l1 = Label(self.uiArbol, text="Show cursor(s/n) ", fg = 'white', bd = '0', bg='#222021')
        self.l1.pack(padx=5, pady=5)
        self.e1 = Entry(self.uiArbol)
        self.e1.pack(padx=5, pady=5)

        self.l2 = Label(self.uiArbol, text="Angulo de rumbo ", fg = 'white', bd = '0', bg='#222021')
        self.l2.pack(padx=5, pady=5)
        self.e2 = Entry(self.uiArbol)
        self.e2.pack(padx=5, pady=5)

        self.l3 = Label(self.uiArbol, text="Color (red/green/blue) ", fg = 'white', bd = '0', bg='#222021')
        self.l3.pack(padx=5, pady=5)
        self.e3 = Entry(self.uiArbol)
        self.e3.pack(padx=5, pady=5)

        self.l4 = Label(self.uiArbol, text="Longitud ", fg = 'white', bd = '0', bg='#222021')
        self.l4.pack(padx=5, pady=5)
        self.e4 = Entry(self.uiArbol)
        self.e4.pack(padx=5, pady=5)

        self.l5 = Label(self.uiArbol, text="Caso base ", fg = 'white', bd = '0', bg='#222021')
        self.l5.pack(padx=5, pady=5)
        self.e5 = Entry(self.uiArbol)
        self.e5.pack(padx=5, pady=5)

        self.l6 = Label(self.uiArbol, text="Factor ", fg = 'white', bd = '0', bg='#222021')
        self.l6.pack(padx=5, pady=5)
        self.e6 = Entry(self.uiArbol)
        self.e6.pack(padx=5, pady=5)

        self.l7 = Label(self.uiArbol, text="Angulo ",fg = 'white', bd = '0', bg='#222021')
        self.l7.pack(padx=5, pady=5)
        self.e7 = Entry(self.uiArbol)
        self.e7.pack(padx=5, pady=5)

        self.l8 = Label(self.uiArbol, text="Iteraciones ",fg = 'white', bd = '0', bg='#222021')
        self.l8.pack(padx=5, pady=5)
        self.e8 = Entry(self.uiArbol)
        self.e8.pack(padx=5, pady=5)
       

        self.botonAceptar = Button(self.uiArbol, bd = '0', text="Guardar", bg='white', fg = '#222021', command = self.cargarK)
        self.botonAceptar.pack(padx=5, pady=5)


    def V_Alfombra(self):

        self.uiArbol = Tk()
        self.uiArbol.title('Parametros Alfombra')
        self.uiArbol.configure(bg='#222021')
        
        self.etiqueta = Label(self.uiArbol, text=" Introduce los datos de tu alfombra. ", fg = 'white', bd = '0', bg='#222021')
        self.etiqueta.pack(padx=5, pady=5)

        
        self.l2 = Label(self.uiArbol, text="Angulo de rumbo ", fg = 'white', bd = '0', bg='#222021')
        self.l2.pack(padx=5, pady=5)
        self.e2 = Entry(self.uiArbol)
        self.e2.pack(padx=5, pady=5)

        self.l3 = Label(self.uiArbol, text="Color (red/green/blue) ", fg = 'white', bd = '0', bg='#222021')
        self.l3.pack(padx=5, pady=5)
        self.e3 = Entry(self.uiArbol)
        self.e3.pack(padx=5, pady=5)

        self.l4 = Label(self.uiArbol, text="Longitud ", fg = 'white', bd = '0', bg='#222021')
        self.l4.pack(padx=5, pady=5)
        self.e4 = Entry(self.uiArbol)
        self.e4.pack(padx=5, pady=5)

        self.l5 = Label(self.uiArbol, text="Caso base ", fg = 'white', bd = '0', bg='#222021')
        self.l5.pack(padx=5, pady=5)
        self.e5 = Entry(self.uiArbol)
        self.e5.pack(padx=5, pady=5)

        self.l9 = Label(self.uiArbol, text="Posicion Inicial ", fg = 'white', bd = '0', bg='#222021')
        self.l9.pack(padx=5, pady=5)
        self.e9 = Entry(self.uiArbol)
        self.e9.pack(padx=5, pady=5)


        self.botonAceptar = Button(self.uiArbol, bd = '0', text="Guardar", bg='white', fg = '#222021', command = self.cargarAlf)
        self.botonAceptar.pack(padx=5, pady=5)


#Creamos el objeto tkinter y deja la ventana corriendo hasta que demos la orden de cerrar               
root = Tk()
miWindows = Windows(root)
root.mainloop()