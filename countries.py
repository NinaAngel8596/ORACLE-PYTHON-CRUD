import oracledb

class Countries:

    #la funcion que crea la conexion entre python y mu sgbd en este caso oracle
    def __init__(self) -> None:
        # Crear una conexión y asignarla a la instancia
        self.cnn = oracledb.connect(
            user="system",
            password="angel123",  
            dsn="localhost/XE"    
        )


    
    def __str__(self):

        datos=self.consulta_paises()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
      
    def consulta_paises(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM usuarios")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_pais(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM countries WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_pais(self,Cod, Name, Lastname, Age):
        cur = self.cnn.cursor()
        sql='''INSERT INTO usuarios (Cod, Name, Lastname, Age) 
        VALUES('{}', '{}', '{}', '{}')'''.format(Cod, Name, Lastname, Age)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    


    #Metodo para elimnar un pais y toma como parametro de entrada el id
    #ya que ese sera el que se ingrese el input
    def elimina_pais(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
    
    def modifica_pais(self,Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
