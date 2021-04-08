import kaggle
from kaggle import KaggleApi
api = KaggleApi()
api.authenticate()

api.dataset_download_files("shivamb/Netflix-shows", unzip= True)


api.kernels_output("eugenioscionti/scraping-rotten-tomatoes-to-enrich-netflix-dataset", "./")