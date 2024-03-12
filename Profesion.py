class Profesion():
    def __init__(self, nombre, sueldo, cantidad_personas):
        self.__nombre = nombre
        self.__sueldo = sueldo
        self.__cantidad_personas = cantidad_personas

    def GetSueldo(self):
        return self.__sueldo
    def SetSueldo(self, nuevo_sueldo):
        self.__sueldo = nuevo_sueldo

    def GetNombre(self):
        return self.__nombre
    def SetNombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def GetCantidadPersonas(self):
        return self.__cantidad_personas
    def SetCantidadPersonas(self, nueva_cantidad_personas):
        self.__cantidad_personas = nueva_cantidad_personas

    def SumarPersona(self):
        self.__cantidad_personas += 1