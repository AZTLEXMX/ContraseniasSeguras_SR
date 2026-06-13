import re
from datetime import datetime

# ==========================================
# BASE DE DATOS SIMULADA
# ==========================================

USUARIOS_DB = {
    "admin": "admin123",
    "estudiante": "pass1234"
}

# ==========================================
# VALIDACIÓN DE LOGIN
# ==========================================

def validar_login(usuario, password):

    return (
        usuario in USUARIOS_DB
        and USUARIOS_DB[usuario] == password
    )

# ==========================================
# VALIDACIÓN DE AÑO
# ==========================================

def validar_anio(anio):

    if not anio.isdigit():
        return False

    if len(anio) != 4:
        return False

    anio = int(anio)

    anio_actual = datetime.now().year

    return (
        1900 <= anio <= anio_actual
    )

# ==========================================
# EVALUACIÓN DE CONTRASEÑA
# ==========================================

def evaluar_contrasena(password, datos_personales):

    errores = []

    # Longitud

    if len(password) < 12 or len(password) > 22:

        errores.append(
            "Debe tener entre 12 y 22 caracteres."
        )

    # Mayúscula

    if not re.search(r"[A-Z]", password):

        errores.append(
            "Debe incluir una letra mayúscula."
        )

    # Minúscula

    if not re.search(r"[a-z]", password):

        errores.append(
            "Debe incluir una letra minúscula."
        )

    # Número

    if not re.search(r"\d", password):

        errores.append(
            "Debe incluir un número."
        )

    # Símbolo

    if not re.search(
        r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]",
        password
    ):

        errores.append(
            "Debe incluir un símbolo."
        )

    # Datos personales

    for dato in datos_personales:

        if (
            dato
            and dato.lower() in password.lower()
        ):

            errores.append(
                f"No debe contener '{dato}'."
            )

    # Secuencias numéricas

    secuencias = [
        "123456",
        "234567",
        "345678",
        "456789",
        "987654",
        "876543",
        "765432",
        "654321"
    ]

    for secuencia in secuencias:

        if secuencia in password:

            errores.append(
                "No debe contener secuencias numéricas."
            )

            break

    # Patrones comunes

    patrones = [
        "qwerty",
        "asdf",
        "zxcv",
        "password",
        "admin",
        "abc123"
    ]

    for patron in patrones:

        if patron.lower() in password.lower():

            errores.append(
                f"No debe contener patrones comunes ({patron})."
            )

            break

    # Repetición excesiva

    if len(set(password)) <= 3:

        errores.append(
            "Demasiados caracteres repetidos."
        )

    return errores