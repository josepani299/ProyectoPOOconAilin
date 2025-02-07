class Pelicula:

    # Creamos el constructor de la clase pelicula.
    def __init__(self,titulo="",director="",genero="",anioestreno=0,calificacion=0):
        self._titulo = titulo
        self._director = director
        self._genero = genero
        self._anioestreno = anioestreno
        self._calificacion = calificacion

    # Creamos los getter para cada atributo de la clase Pelicula

    def get_titulo(self):
        return self._titulo

    def get_directo(self):
        return self._director

    def get_genero(self):
        return self._genero

    def get_anioestreno(self):
        return self._anioestreno

    def get_calificaciom(self):
        return self._calificacion

