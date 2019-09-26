# Tarea 1 NLP

#### Nombre Equipo: Tinkiwinki
#### Intengrantes: Marcelo Navarro y Fernanda Sanchirico

## Run in Colaboratory:

Basta con abrir el archivo que se desea con [Colab](https://colab.research.google.com) :)
 
## Run in localhost:

0. instalar virtualenv (si ya lo tienes instalado ignora este paso)
```
    $ pip install virtualenv 
```

1. En la carpeta NLP_PROYECTS2019 crear un ambiente virtual. Esto creará una carpeta con el nombre *venv* que tendrá un nuevo ambiente para ejecutar python.

```
    $ virtualenv venv
```

1. Activar el nuevo ambiente virtual.

```
    $ source venv/bin/activate
```

3. Instalar paquetes necesarios para correr los archivos
```
    $ pip install -r requirements.txt
```

4. Instalar ambiente virtual para jupyter notebook

```
    $ ipython kernel install --user --name=.venv
```

5. Ejecutar jupyter notebook y al ejecutar un codigo setear el ambiente para python como .venv

```
    $ jupyter notebook
```