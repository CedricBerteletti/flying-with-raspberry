from services.singleton import SingletonMeta
import services.settings as settings
import datetime


TIME_FORMAT = settings.get("time.format")
FOLDER = settings.get("pictures.folder")
PICTURES_NAME = settings.get("pictures.name")

class ImageProcessing(metaclass=SingletonMeta):

    num_picture = 0

    def take_picture():
        time_str = datetime.date.today().strftime(TIME_FORMAT)
        num_picture = num_picture + 1
        file_name = f"{FOLDER}{time_str}-{PICTURES_NAME}-{str(num_picture)}.jpg"
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)
        os.system("rpicam-still" + " -o " + file_name + " -t 1ms")
        
        return num_picture, file_name

