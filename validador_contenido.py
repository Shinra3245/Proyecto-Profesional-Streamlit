# Clase para validar si el contenido de un archivo corresponde a una
# configuracion de red Cisco IOS o Huawei VRP, mas alla de su extension
class ValidadorContenido:

    # Palabras reservadas minimas que debe contener una configuracion valida
    PALABRAS_CLAVE = {
        "INTERFACE", "IP", "IPV6", "HOSTNAME", "VLAN", "ROUTER", "OSPF",
        "ACL", "ACCESS_LIST", "SYSTEM_VIEW", "SWITCH_PORT", "PORT",
        "SHOW", "DISPLAY", "SHUTDOWN", "UNDO", "ROUTE", "ROUTE_STATIC",
    }

    # Constructor
    def __init__(self, tokens):

        # Guardamos la lista de tokens generada por el analizador lexico
        self.tokens = tokens

    # Metodo para validar si el contenido pertenece a este lenguaje
    def es_configuracion_valida(self):

        # Armamos el conjunto de nombres de token presentes en el archivo
        nombres_token = {token["token"] for token in self.tokens}

        # Es valido si al menos una palabra clave esta presente
        return len(nombres_token & self.PALABRAS_CLAVE) > 0
