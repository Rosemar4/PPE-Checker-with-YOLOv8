🦺 PPE Checker

This project detects Personal Protective Equipment (PPE) such as helmets and safety vests for construction firms using YOLOv8.  
It can run real-time on your webcam and draw bounding boxes around detected objects.
 

📂 Project Structure
PPE-Checker/
│── ppe_webcam.py # Main YOLOv8 detection script
│── requirements.txt # Python dependencies
│── README.md # Project description (this file)
│── .gitignore # Ignore unnecessary files
│── best.pt # Model weights 
 

🚀 Usage

1. Clone the repository
```bash
git clone https://github.com/your-username/PPE-Checker.git
cd PPE-Checker
```

2. Install dependencies
Copy code
```
pip install -r requirements.txt
```
3. Run detection with webcam
Copy code
```
python ppe_webcam.py
```

📦 Model Weights
The trained YOLOv8 model is available here:
👉 Download best.pt


📌 Example Classes
- Helmet
- Vest
- No Helmet
- No Vest
- Person

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📂 Dataset

The dataset used for training this model is available in two places:

- 📥 Google Drive:  
  👉 [Download Dataset](https://drive.google.com/drive/folders/1gqBkwLW9GpK_X8lPbZHrwrgwl2_CAwvu?usp=drive_link)  

- 🌐 **Roboflow** (original source):  
  👉 [View on Roboflow](https://universe.roboflow.com/rosemary-xt27v/ppe-detection-q897z-bghcd)
  

📦 How to Use
After downloading, place the dataset in a `datasets/` folder like this:

datasets/
│── PPE-Dataset/
    │── train/
    │── valid/
    │── test/
    │── data.yaml

