import easyocr
import cv2
import numpy as np


# =====================================
# OCR
# =====================================

reader = easyocr.Reader(
    ['es'],
    gpu=False
)


# =====================================
# PREPROCESAR IMAGEN
# =====================================

def preprocess_image(image_path):

    image = cv2.imread(image_path)

    # =====================================
    # ESCALA GRISES
    # =====================================

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # =====================================
    # AGRANDAR IMAGEN
    # =====================================

    gray = cv2.resize(

        gray,

        None,

        fx=3,

        fy=3,

        interpolation=cv2.INTER_CUBIC

    )

    # =====================================
    # REDUCIR RUIDO
    # =====================================

    gray = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    # =====================================
    # THRESHOLD ADAPTATIVO
    # =====================================

    thresh = cv2.adaptiveThreshold(

        gray,

        255,

        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,

        cv2.THRESH_BINARY,

        11,

        2

    )

    # =====================================
    # SHARPEN
    # =====================================

    kernel = np.array([

        [0, -1, 0],

        [-1, 5,-1],

        [0, -1, 0]

    ])

    sharpen = cv2.filter2D(
        thresh,
        -1,
        kernel
    )

    return sharpen


# =====================================
# EXTRAER TEXTO
# =====================================

def extract_text(image_path):

    processed = preprocess_image(
        image_path
    )

    results = reader.readtext(

        processed,

        detail=0,

        paragraph=False

    )

    cleaned = []

    for line in results:

        line = line.strip()

        if len(line) > 1:

            cleaned.append(line)

    return "\n".join(cleaned)