import customtkinter as ctk
from tkinter import messagebox
import re
from validaciones import validar_login
from validaciones import evaluar_contrasena
from validaciones import validar_anio

# ==========================
# CONFIGURACIÓN GENERAL
# ==========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==========================
# VENTANA
# ==========================
ventana = ctk.CTk()

ventana.title("Sistema de Contraseñas Seguras")
ventana.geometry("900x750")

ventana.resizable(True, True)

ventana.configure(fg_color="#0D1117")

# ==========================
# FRAME PRINCIPAL
# ==========================
frame = ctk.CTkFrame(ventana, fg_color="#0D1117")

frame.pack(fill="both", expand=True)

def crear_panel():
    panel = ctk.CTkFrame(
        frame,
        width=550,
        height=520,
        corner_radius=20,
        fg_color="#161B22",
        border_width=2,
        border_color="#00E5FF"
    )

    panel.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    panel.pack_propagate(False)

    return panel


def limpiar_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_login():
    limpiar_frame()
    panel = crear_panel()

    titulo = ctk.CTkLabel(
        panel,
        text="SISTEMA DE CONTRASEÑAS SEGURAS",
        font=("Segoe UI", 20, "bold"),
        text_color="#00E5FF"
    )

    titulo.pack(pady=(50,20))

    subtitulo = ctk.CTkLabel(

        panel,
        text="Inicio de Sesión",
        font=("Segoe UI",18)
    )

    subtitulo.pack(
        pady=(0,30)
    )

    usuario_entry = ctk.CTkEntry(
        panel,
        width=320,
        height=45,
        placeholder_text="Usuario"
    )

    usuario_entry.pack(
        pady=10
    )

    password_entry = ctk.CTkEntry(
        panel,
        width=320,
        height=45,
        placeholder_text="Contraseña",
        show="*"
    )

    password_entry.pack(
        pady=10
    )

    def login():
        usuario = usuario_entry.get()
        password = password_entry.get()

        if validar_login(
            usuario,
            password
        ):
            mostrar_menu()
        else:

            messagebox.showerror(
                "Error",
                "Credenciales incorrectas"
            )
 
    boton_login = ctk.CTkButton(
        panel,
        text="INICIAR SESIÓN",
        width=250,
        height=45,
        fg_color="#00E5FF",
        hover_color="#0099AA",
        text_color="black",
        font=("Segoe UI",14,"bold"),
        command=login
    )

    boton_login.pack(
        pady=30
    )

mostrar_login()

def mostrar_menu():
    limpiar_frame()
    panel = crear_panel()
    titulo = ctk.CTkLabel(
        panel,
        text="MENÚ PRINCIPAL",
        font=("Segoe UI", 28, "bold"),
        text_color="#00E5FF"
    )

    titulo.pack(
        pady=(50,40)
    )

    boton_contrasena = ctk.CTkButton(
        panel,
        text="CREAR CONTRASEÑA SEGURA",
        width=300,
        height=50,
        fg_color="#00E5FF",
        hover_color="#0099AA",
        text_color="black",
        font=("Segoe UI",14,"bold"),
        command=mostrar_evaluador
    )

    boton_contrasena.pack(
        pady=15
    )

    boton_salir = ctk.CTkButton(
        panel,
        text="CERRAR SESIÓN",
        width=300,
        height=50,
        fg_color="#FF3131",
        hover_color="#CC0000",
        font=("Segoe UI",14,"bold"),
        command=mostrar_login
    )

    boton_salir.pack(
        pady=15
    )

