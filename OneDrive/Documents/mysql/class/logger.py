import os
import logging
from datetime import datetime


log_file_name=f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

log_file_dir=os.path.join(os.getcwd(),'logs')

os.mkdirs(log_file_dir,exist_Ok=True)

log_file_path = os.path.join(log_file_dir,log_file_name)

logging.basicConfig(
    filemode=log_file_path,
    level=logging.DEBUG,
    format='{astime} --- {name} --- {message}',
    style='{'
)
