from estudiantes import estudiantesBD
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self,ventana):
           self.ventana=ventana
           self.ventana.title("Gestion de estudiantes")
           self.ventana.geometry("800x600")
           self.ventana.resizable(0,0)
           self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
            
    #VISTAS DEL SISTEMA
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Estudiantes"
        Label(self.ventana,text=f"\n...::: menu de {tipo} :::... \n")
        Button(self.ventana,text="1.- Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.- Borra",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Salir",command=self.main).pack(pady=5)
        
    def main (self):
        self.borrarPantalla()
        Label(self.ventana,text="\n...::: M E N U   P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana,text="1.- Estudientes",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=5)
        
    def insertar_view(self):
            self.borrarPantalla()
            Label(self.ventana,text="...Ingresar los datos de Estudiante").pack(pady=10)
            
            Label(self.ventana,text="Nombre Completo").pack(pady=5)
            self._nombre=Entry(self.ventana)
            self._nombre.focus()
            self._nombre.pack(pady=5)
            
            Label(self.ventana,text="Nota o Calificacion").pack(pady=5)
            self._nota=Entry(self.ventana)
            self._nota.focus()
            self._nota.pack(pady=5)
            
            Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
            Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)
            
    def eliminar_view(self):
            self.borrarPantalla()
            Label(self.ventana,text="...Ingresar el ID del Estudiante a eliminar").pack(pady=10)
                
            Label(self.ventana,text="ID").pack(pady=5)
            self.id=Entry(self.ventana)
            self.id.pack(pady=5)
                
                
            Button(self.ventana,text="Eliminar",command=self.eliminar_controller).pack(pady=10)
            Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)
            
    def consultar_view(self):
            self.borrarPantalla()
            Label(self.ventana,text="::: Consultar los estudiantes :::").pack(pady=10)
            filas=""
            filas=self.consultar_controller(filas)
            Label(self.ventana,text=f"{'No.':<20} {'ID':<20} {'Nombre':<20} {'Nota':<20}").pack(pady=5)
            Label(self.ventana,text=f"-"*100).pack(pady=5)
            Label(self.ventana,text=f"{filas}").pack(pady=5)
            Label(self.ventana,text=f"-"*100).pack(pady=5)
            Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
            
    def modificar_view(self):
                self.borrarPantalla()
                Label(self.ventana,text="...Ingresar el ID del Estudiante a modificar").pack(pady=10)
                        
                Label(self.ventana,text="ID").pack(pady=5)
                self.id=Entry(self.ventana)
                self.id.focus()
                self.id.pack(pady=5)
                
                Label(self.ventana,text="Nuevo Nombre").pack(pady=5)
                self._nombre=Entry(self.ventana)
                self._nombre.pack(pady=5)
                        
                Label(self.ventana,text="Nueva Nota").pack(pady=5)
                self._nota=Entry(self.ventana)
                self._nota.pack(pady=5)
                        
                Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
                Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)
            
    #CONTROLADOR DEL SISTEMA
    def insertar_controller(self):
            estudiante1=estudiantesBD.EstudianteBD(self._nombre.get(),self._nota.get())
            respuesta=estudiante1.insertar()
            self.respuesta_sql(respuesta)
            del estudiante1
            self.insertar_view()
            
    def eliminar_controller(self):
                id=self.id.get()
                respuesta=estudiantesBD.EstudianteBD.eliminar(id)
                self.respuesta_sql(respuesta)
                
    def consultar_controller(self,filas):
            registros= estudiantesBD.EstudianteBD.consultar()
            if len(registros)>0:
                num_estudiante=1
                for fila in registros:
                    #filas=filas+f"Estudiante # {num_estudiante}\nID: {fila[0]}\t Nombre: {fila[1]}\n\t Nota: {fila[2]}"
                    filas=filas+f"\n{num_estudiante:<20}{fila[0]:<20}{fila[1]:<20}{fila[2]:<20}"
                    num_estudiante+=1
            else:
                    print("\n\n\t ¡No existen datos que mostrarpor el momento ...!")
                    
            return filas
        
    def modificar_controller(self):
            id=self.id.get()
            estudiante1=estudiantesBD.EstudianteBD(self._nombre.get(),self._nota.get())
            respuesta=estudiante1.actualizar(id)
            self.respuesta_sql(respuesta)
            del estudiante1

    def respuesta_sql(self,respuesta):
           if respuesta:
               messagebox.showinfo(title="... Exitoso ...",message="... ¡Accion Realizada con Exito!")
           else:
               messagebox.showerror(title="...¡ Verifique por favo !...",message="...¡Esta Accion no pudo realizarse en este momento!...")

    def datos_estudiantes(self, tipo):
        self.borrarPantalla()
        print(f"\n\t\t...Ingresa los datos del {tipo}...")
        estudiantitos={}
        estudiantitos['nombre'] = input("\t\tIngresa el nombre del estudiante: ").upper().strip()
        estudiantitos['nota'] = input("\t\tIngresa la nota del estudiante: ").upper().strip()

        return estudiantitos

    def menu_estudiantes(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")
            match opcion:
                case '1':
                    self.borrarPantalla()
                    estudiantitos = self.datos_estudiantes("Estudiantes")
                    estudiante1 = estudiantesBD.EstudianteBD(estudiantitos['nombre'], estudiantitos['nota'])

                    respuesta = estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case '2':
                    self.borrarPantalla()
                    try:
                        id = int(input("Ingresa el ID del estudiante a eliminar: ").strip())
                        respuesta =estudiantesBD.EstudianteBD.eliminar(id)
                        self.respuesta_sql(respuesta)
                    except:
                        print("\t\tError: El ID debe ser un numero.")
                        self.esperarTecla()

                case '3':
                    self.borrarPantalla()
                    try:
                        id = int(input("Ingresa el ID del estudiante a actualizar: ").strip())
                        self.borrarPantalla()
                        estudiantitos = self.datos_estudiantes("Estudiantes")
                        estudiante1 = estudiantesBD.EstudianteBD(estudiantitos['nombre'], estudiantitos['nota'])

                        respuesta = estudiante1.actualizar(id)
                        self.respuesta_sql(respuesta)
                        del estudiante1

                    except:
                        print("\t\tError: El ID debe ser un numero.")
                        self.esperarTecla()

                case '4':
                    self.borrarPantalla()
                    registros = estudiantesBD.EstudianteBD.consultar()

                    if registros and len(registros) > 0:
                        num_estudiante = 1
                        for fila in registros:
                            print(f"\n\t\t...::: Estudiante # {num_estudiante} :::...")
                            print(f"ID: {fila[0]}")
                            print(f"Nombre: {fila[1]}")
                            print(f"Nota: {fila[2]}")
                            num_estudiante += 1
                        self.esperarTecla()
                    else:
                        print("\n\n\t NO existen datos que mostrar por el momento")
                        self.esperarTecla()

                case '5':
                    self.borrarPantalla()
                    print("\t\t...Regresando al menu principal...")
                    opcion = False

                case _:
                    input("\t\t\t...Opcion invalida...")

    #def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            print("\n\t\t\t...::: Menu Principal :::...\n")
            print("1.- Estudiantes")
            print("2.- Salir")
            opcion = input("Elige una opcion: ").strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()
                case '2':
                    self.borrarPantalla()
                    print("...Salir del sistema...")
                    opcion = False
                case _:
                    input("\t\t\t...Opcion invalida...")

if __name__ == "__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()