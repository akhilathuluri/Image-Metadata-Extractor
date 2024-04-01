from flask import Flask, render_template, request, send_from_directory
from flask_ngrok import run_with_ngrok
import os
import PIL.Image
import PIL.ExifTags
from gmplot import gmplot
from geopy.geocoders import Nominatim

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(image_path):
    img = PIL.Image.open(image_path)
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    if 'GPSInfo' not in exif:
        return None, None, None

    north = exif['GPSInfo'][2]
    east = exif['GPSInfo'][4]

    lat = ((((north[0] * 60) + north[1]) * 60) + north[2]) / 60 / 60
    lon = ((((east[0] * 60) + east[1]) * 60) + east[2]) / 60 / 60

    lat, lon = float(lat), float(lon)

    gmap = gmplot.GoogleMapPlotter(lat, lon, 12)
    gmap.marker(lat, lon, "cornflowerblue")
    map_file = os.path.join(app.config['UPLOAD_FOLDER'], 'location.html')
    gmap.draw(map_file)

    geoLoc = Nominatim(user_agent="GetLoc")
    locationName = geoLoc.reverse(f"{lat}, {lon}")
    address = locationName.address

    return lat, lon, address, exif, map_file

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('upload.html', error='No file part')
    file = request.files['file']
    if file.filename == '':
        return render_template('upload.html', error='No selected file')
    if file and allowed_file(file.filename):
        filename = 'uploaded_image.jpg'  # Save the uploaded file with a fixed name
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        lat, lon, address, exif, map_file = process_image(file_path)
        if lat is None or lon is None:
            return render_template('result.html', error='No GPS information found in the image')
        return render_template('result.html', map_file=map_file, lat=lat, lon=lon, address=address, exif=exif)
    else:
        return render_template('upload.html', error='File type not allowed')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run()
