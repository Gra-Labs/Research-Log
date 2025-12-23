from flask import Flask, render_template, request, redirect, url_for
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER_IMG = 'assets/img'
UPLOAD_FOLDER_PDF = 'assets/pdf'
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
ALLOWED_PDF_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER_IMG'] = UPLOAD_FOLDER_IMG
app.config['UPLOAD_FOLDER_PDF'] = UPLOAD_FOLDER_PDF
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB per file

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Fungsi untuk menghitung titik polygon Radar Chart
def calculate_radar_points(math, code, hw, novelty):
    # Mapping nilai 0-100 ke koordinat SVG box 100x100 (Center 50,50)
    # Radius chart = 40 unit
    p_math_y = 50 - (int(math) / 100 * 40)    # Top
    p_code_x = 50 + (int(code) / 100 * 40)    # Right
    p_hw_y = 50 + (int(hw) / 100 * 40)        # Bottom
    p_nov_x = 50 - (int(novelty) / 100 * 40)  # Left
    return f"50,{p_math_y} {p_code_x},50 50,{p_hw_y} {p_nov_x},50"

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    log_id = data['log_id']
    
    # Handle Image Upload
    image_filename = data.get('image_file', '')  # Manual input
    if 'image_upload' in request.files:
        image_file = request.files['image_upload']
        if image_file and image_file.filename != '' and allowed_file(image_file.filename, ALLOWED_IMAGE_EXTENSIONS):
            # Get file extension
            file_ext = image_file.filename.rsplit('.', 1)[1].lower()
            # Create filename with log_id prefix
            image_filename = f"{log_id}-arch.{file_ext}"
            # Save file
            os.makedirs(UPLOAD_FOLDER_IMG, exist_ok=True)
            image_file.save(os.path.join(UPLOAD_FOLDER_IMG, image_filename))
    
    # Handle PDF Upload
    pdf_filename = data.get('pdf_file', '')  # Manual input
    if 'pdf_upload' in request.files:
        pdf_file = request.files['pdf_upload']
        if pdf_file and pdf_file.filename != '' and allowed_file(pdf_file.filename, ALLOWED_PDF_EXTENSIONS):
            # Create filename with log_id prefix
            pdf_filename = f"{log_id}-annotated.pdf"
            # Save file
            os.makedirs(UPLOAD_FOLDER_PDF, exist_ok=True)
            pdf_file.save(os.path.join(UPLOAD_FOLDER_PDF, pdf_filename))
    
    # 1. Siapkan Data
    paper_data = {
        "log_id": log_id,
        "filename": data['filename'],
        "title": data['title'],
        "authors": data['authors'],
        "publication": data['publication'],
        "tags": [t.strip() for t in data['tags'].split(',')],
        "summary_problem": data['summary_problem'],
        "summary_solution": data['summary_solution'],
        "summary_result": data['summary_result'],
        # Memecah text area per baris menjadi list
        "strengths": [s.strip() for s in data['strengths'].split('\n') if s.strip()],
        "weaknesses": [w.strip() for w in data['weaknesses'].split('\n') if w.strip()],
        "score_math": data['score_math'],
        "score_code": data['score_code'],
        "score_hw": data['score_hw'],
        "score_novelty": data['score_novelty'],
        "radar_points": calculate_radar_points(data['score_math'], data['score_code'], data['score_hw'], data['score_novelty']),
        "dataset": data['dataset'],
        "method_tech": data['method_tech'],
        "video_id": data['video_id'],
        "image_file": image_filename,
        "image_caption": data['image_caption'],
        "pdf_file": pdf_filename,
        "bibtex": data['bibtex']
    }

    # 2. Render HTML
    rendered_html = render_template('paper_master.html', **paper_data)

    # 3. Simpan File HTML ke folder reviews
    output_path = os.path.join('reviews', data['filename'])
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    # 4. Update Database (papers.json) - Opsional, untuk arsip
    json_path = 'papers.json'
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            try:
                db = json.load(f)
            except:
                db = []
    else:
        db = []
    
    db.append(paper_data)
    with open(json_path, 'w') as f:
        json.dump(db, f, indent=4)

    # Prepare upload info for success page
    upload_info = []
    if image_filename:
        upload_info.append(f"📷 Image: {image_filename}")
    if pdf_filename:
        upload_info.append(f"📄 PDF: {pdf_filename}")
    
    upload_status = "<br>".join(upload_info) if upload_info else "No files uploaded"

    # Return stylish success page
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OPERATION SUCCESS</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            background: linear-gradient(to bottom, #0a0000, #1a0000, #0a0000);
            color: #ffffff;
            font-family: 'JetBrains Mono', 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            animation: bgPulse 8s ease-in-out infinite;
        }}

        @keyframes bgPulse {{
            0%, 100% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
        }}

        body::before {{
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: -1;
            background-image: 
                linear-gradient(rgba(255, 26, 26, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 26, 26, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: fireGrid 4s linear infinite;
            opacity: 0.3;
        }}

        @keyframes fireGrid {{
            0%, 100% {{ 
                background-position: 0 0;
                opacity: 0.2;
            }}
            50% {{ 
                background-position: 25px 25px;
                opacity: 0.4;
            }}
        }}

        .success-container {{
            text-align: center;
            padding: 60px 40px;
            background: rgba(5, 5, 5, 0.9);
            border: 2px solid #ff3333;
            box-shadow: 
                0 0 30px rgba(255, 51, 51, 0.3),
                0 0 60px rgba(255, 51, 51, 0.2),
                inset 0 0 30px rgba(255, 51, 51, 0.1);
            max-width: 600px;
            animation: slideIn 0.6s ease-out;
            position: relative;
        }}

        @keyframes slideIn {{
            0% {{
                opacity: 0;
                transform: translateY(-50px) scale(0.9);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0) scale(1);
            }}
        }}

        .success-icon {{
            font-size: 80px;
            margin-bottom: 20px;
            animation: iconPulse 2s ease-in-out infinite;
            filter: drop-shadow(0 0 20px rgba(255, 51, 51, 0.8));
        }}

        @keyframes iconPulse {{
            0%, 100% {{
                transform: scale(1);
                filter: drop-shadow(0 0 20px rgba(255, 51, 51, 0.8));
            }}
            50% {{
                transform: scale(1.1);
                filter: drop-shadow(0 0 40px rgba(255, 51, 51, 1));
            }}
        }}

        h1 {{
            color: #ff3333;
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 
                0 0 10px rgba(255, 51, 51, 0.8),
                0 0 20px rgba(255, 51, 51, 0.6),
                0 0 30px rgba(255, 51, 51, 0.4),
                0 0 40px rgba(255, 51, 51, 0.2);
            animation: neonPulse 2s ease-in-out infinite;
            letter-spacing: 2px;
        }}

        @keyframes neonPulse {{
            0%, 100% {{
                text-shadow: 
                    0 0 10px rgba(255, 51, 51, 0.8),
                    0 0 20px rgba(255, 51, 51, 0.6),
                    0 0 30px rgba(255, 51, 51, 0.4);
            }}
            50% {{
                text-shadow: 
                    0 0 15px rgba(255, 51, 51, 1),
                    0 0 30px rgba(255, 51, 51, 0.8),
                    0 0 45px rgba(255, 51, 51, 0.6),
                    0 0 60px rgba(255, 51, 51, 0.4);
            }}
        }}

        .status {{
            color: #00ff00;
            font-size: 1.2rem;
            margin-bottom: 15px;
            text-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
            font-weight: bold;
        }}

        .file-path {{
            background: rgba(0, 0, 0, 0.5);
            padding: 15px;
            border-left: 3px solid #ff3333;
            margin: 20px 0;
            font-size: 0.9rem;
            color: #cccccc;
            text-align: left;
            word-break: break-all;
        }}

        .file-path strong {{
            color: #ff3333;
            text-shadow: 0 0 5px rgba(255, 51, 51, 0.5);
        }}

        .buttons {{
            display: flex;
            gap: 15px;
            margin-top: 30px;
            flex-wrap: wrap;
            justify-content: center;
        }}

        .btn {{
            padding: 15px 30px;
            text-decoration: none;
            font-weight: bold;
            border: 2px solid #ff3333;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.9rem;
        }}

        .btn-primary {{
            background: #ff3333;
            color: #000;
            box-shadow: 
                0 0 10px rgba(255, 51, 51, 0.5),
                0 0 20px rgba(255, 51, 51, 0.3);
        }}

        .btn-primary:hover {{
            background: #ff0000;
            box-shadow: 
                0 0 20px rgba(255, 51, 51, 0.8),
                0 0 40px rgba(255, 51, 51, 0.6),
                0 0 60px rgba(255, 51, 51, 0.4);
            transform: scale(1.05);
        }}

        .btn-secondary {{
            background: transparent;
            color: #ff3333;
        }}

        .btn-secondary:hover {{
            background: rgba(255, 51, 51, 0.2);
            box-shadow: 0 0 15px rgba(255, 51, 51, 0.5);
        }}

        .timer {{
            margin-top: 20px;
            font-size: 0.8rem;
            color: #888;
        }}
    </style>
</head>
<body>
    <div class="success-container">
        <div class="success-icon">✓</div>
        <h1>[ OPERATION SUCCESS ]</h1>
        <p class="status">// PROTOCOL EXECUTED SUCCESSFULLY</p>
        
        <div class="file-path">
            <strong>OUTPUT LOCATION:</strong><br>
            {output_path}
        </div>

        <div class="file-path">
            <strong>FILENAME:</strong> {data['filename']}<br>
            <strong>PAPER ID:</strong> #{data['log_id']}<br>
            <strong>TITLE:</strong> {data['title'][:50]}{'...' if len(data['title']) > 50 else ''}<br>
            <br>
            <strong>FILES UPLOADED:</strong><br>
            {upload_status}
        </div>

        <div class="buttons">
            <a href="/" class="btn btn-primary">CREATE ANOTHER LOG</a>
            <a href="/{output_path}" class="btn btn-secondary">VIEW GENERATED FILE</a>
        </div>

        <p class="timer">Redirecting to home in <span id="countdown">10</span>s...</p>
    </div>

    <script>
        // Fire Particle Animation
        const canvas = document.createElement('canvas');
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.zIndex = '-2';
        canvas.style.pointerEvents = 'none';
        canvas.style.opacity = '0.4';
        canvas.style.mixBlendMode = 'screen';
        document.body.insertBefore(canvas, document.body.firstChild);

        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }});

        class FireParticle {{
            constructor() {{
                this.reset();
            }}

            reset() {{
                this.x = Math.random() * canvas.width;
                this.y = canvas.height + Math.random() * 100;
                this.size = Math.random() * 3 + 1;
                this.speedY = Math.random() * 3 + 1;
                this.speedX = (Math.random() - 0.5) * 2;
                this.opacity = Math.random() * 0.5 + 0.5;
                const colorVariant = Math.floor(Math.random() * 3);
                if (colorVariant === 0) {{
                    this.color = `rgba(255, 50, 0, ${{this.opacity}})`;
                }} else if (colorVariant === 1) {{
                    this.color = `rgba(255, 100, 0, ${{this.opacity}})`;
                }} else {{
                    this.color = `rgba(255, 0, 0, ${{this.opacity}})`;
                }}
            }}

            update() {{
                this.y -= this.speedY;
                this.x += this.speedX;
                this.opacity -= 0.003;
                this.size *= 0.99;

                if (this.y < -10 || this.opacity <= 0 || this.size < 0.5) {{
                    this.reset();
                }}
            }}

            draw() {{
                ctx.fillStyle = this.color;
                ctx.globalAlpha = this.opacity;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 15;
                ctx.shadowColor = this.color;
            }}
        }}

        const particles = [];
        const particleCount = 150;
        for (let i = 0; i < particleCount; i++) {{
            particles.push(new FireParticle());
        }}

        function animate() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(particle => {{
                particle.update();
    os.makedirs('reviews', exist_ok=True)
    os.makedirs('assets/img', exist_ok=True)
    os.makedirs('assets/pdf', exist_ok=True
            requestAnimationFrame(animate);
        }}

        animate();

        // Countdown timer
        let seconds = 10;
        const countdownEl = document.getElementById('countdown');
        const timer = setInterval(() => {{
            seconds--;
            countdownEl.textContent = seconds;
            if (seconds <= 0) {{
                clearInterval(timer);
                window.location.href = '/';
            }}
        }}, 1000);
    </script>
</body>
</html>
    """

if __name__ == '__main__':
    # Pastikan folder ada
    if not os.path.exists('reviews'):
        os.makedirs('reviews')
    app.run(debug=True, port=5000)