# Image Metadata Extractor

Flask Image Metadata Extractor is a web application developed with Flask that allows users to upload images and extract metadata, including GPS information. The extracted GPS coordinates are then displayed on Google Maps.

## **Installation**

### **Clone the repository:**

```jsx
https://github.com/akhilathuluri/Image-Metadata-Extractor.git
```

This will install clone the  **Image Metadata Extractor** on your system, allowing you to use it from the command line.

### **Navigate to the project directory:**

```jsx
cd image-metadata-extractor
```

### **Install dependencies:**

```jsx
pip install -r requirements.txt
```

### **Usage**

1. **Run the Flask app:**

```jsx
python app.py
```

1. **Open a web browser and navigate to http://127.0.0.1:5000/.**
2. **Upload an image file with GPS information.**
3. **View the extracted metadata and the location displayed on Google Maps.**

### **File Structure**

```jsx
image-metadata-extractor/
│
├── app.py
│
├── uploads/
│   └── location.html
│
├── templates/
│   ├── upload.html
│   └── result.html
│
│
├── requirements.txt
│
└── LICENSE

```

###Outputs
![image](https://github.com/akhilathuluri/Image-Metadata-Extractor/assets/89147384/4537004e-dd19-4997-ae54-ef1489585dc4)
![image](https://github.com/akhilathuluri/Image-Metadata-Extractor/assets/89147384/9b106d7a-ad8f-4f0e-bca0-8db5d9479ddf)
![image](https://github.com/akhilathuluri/Image-Metadata-Extractor/assets/89147384/2ec5346b-b078-4c8a-9366-5b750639e7a3)


## **License**

This project is licensed under the MIT License - see the LICENSE file for details.
