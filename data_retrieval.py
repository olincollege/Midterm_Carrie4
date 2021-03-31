import kaggle
# from kaggle.api.kaggle_api_extended import KaggleApi
from kaggle import KaggleApi
api = KaggleApi()
api.authenticate()

api.dataset_download_files('shivamb/Netflix-shows', unzip= True)

