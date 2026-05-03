from services.singleton import SingletonMeta
import services.settings as settings
import datetime
import os



class ImageProcessing(metaclass=SingletonMeta):

    def __init__(self):
        self.num_picture = 0
        self.TIME_FORMAT = settings.get("time.format")
        self.FOLDER = settings.get("pictures.folder")
        self.PICTURES_NAME = settings.get("pictures.name")

    def take_picture(self):
        time_str = datetime.date.today().strftime(self.TIME_FORMAT)
        self.num_picture = self.num_picture + 1
        file_name = f"{self.FOLDER}{time_str}-{self.PICTURES_NAME}-{str(self.num_picture)}.jpg"
        if not os.path.exists(self.FOLDER):
            os.makedirs(self.FOLDER)
        os.system(f"rpicam-still -o {file_name} -t 1ms")
        
        return self.num_picture, file_name

