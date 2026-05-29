import sqlite3


# =====================================
# CONECTAR DB
# =====================================

connection = sqlite3.connect(
    "autopedidos.db"
)

cursor = connection.cursor()


# =====================================
# CREAR TABLA
# =====================================

cursor.execute("""

CREATE TABLE IF NOT EXISTS pedidos (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    cliente TEXT,

    producto TEXT,

    cantidad TEXT,

    presentacion TEXT

)

""")


connection.commit()


# =====================================
# GUARDAR PEDIDO
# =====================================

def save_order(
    cliente,
    producto,
    cantidad,
    presentacion
):

    cursor.execute("""

    INSERT INTO pedidos (

        cliente,
        producto,
        cantidad,
        presentacion

    )

    VALUES (?, ?, ?, ?)

    """, (

        cliente,
        producto,
        cantidad,
        presentacion

    ))

    connection.commit()