'''
class Alumno:
    def __init__(self, name, nota):
        self.name = name
        self.nota = nota
    def __str__(self):
        return f"NAME: {self.name} SURNAME: {self.nota} "

def read_students():
    correct = False
    while not correct:
        try:
            number = int(input(" Please, enter the number of students you want to add: "))
            correct = True
        except ValueError:
            print("Incorrect value.", end=" ")
    return number

def read_name():
    name = input("Enter the NAME:")
    return name

def read_nota():
    correct = False
    while not correct:
        try:
            score = float(input("Please, enter score:"))
            if 0 <= score <= 10:
                correct = True
        except ValueError:
            print("Incorrect value.", end=" ")
    return score

students_list = []
student = read_students()

for i in range(1, student + 1):
    name = read_name()
    nota = read_nota()
    s = Alumno(name, nota)
    students_list.append(s)

for i in students_list:
    print(i)
    if i.nota >=  5:
        print(f"has aprobado ")
    if i.nota < 5:
        print(f"has suspendido ")
'''

'''
class Triangulo:
    
    def lados(self):
        self.lado1 = int(input("Introduce el lado1: "))
        self.lado2 = int(input("Introduce el lado2: "))
        self.lado3 = int(input("Introduce el lado3: "))

    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Triangulo equilatero")
        elif self.lado1 == self.lado2 or self.lado3 == self.lado2 or self.lado1 == self.lado3:
            print("triangulo isosceles")
        else:
            print("Triangulo escaleno")

    def mayor(self):
        mayor = int
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            mayor = self.lado1
            print(mayor)
        elif self.lado2 > self.lado3:
            mayor = self.lado2
            print(mayor)
        else:
            mayor = self.lado3
            print(mayor)

figura=Triangulo(0, 0, 0)
figura.lados()
figura.tipo()
figura.mayor()
'''
'''
class Calculator:
    def __init__(self):
        self.n1 = int(input("Introduce un n entero: "))
        self.n2 = int(input("Introduce un n entero: "))

    def suma(self):
        suma = self.n1 + self.n2
        print(suma)

    def resta(self):
        resta = self.n1 - self.n2
        print(resta)

    def mult(self):
        mult = self.n1 * self.n2
        print(mult)

    def div(self):
        div = self.n1 / self.n2
        print(div)


calculadora = Calculator()
calculadora.suma()
calculadora.resta()
calculadora.mult()
calculadora.div()
'''
'''
class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        print("---MENU---")
        print("1.-Añadir contacto")
        print("2.-Lista de contactos")
        print("3.-Buscar contacto")
        print("4.-Editar contacto")
        print("5.-Cerrar agenda")
        opcion = int(input("Introducca la opcion deseada: "))
        if opcion == 1:
            self.add_contact()
        elif opcion == 2:
            self.lista()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            self.editar()
        elif opcion == 5:
            print("Saliendo de la agenda...")
            exit()
        self.menu()

    def add_contact(self):
        print("---Añade al nuevo contacto---")
        name = input("Nombre: ")
        telefono = int(input("Telefono: "))
        email = input("Email: ")
        self.contactos.append({'Nombre': name, 'Telefono': telefono, 'Email': email})

    def lista(self):
        print("---Lista de contactos---")
        if len(self.contactos) != 0:
            for i in range(len(self.contactos)):
                print(self.contactos[i]['Nombre'])
        else:
            print("La Lista de contactos esta vacia")
    def buscar(self):
        print("---Buscar contactos---")
        buscador = input("Que nombre quieres buscar: ")
        for i in range(len(self.contactos)):
            if buscador == self.contactos[i]['Nombre']:
                print("Datos del contacto -->")
                print(f"Nombre: {self.contactos[i]['Nombre']}")
                print(f"Telefono: {self.contactos[i]['Telefono']}")
                print(f"Email: {self.contactos[i]['Email']}")
                return i

    def editar(self):
        print("Editar contacto")
        data = self.buscar()
        ok = False
        while not ok:
            select = input("¿Que quieres modificar?: ")
            if select == 'nombre':
                new_name = input("porque nombre lo vas a cambiar: ")
                self.contactos[data]["Nombre"]= new_name
            elif select == 'telefono':
                new_telefono = input("porque numero lo vas a cambiar: ")
                self.contactos[data]["Telefono"]= new_telefono
            elif select == 'email':
                new_email = input("porque email lo vas a cambiar: ")
                self.contactos[data]["Email"]= new_email
            elif select == exit:
                 ok = True

agenda = Agenda()
agenda.menu()
'''

