from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
# conexion a la base de datos 
# nombre base de datos 
dataBaseName="gestion_bd"


#usuario base de datos 
userName="root"

#contraseña base de datos
userPassword=""

#puerto de conexion
conexionPort="3306"

#servidor
ServerConnection="localhost"

#creando la conexion 
conexionToDataBase=f"mysql+mysqlconnector://{userName}:{userPassword}@{ServerConnection}:{conexionPort}/{dataBaseName}"


engine=create_engine(conexionToDataBase)
sessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

