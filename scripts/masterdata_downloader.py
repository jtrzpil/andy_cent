from requests import get
import gzip
import shutil
 
urls = ['https://landsat.usgs.gov/landsat/metadata_service/bulk_metadata_files/LANDSAT_OT_C2_L2.csv.gz',
        'https://landsat.usgs.gov/landsat/metadata_service/bulk_metadata_files/LANDSAT_ETM_C2_L2.csv.gz',
        'https://landsat.usgs.gov/landsat/metadata_service/bulk_metadata_files/LANDSAT_TM_C2_L2.csv.gz']
 
for url in urls:
    current_path = "../datasets/masterdata"+url.split("/")[-1]
    with open(current_path, "wb") as file:
        print("downloading landsat masterdata file")
        response = get(url)
        file.write(response.content)
        print("extracting landsat masterdata file")
        with gzip.open(current_path, 'rb') as f_in:
                with open(current_path[:-3], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
