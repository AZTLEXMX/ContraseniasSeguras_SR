import re
import getpass
import sys

# ==========================================
# BASE DE DATOS SIMULADA PARA INICIO SESIÓN
# ==========================================
USUARIOS_DB = {
    "admin": "admin123",
    "estudiante": "pass1234"
}


# ==========================================
# FUNCIONES DE LÓGICA Y VALIDACIÓN
# ==========================================

def iniciar_sesion():
    """Maneja la lógica de inicio de sesión del usuario."""
    print("\n" + "=" * 40)
    print("   SISTEMA DE SEGURIDAD - LOGIN")
    print("=" * 40)

    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        if usuario in USUARIOS_DB and USUARIOS_DB[usuario] == password:
            print(f"\n\t Bienvenido, {usuario}.")
            return True
        else:
            intentos -= 1
            print(
                f"[-] Credenciales incorrectas. Te quedan {intentos} intento(s).")

    print("\n[!] Has agotado tus intentos. Saliendo del sistema...")
    return False


def evaluar_contrasena(password, datos_personales):
    """
    Evalúa si una contraseña cumple con los requisitos de seguridad.
    Retorna una lista de errores. Si la lista está vacía, es segura.
    """
    errores = []

    # 1. Al menos 12 caracteres de longitud
    if len(password) < 12:
        errores.append("Debe tener al menos 12 caracteres de longitud.")

    # 2. Letras mayúsculas
    if not re.search(r"[A-Z]", password):
        errores.append("Debe incluir al menos una letra mayúscula.")

    # 3. Letras minúsculas
    if not re.search(r"[a-z]", password):
        errores.append("Debe incluir al menos una letra minúscula.")

    # 4. Números
    if not re.search(r"\d", password):
        errores.append("Debe incluir al menos un número.")

    # 5. Símbolos
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        errores.append(
            "Debe incluir al menos un símbolo (por ejemplo, @, #, $).")

    # 6. Información personal obvia
    for dato in datos_personales:
        if dato and dato.lower() in password.lower():
            errores.append(
                f"No debe contener información personal obvia (se detectó: '{dato}').")

    return errores


# ==========================================
# MENÚ PRINCIPAL Y FLUJO DE LA APLICACIÓN
# ==========================================

def menu_crear_contrasena():
    """Flujo para crear y evaluar una contraseña segura."""
    print("\n" + "-" * 40)
    print("   CREACIÓN DE CONTRASEÑA SEGURA")
    print("-" * 40)
    print("Requisitos:")
    print(" - Al menos 12 caracteres de longitud.")
    print(" - Debe incluir letras mayúsculas y minúsculas.")
    print(" - Debe incluir números.")
    print("- Debe incluir símbolos (por ejemplo, @, #, $, etc.).")
    print(" - No debe contener información personal obvia, tales como nombre o fecha de nacimiento\n")

    # Recopilar datos para la validación de información personal
    print(
        "Para asegurar que tu contraseña no tenga datos obvios, necesitamos:")
    nombre = input("Tu nombre o apodo: ").strip()
    fecha_nacimiento = input("Tu año de nacimiento (ej. 1995): ").strip()

    datos_personales = [nombre, fecha_nacimiento]

    while True:
        print("\nEjemplo de contraseña robusta: G3n!us#P@ssw0rd2024")
        nueva_pass = input(
            "\nIngresa la contraseña que deseas evaluar (o 'salir' para cancelar): ").strip()

        if nueva_pass.lower() == 'salir':
            break

        print("\nEvaluando contraseña...")
        errores = evaluar_contrasena(nueva_pass, datos_personales)

        if not errores:
            print("[+] ¡Felicidades! Tu contraseña es ROBUSTA y SEGURA.")
            break
        else:
            print(
                "[-] Tu contraseña es DÉBIL. No cumple con los siguientes requisitos:")
            for error in errores:
                print(f"    * {error}")
            print("\n¡Inténtalo de nuevo!")


def app():
    """Función principal que orquesta la aplicación."""
    if iniciar_sesion():
        while True:
            print("\n" + "=" * 40)
            print("            MENÚ PRINCIPAL")
            print("=" * 40)
            print("1. Crear contraseña segura")
            print("2. Salir")

            opcion = input("\nSelecciona una opción (1-2): ").strip()

            if opcion == '1':
                menu_crear_contrasena()
            elif opcion == '2':
                print("Cerrando sesión.")
                sys.exit()
            else:
                print("Opción no válida. Intenta de nuevo.")


# Punto de entrada del script
if __name__ == "__main__":
    app()