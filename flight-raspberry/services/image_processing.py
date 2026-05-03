from services.singleton import SingletonMeta
import services.settings as settings
import datetime
import glob
import os



class ImageProcessing(metaclass=SingletonMeta):

    def __init__(self):
        self.TIME_FORMAT = settings.get("time.format")
        self.FOLDER = settings.get("pictures.folder")
        self.PICTURES_NAME = settings.get("pictures.name")
        self.PICTURES_FORMAT = settings.get("pictures.format")

        self.num_picture = 0


    def take_picture(self):
        time_str = datetime.date.today().strftime(self.TIME_FORMAT)
        self.num_picture = self.get_last_picture_id() + 1

        file_name = f"{self.FOLDER}{time_str}-{self.PICTURES_NAME}-{str(self.get_last_picture_id())}.{self.PICTURES_FORMAT}"
        if not os.path.exists(self.FOLDER):
            os.makedirs(self.FOLDER)
        os.system(f"rpicam-still -o {file_name} -t 1ms")
        
        return self.get_last_picture_id(), file_name
    
    def get_last_picture_id(self):
        # Initialize the picture counter based on existing pictures
        if self.num_picture == 0 and os.path.exists(self.FOLDER):
            # Scan existing pictures to set the num_picture counter
            for file in glob.glob(f"{self.FOLDER}*-{self.PICTURES_NAME}-*.{self.PICTURES_FORMAT}"):
                try:
                    num = int(file.split(f"-{self.PICTURES_NAME}-")[-1].split(f".{self.PICTURES_FORMAT}")[0])
                    self.num_picture = max(self.num_picture, num)
                except ValueError:
                    continue
        return self.num_picture

    def get_picture(self, id):
        target_suffix = f"-{self.PICTURES_NAME}-{str(id)}.{self.PICTURES_FORMAT}"
        
        if os.path.exists(self.FOLDER):
            for file in os.listdir(self.FOLDER):
                if file.endswith(target_suffix):
                    return os.path.join(self.FOLDER, file)
        
        return None

