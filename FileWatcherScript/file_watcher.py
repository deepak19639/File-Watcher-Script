import time
import os
import shutil  # for file move 
import logging 


logging.basicConfig(
    filename='file_watcher.log',   # Jisme log save hoga
    level=logging.INFO,            # Kya level ka message log ho (INFO/ERROR/etc.)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Kaise dikhna chahiye
)



WATCH_FOLER = "Watched_folder"
PROCESS_FOLDER = "Processed_folder"
FILE_TYPES = [ '.csv','.txt']



#crete folder if not exist
os.makedirs(WATCH_FOLER,exist_ok= True)
os.makedirs(PROCESS_FOLDER,exist_ok= True)


# seen files 

seen_files = set(os.listdir(WATCH_FOLER))


# new files


while True:
    time.sleep(2)   # break for 2 sec
    Current_file = set(os.listdir(WATCH_FOLER))
    new_files = Current_file - seen_files

    for file_name in new_files:
        if(file_name.endswith('.csv') or file_name.endswith('.txt')):
            file_path = os.path.join(WATCH_FOLER,file_name)
            print(f"new file {file_path}")
            logging.info(f"new file {file_path}")
            # seen_files.add(file_name)
    # process the file

        try:
            with open(file_path,'r') as f:
                lines = f.readlines()
                print(f"{file_name} has {len(lines) } lines")
                logging.info(f"{file_name} has {len(lines) } lines")
    # Move the files
            Processed_path = os.path.join(PROCESS_FOLDER,file_name)
            shutil.move(file_path,Processed_path)
            print(f"{file_name} has moved to : {PROCESS_FOLDER}")
            logging.info(f"{file_name} has moved to : {PROCESS_FOLDER}")

            seen_files.add(file_name)
            
        except Exception as e:
            print(f"File has error {str(e)}")







