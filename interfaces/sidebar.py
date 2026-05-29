import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(
            width=250,
            fg_color="#0F172A",
            corner_radius=0
        )

        self.grid_propagate(False)

        # Logo
        logo = ctk.CTkLabel(
            self,
            text="Autopedidos OCR",
            font=("Arial", 24, "bold"),
            text_color="white"
        )

        logo.pack(pady=(40, 30))

        # Menú
        menu_items = [
            "Inicio",
            "Subir Pedido",
            "Pedidos",
            "Historial",
            "Clientes",
            "Reportes",
            "Configuración"
        ]

        for item in menu_items:

            button = ctk.CTkButton(
                self,
                text=item,
                height=45,
                corner_radius=12,
                fg_color="transparent",
                hover_color="#2563EB",
                anchor="w",
                font=("Arial", 15)
            )

            button.pack(
                fill="x",
                padx=20,
                pady=8
            )