# 🔥 Research Log - Paper Review System

Cyberpunk-themed paper research database with neon red aesthetics.

## 🚀 Quick Start

### View Papers (Web Interface)
```bash
./start.sh
```
Then open: http://localhost:8000/index.html

### Generate New Paper (with File Upload Support) ✨ NEW
```bash
./start-upload.sh
# atau
./generator.sh
```
Then open: http://localhost:5000/

**🆕 Fitur Baru:**
- 📤 Upload gambar dengan auto-naming (`{log_id}-arch.png`)
- 📄 Upload PDF dengan auto-naming (`{log_id}-annotated.pdf`)
- 👀 Live preview untuk gambar yang diupload
- 💾 Max file size: 16MB

## 📁 File Structure
```
Research-log/
├── index.html              # Main page (displays all papers)
├── papers.json             # Database of papers
├── app.py                  # Paper generator (Flask) ✨ Updated
├── reviews/                # Generated paper review HTML files
├── assets/
│   ├── img/               # Uploaded images (auto-named)
│   └── pdf/               # Uploaded PDFs (auto-named)
├── templates/
│   └── form.html          # Generator form ✨ Updated
├── start.sh               # Quick start web server
├── generator.sh           # Quick start paper generator (old)
└── start-upload.sh        # Quick start with upload support ✨ NEW
```

## 🎯 Workflow

### 1. Generate Paper with File Upload
1. Run `./start-upload.sh` atau `./generator.sh`
2. Open http://localhost:5000
3. Fill form dengan data paper
4. **Upload files** (opsional):
   - Pilih image → otomatis jadi `{log_id}-arch.{ext}`
   - Pilih PDF → otomatis jadi `{log_id}-annotated.pdf`
5. Click "INITIATE BUILD SEQUENCE"
6. Files tersimpan di:
   - Images: `assets/i (Mobile optimized)
- 📤 **File upload with auto-naming** ✨ NEW
- 👀 **Live image preview** ✨ NEW
- 💾 **Smart file management** ✨ NEW

## 📱 Mobile Optimization

Website sudah dioptimalkan untuk Android/iOS:
- ✅ Responsive grid layout
- ✅ Touch-friendly interactions
- ✅ Performance optimizations
- ✅ Disabled heavy effects on mobile

Lihat: [MOBILE_OPTIMIZATION.md](MOBILE_OPTIMIZATION.md)

## 📚 Documentation

- [File Upload Guide](FILE_UPLOAD_GUIDE.md) - Cara menggunakan fitur upload
- [Mobile Optimization](MOBILE_OPTIMIZATION.md) - Detail optimasi mobilemg/`
   - PDFs: `assets/pdf/`

### 2. View Papers
1. Run `./start.sh`
2. Open http://localhost:8000/index.html
3. Papers akan tampil dengan data dari `papers.json`

### 3. Update GitHub
```bash
git add .
git commit -m "Add new paper with uploads"
git push
```

## 📤 File Upload Feature

Lihat dokumentasi lengkap di: [FILE_UPLOAD_GUIDE.md](FILE_UPLOAD_GUIDE.md)

**Supported Formats:**
- Images: PNG, JPG, JPEG, GIF, WEBP
- Documents: PDF
- Max size: 16MB per file

**Auto-Naming:**
- Image: `{log_id}-arch.{extension}`
- PDF: `{log_id}-annotated.pdf`

Contoh: Log ID `003` + upload `diagram.png` → `003-arch.png`

## 🎨 Features
- 🔥 Fire particle background animation
- 💡 Neon red glowing text effects
- 📊 Dynamic radar charts for each paper
- 🔍 Search functionality
- 📱 Responsive design (Mobile optimized)
- 📤 **File upload with auto-naming**
- 👀 **Live image preview**
- 💾 **Smart file management**
- 📝 **Algorithm Core Logic display** ✨ NEWEST
- 🎯 **Performance Benchmark HUD** ✨ NEWEST

## 📱 Mobile Optimization

Website sudah dioptimalkan untuk Android/iOS:
- ✅ Responsive grid layout
- ✅ Touch-friendly interactions
- ✅ Performance optimizations
- ✅ Disabled heavy effects on mobile

Lihat: [MOBILE_OPTIMIZATION.md](MOBILE_OPTIMIZATION.md)

## 📚 Documentation

- [File Upload Guide](FILE_UPLOAD_GUIDE.md) - Cara menggunakan fitur upload
- [Mobile Optimization](MOBILE_OPTIMIZATION.md) - Detail optimasi mobile
- [Algorithm & Benchmark Guide](ALGORITHM_BENCHMARK_GUIDE.md) - Fitur Algorithm Logic & Performance Benchmark ✨ NEW

---
*Press Ctrl+C to stop any running server*
