# Inicialización de modelos
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_aligner = FaceAligner(shape_predictor, desireFaceWidh=200)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# Inicializacion del seguidor y almacenamiento
ct = CentroidTracker(maxDisappeared = 40, maxDistance = 50)
trackers = []
trackableObjects = {}

# Iniciar el estado y las detecciones
## Inicializar el estado actual y la lista de deliniación
status = "Waiting"
rects = []
cantidad = 0

## Metodo de detección para ayudar al tracker
if totalFrames % args["skip_frames"] == 0:
    #Cambiar el estado y definir el tracker
    status = "Detecting"
    trackers = []
    # Convertir el frame en un blob y pasar este através de la Red
    # neuronal para obtener las detecciones
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

## Buvle a través de las detecciones
for i in np.arange(0, detections.shape[2]):
    # Extraer el valor