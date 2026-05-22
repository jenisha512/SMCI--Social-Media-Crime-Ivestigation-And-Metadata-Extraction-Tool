import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Import your custom modules
from modules.metadata import get_exif_data
from modules.analysis import scan_text_for_crime
from modules.hashing import calculate_hash

# Try to import OCR, but handle it if the module is missing
try:
    from modules.ocr import extract_text_from_image
except ImportError:
    extract_text_from_image = None
    print("Warning: OCR module not found. Text extraction from images will not work.")

# 1. INITIALIZE FLASK APP (This was missing or misplaced)
app = Flask(__name__)

# 2. CONFIGURE APP
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max size

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 3. DEFINE ROUTES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # A. Generate Hash
        file_hash = calculate_hash(filepath)
        
        # B. Extract Metadata
        metadata = get_exif_data(filepath)
        
        # C. OCR & CRIME CHECK (The New Logic)
        # If metadata is basically empty (just returns "Status"), try OCR
        if "Status" in metadata or len(metadata) < 2:
            if extract_text_from_image:
                print(f"Metadata missing for {filename}. Attempting OCR...")
                ocr_text = extract_text_from_image(filepath)
                
                if ocr_text:
                    # Scan the extracted text for crimes
                    crime_results = scan_text_for_crime(ocr_text)
                    
                    # Add findings to the report
                    metadata["[FORENSIC NOTE]"] = "Metadata scrubbed. Performed OCR extraction."
                    metadata["[EXTRACTED TEXT]"] = ocr_text[:300] + "..." # Show preview
                    
                    if crime_results:
                        for cat, keywords in crime_results.items():
                            metadata[f"[ALERT: {cat.upper()}]"] = ", ".join(keywords)
            else:
                 metadata["[FORENSIC NOTE]"] = "Metadata scrubbed. OCR module not available."

        return render_template('report.html', 
                             evidence_type="Image Forensics (Metadata + OCR)", 
                             target=filename, 
                             hash_val=file_hash, 
                             data=metadata)

@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    text_input = request.form['text_content']
    
    # Analyze Text
    results = scan_text_for_crime(text_input)
    
    # Format results for the report
    formatted_results = {}
    if results:
        for category, keywords in results.items():
            formatted_results[category.upper()] = ", ".join(keywords)
    else:
        formatted_results = None

    return render_template('report.html', 
                         evidence_type="Text Keyword Analysis", 
                         target="Manual Text Input", 
                         hash_val="N/A", 
                         data=formatted_results)

if __name__ == '__main__':
    app.run(debug=True)