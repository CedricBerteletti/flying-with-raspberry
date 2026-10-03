from services.singleton import SingletonMeta
import services.config as config
import datetime
import glob
import os


class TraitementImage(metaclass=SingletonMeta):
    """Gère la prise et la récupération des images."""

    def __init__(self):
        self.TEMPS_FORMAT = config.get("temps.format")
        self.DOSSIER = config.get("images.dossier")
        self.IMAGES_NOM = config.get("images.nom")
        self.IMAGES_FORMAT = config.get("images.format")

        self.num_picture = 0

    def prend_photo(self):
        """Prend une photo et renvoie son ID ainsi que le chemin du fichier."""
        date_chaine = datetime.date.today().strftime(self.TEMPS_FORMAT)
        self.num_picture = self.get_id_derniere_image() + 1

        nom_fichier = f"{self.DOSSIER}{date_chaine}-{self.IMAGES_NOM}-{str(self.get_id_derniere_image())}.{self.IMAGES_FORMAT}"
        if not os.path.exists(self.DOSSIER):
            os.makedirs(self.DOSSIER)
        os.system(f"rpicam-still -o {nom_fichier} -t 1ms")

        return self.get_id_derniere_image(), nom_fichier

    def get_id_derniere_image(self):
        """Retourne l'identifiant de la dernière image enregistrée."""
        # Initialise le compteur d'images à partir des fichiers déjà présents.
        if self.num_picture == 0 and os.path.exists(self.DOSSIER):
            # Parcourt les images existantes pour définir le compteur.
            for fichier in glob.glob(f"{self.DOSSIER}*-{self.IMAGES_NOM}-*.{self.IMAGES_FORMAT}"):
                try:
                    numero = int(fichier.split(f"-{self.IMAGES_NOM}-")[-1].split(f".{self.IMAGES_FORMAT}")[0])
                    self.num_picture = max(self.num_picture, numero)
                except ValueError:
                    continue
        return self.num_picture

    def get_image(self, identifiant):
        """Retourne le chemin d'une image correspondant à l'identifiant donné."""
        suffixe_cible = f"-{self.IMAGES_NOM}-{str(identifiant)}.{self.IMAGES_FORMAT}"

        if os.path.exists(self.DOSSIER):
            for fichier in os.listdir(self.DOSSIER):
                if fichier.endswith(suffixe_cible):
                    return os.path.join(self.DOSSIER, fichier)

        return None

