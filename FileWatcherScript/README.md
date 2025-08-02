# File Watcher Script

## 📌 Overview
This project is a **Python-based File Watcher** that continuously monitors a folder for new files.  
When a new file is detected, it automatically processes it and moves it to another folder.

It is useful for:
- ETL Pipelines
- Data ingestion workflows
- File processing automation

---

## 📂 Project Structure
```
FileWatcherScript/
├── file_watcher.py              ← Main Python script
├── README.md                    ← Project details
├── Watched_folder/              ← Folder where new files will be placed
├── Processed_folder/            ← Folder where processed files will be moved
├── sample_data/                 ← Sample input files for testing
└── documentation/               ← Word file & screenshots (optional)
```

---

## 🚀 How to Run
1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/FileWatcherScript.git
```

2. **Navigate to the folder**
```bash
cd FileWatcherScript
```

3. **Run the script**
```bash
python file_watcher.py
```

4. **Test the watcher**
- Place a file in the **Watched_folder**.
- The script will detect it and move it to **Processed_folder**.

---

## 🛠️ Technologies Used
- Python 3
- `os` module – For file/folder handling
- `time` module – For interval-based checking
- `shutil` module – For moving files

---

## 📸 Screenshots

    
## 📜 License
This project is open-source. You can use and modify it freely.
