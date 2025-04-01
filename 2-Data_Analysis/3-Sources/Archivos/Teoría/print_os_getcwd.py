import os
print("PWD:")
print(os.getcwd())

print()
print("DIRECTORIO DEL SCRIPT:")
ruta_directorio = os.path.dirname(os.path.abspath(__file__))
print(ruta_directorio)