def mostrar_evaluador():
    limpiar_frame()
    panel = crear_panel()
    titulo = ctk.CTkLabel(
        panel,
        text="CREAR CONTRASEÑA SEGURA",
        font=("Segoe UI", 24, "bold"),
        text_color="#00E5FF"
    )
    titulo.pack(pady=(20, 20))

    subtitulo1 = ctk.CTkLabel(
        panel,
        text="Datos para evitar en contraseña",
        font=("Segoe UI", 16),
        text_color="#9CAFFF"
    )
    subtitulo1.pack(pady=(10, 5))

    nombre_entry = ctk.CTkEntry(
        panel,
        width=350,
        placeholder_text="Nombre o apodo"
    )
    nombre_entry.pack(pady=5)

    def validar_anio_entry(texto):
        if texto == "":
            return True

        return (
            texto.isdigit()
            and len(texto) <= 4
        )

    vcmd_anio = (
        ventana.register(validar_anio_entry),
        "%P"
    )

    nacimiento_entry = ctk.CTkEntry(
        panel,
        width=350,
        placeholder_text="Año de nacimiento (AAAA)"
    )
    nacimiento_entry.pack(pady=5)

    def validar_password_entry(texto):
        if texto == "":
            return True
        return len(texto) <= 22

    vcmd_password = (
        ventana.register(validar_password_entry),
        "%P"
    )

    subtitulo2 = ctk.CTkLabel(
        panel,
        text="PROBAR CONTRASEÑA SEGURA",
        font=("Segoe UI", 16),
        text_color="#9CAFFF"
    )
    subtitulo2.pack(pady=(10, 5))

    password_entry = ctk.CTkEntry(
        panel,
        width=350,
        placeholder_text="Probar Contraseña",
        show="*",
        validatecommand=vcmd_password
    )
    password_entry.pack(pady=15)

    barra = ctk.CTkProgressBar(
        panel,
        width=350
    )
    barra.pack(pady=10)
    barra.set(0)

    nivel_label = ctk.CTkLabel(
        panel,
        text="FORTALEZA: DÉBIL",
        text_color="red"
    )
    nivel_label.pack(pady=5)

    def validar_tiempo_real(event=None):

        password = password_entry.get()
        nombre = nombre_entry.get()
        nacimiento = nacimiento_entry.get()

        puntos = 0

        # Longitud
        if len(password) >= 12:
            puntos += 1

        # Mayúscula
        if re.search(r"[A-Z]", password):
            puntos += 1

        # Minúscula
        if re.search(r"[a-z]", password):
            puntos += 1

        # Número
        if re.search(r"\d", password):
            puntos += 1

        # Símbolo
        if re.search(
            r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]",
            password
        ):
            puntos += 1

        # Datos personales
        contiene_datos = False

        if nombre and nombre.lower() in password.lower():
            contiene_datos = True

        if nacimiento and nacimiento in password:
            contiene_datos = True

        if not contiene_datos:
            puntos += 1

        barra.set(puntos / 6)

        if puntos <= 2:
            nivel_label.configure(
                text="FORTALEZA: DÉBIL",
                text_color="red"
            )

        elif puntos <= 4:

            nivel_label.configure(
                text="FORTALEZA: MEDIA",
                text_color="yellow"
            )

        else:

            nivel_label.configure(
                text="FORTALEZA: FUERTE",
                text_color="#39FF14"
            )

    def validar_contrasenia():
        anio = nacimiento_entry.get()
        if not validar_anio(anio):
            messagebox.showerror(
                "Error",
                "El año debe tener 4 dígitos y estar entre 1900 y el año actual."
            )

            return

        errores = evaluar_contrasena(
            password_entry.get(),
            [
                nombre_entry.get(),
                nacimiento_entry.get()
            ]
        )

        if not errores:
            messagebox.showinfo(
                "Éxito",
                "Contraseña válida y segura."
            )
            mostrar_evaluador()

        else:

            messagebox.showerror(
                "Error",
                "\n".join(errores)
            )

    password_entry.bind(
        "<KeyRelease>",
        validar_tiempo_real
    )

    validar_btn = ctk.CTkButton(
        panel,
        text="VALIDAR CONTRASEÑA",
        width=300,
        fg_color="#00E5FF",
        text_color="black",
        command=validar_contrasenia
    )

    validar_btn.pack(
        pady=(15, 5)
    )

    regresar_btn = ctk.CTkButton(
        panel,
        text="REGRESAR",
        width=300,
        command=mostrar_menu
    )

    regresar_btn.pack(
        pady=(5, 10)
    )   

ventana.mainloop()
