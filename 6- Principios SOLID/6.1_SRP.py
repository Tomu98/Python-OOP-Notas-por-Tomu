# SRP - Single Responsibility Principle

# Principio de Responsabilidad Única.
# Este principio establece que una clase debe tener una sola razón para cambiar, en otras palabras, una clase debe tener una única responsabilidad en el sistema.
# Esto significa que una clase debe hacer solo una cosa y hacerlo bien.
# Si una clase tiene más de una responsabilidad, se vuelve más difícil de mantener y entender.
# Dividir la funcionalidad en clases más pequeñas y especializadas ayuda a mejorar la modularidad y la facilidad de mantenimiento.

# Ejemplo:
# Supongamos que estás creando una clase llamada "CorreoElectrónico" que se encarga de enviar correos electrónicos y, al mismo tiempo, almacena los correos en una base de datos.
# Esto violaría el SRP porque la clase tiene dos responsabilidades: enviar correos y gestionar la base de datos.
# En lugar de eso, puedes dividir estas responsabilidades en dos clases separadas: "EnvíoDeCorreo" y "AlmacenamientoDeCorreo".
# Cada una de estas clases tiene una única responsabilidad.

# Violación del SRP
class CorreoElectronico:
    def enviar_correo(self, mensaje):
        # Lógica para enviar el correo
        pass

    def guardar_correo_en_base_de_datos(self, correo):
        # Lógica para guardar el correo en la base de datos
        pass

# Aplicación del SRP
class EnvioDeCorreo:
    def enviar_correo(self, mensaje):
        # Lógica para enviar el correo
        return f"{mensaje} enviado."

class AlmacenamientoDeCorreo:
    def guardar_correo_en_base_de_datos(self, correo):
        # Lógica para guardar el correo en la base de datos
        return f"{correo} guardado exitosamente en la base de datos."
