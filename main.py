import customtkinter as ctk
import tkinter as tk

from tkinter import filedialog

from PIL import Image

from interfaces.sidebar import Sidebar

from ocr.ocr_engine import extract_text

from parser.smart_parser import parse_text

from database.db import save_order


# =====================================
# CONFIGURACIÓN GENERAL
# =====================================

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")


# =====================================
# CREAR APP
# =====================================

app = ctk.CTk()

app.geometry("1400x850")

app.title("Autopedidos OCR")


# =====================================
# GRID PRINCIPAL
# =====================================

app.grid_columnconfigure(1, weight=1)

app.grid_rowconfigure(0, weight=1)


# =====================================
# SIDEBAR
# =====================================

sidebar = Sidebar(app)

sidebar.grid(
    row=0,
    column=0,
    sticky="ns"
)


# =====================================
# MAIN FRAME
# =====================================

main_frame = ctk.CTkFrame(
    app,
    fg_color="#F1F5F9"
)

main_frame.grid(
    row=0,
    column=1,
    sticky="nsew"
)


# =====================================
# TÍTULO
# =====================================

title = ctk.CTkLabel(
    main_frame,
    text="Autopedidos OCR",
    font=("Arial", 32, "bold"),
    text_color="#111827"
)

title.pack(
    anchor="nw",
    padx=40,
    pady=20
)


# =====================================
# FUNCIÓN SUBIR IMAGEN
# =====================================

def upload_image():

    # =====================================
    # VENTANA TEMPORAL
    # =====================================

    root = tk.Tk()

    root.withdraw()

    root.attributes("-topmost", True)

    # =====================================
    # EXPLORADOR ARCHIVOS
    # =====================================

    file_path = filedialog.askopenfilename(

        parent=root,

        title="Seleccionar Imagen",

        filetypes=[
            ("Imágenes", "*.png *.jpg *.jpeg")
        ]
    )

    root.destroy()

    # =====================================
    # VALIDAR
    # =====================================

    if not file_path:
        return

    # =====================================
    # MOSTRAR IMAGEN
    # =====================================

    image = Image.open(file_path)

    image = image.resize((500, 300))

    ctk_image = ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=(500, 300)
    )

    image_label.configure(
        image=ctk_image,
        text=""
    )

    image_label.image = ctk_image

    # =====================================
    # EXTRAER TEXTO OCR
    # =====================================

    extracted_text = extract_text(
        file_path
    )

    print("\n=== TEXTO OCR ===\n")

    print(extracted_text)

    print("\n=================\n")

    # =====================================
    # PARSEAR TEXTO
    # =====================================

    orders = parse_text(
        extracted_text
    )

    normalized_text = extracted_text

    # =====================================
    # LIMPIAR TEXTBOX
    # =====================================

    textbox.delete(
        "1.0",
        "end"
    )

    # =====================================
    # MOSTRAR TEXTO DETECTADO
    # =====================================

    textbox.insert(
        "end",
        "============================================================\n"
    )

    textbox.insert(
        "end",
        "                 TEXTO DETECTADO\n"
    )

    textbox.insert(
        "end",
        "============================================================\n\n"
    )

    # =====================================
    # MOSTRAR LÍNEAS
    # =====================================

    for line in normalized_text.split("\n"):

        textbox.insert(
            "end",
            f"{line}\n"
        )

    textbox.insert(
        "end",
        "\n"
    )

    # =====================================
    # PEDIDOS DETECTADOS
    # =====================================

    textbox.insert(
        "end",
        "\n============================================================\n"
    )

    textbox.insert(
        "end",
        "               PEDIDOS DETECTADOS\n"
    )

    textbox.insert(
        "end",
        "============================================================\n\n"
    )

    # =====================================
    # MOSTRAR PEDIDOS
    # =====================================

    if len(orders) > 0:

        for order in orders:

            # =====================================
            # GUARDAR SQLITE
            # =====================================

            save_order(

                order["cliente"],

                order["producto"],

                order["cantidad"],

                order["presentacion"]

            )

            # =====================================
            # MOSTRAR RESULTADO
            # =====================================

            textbox.insert(
                "end",
                f"CLIENTE: {order['cliente']}\n"
            )

            textbox.insert(
                "end",
                f"PRODUCTO: {order['producto']}\n"
            )

            textbox.insert(
                "end",
                f"CANTIDAD: {order['cantidad']}\n"
            )

            textbox.insert(
                "end",
                f"PRESENTACIÓN: {order['presentacion']}\n"
            )

            textbox.insert(
                "end",
                f"UNIDAD: {order['unidad']}\n"
            )

            textbox.insert(
                "end",
                f"TEXTO ORIGINAL: {order['texto_original']}\n"
            )

            textbox.insert(
                "end",
                "\n----------------------------------------\n\n"
            )

    else:

        textbox.insert(
            "end",
            "No se detectaron pedidos."
        )


# =====================================
# BOTÓN SUBIR IMAGEN
# =====================================

upload_button = ctk.CTkButton(

    main_frame,

    text="Subir Imagen",

    command=upload_image,

    width=220,

    height=50,

    corner_radius=15,

    font=("Arial", 18, "bold")

)

upload_button.pack(
    pady=10
)


# =====================================
# LABEL IMAGEN
# =====================================

image_label = ctk.CTkLabel(

    main_frame,

    text="No hay imagen cargada",

    width=500,

    height=300,

    fg_color="white",

    text_color="black",

    corner_radius=20

)

image_label.pack(
    pady=20
)


# =====================================
# TEXTBOX RESULTADOS
# =====================================

textbox = ctk.CTkTextbox(

    main_frame,

    width=950,

    height=260,

    font=("Arial", 16)

)

textbox.pack(
    padx=30,
    pady=20
)


# =====================================
# EJECUTAR APP
# =====================================

app.mainloop()