import re

from parser.product_matcher import match_product


# =====================================
# RECONSTRUIR LÍNEAS
# =====================================

def rebuild_lines(lines):

    rebuilt = []

    temp = ""

    for line in lines:

        line = line.strip()

        # =====================================
        # LÍNEAS MUY CORTAS
        # =====================================

        if len(line) <= 5:

            temp += " " + line

        else:

            if temp:

                rebuilt.append(
                    temp.strip()
                )

            temp = line

    if temp:

        rebuilt.append(
            temp.strip()
        )

    return rebuilt


# =====================================
# PARSEAR TEXTO
# =====================================

def parse_text(text):

    orders = []

    # =====================================
    # SEPARAR LÍNEAS
    # =====================================

    raw_lines = [

        line.strip()

        for line in text.split("\n")

        if line.strip()

    ]

    # =====================================
    # RECONSTRUIR
    # =====================================

    lines = rebuild_lines(
        raw_lines
    )

    print("\n=== LÍNEAS RECONSTRUIDAS ===\n")

    for l in lines:

        print(l)

    print("\n============================\n")

    # =====================================
    # CLIENTE
    # =====================================

    client = "No detectado"

    possible_clients = []

    for line in lines:

        if len(line.split()) >= 2:

            possible_clients.append(line)

    if len(possible_clients) > 0:

        client = possible_clients[-1]

    # =====================================
    # ANALIZAR PEDIDOS
    # =====================================

    for line in lines:

        # =====================================
        # PRODUCTO
        # =====================================

        product = match_product(line)

        if product:

            quantity = 1

            presentation = None

            unit = None

            # =====================================
            # CANTIDAD
            # =====================================

            quantity_match = re.search(
                r"(\d+)",
                line
            )

            if quantity_match:

                quantity = quantity_match.group(1)

            # =====================================
            # PRESENTACIÓN
            # =====================================

            presentation_match = re.search(
                r"x\s?(\d+)",
                line.lower()
            )

            if presentation_match:

                presentation = presentation_match.group(1)

            # =====================================
            # UNIDAD
            # =====================================

            units = [

                "und",
                "paq",
                "disp"

            ]

            for u in units:

                if u in line.lower():

                    unit = u

            # =====================================
            # GUARDAR
            # =====================================

            orders.append({

                "cliente": client,

                "producto": product,

                "cantidad": quantity,

                "presentacion": presentation,

                "unidad": unit,

                "texto_original": line

            })

    return orders