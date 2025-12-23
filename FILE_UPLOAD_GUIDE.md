# 📤 File Upload Feature - Research Log Generator

## Fitur Baru: Auto-Upload & Auto-Naming

### ✨ Apa yang Baru?

Form generator sekarang mendukung **upload file langsung** dengan penamaan otomatis berdasarkan **Log ID**.

---

## 📋 Cara Menggunakan

### 1. **Upload Gambar (Image)**

#### Opsi A: Upload File Baru
1. Isi **LOG ID** terlebih dahulu (contoh: `003`)
2. Di bagian "FILE UPLOADS", klik tombol **"Choose File"** pada "UPLOAD IMAGE"
3. Pilih gambar dari komputer Anda (PNG, JPG, JPEG, GIF, WEBP)
4. File akan otomatis diberi nama: `{log_id}-arch.{ext}`
   - Contoh: Log ID `003` + upload `diagram.png` → disimpan sebagai `003-arch.png`
5. Preview gambar akan muncul langsung

#### Opsi B: Manual (File Sudah Ada)
- Jika file sudah ada di folder `assets/img/`, cukup isi nama file secara manual
- Contoh: `003-arch.png`

**Lokasi penyimpanan:** `/assets/img/`

---

### 2. **Upload PDF**

#### Opsi A: Upload File Baru
1. Isi **LOG ID** terlebih dahulu
2. Klik tombol **"Choose File"** pada "UPLOAD PDF"
3. Pilih file PDF dari komputer Anda
4. File akan otomatis diberi nama: `{log_id}-annotated.pdf`
   - Contoh: Log ID `003` → disimpan sebagai `003-annotated.pdf`
5. Info PDF akan muncul (nama & ukuran file)

#### Opsi B: Manual (File Sudah Ada)
- Jika PDF sudah ada di folder `assets/pdf/`, isi nama file secara manual
- Contoh: `003-annotated.pdf`

**Lokasi penyimpanan:** `/assets/pdf/`

---

## 🎯 Contoh Workflow

### Scenario: Membuat Paper Log #005

1. **Isi LOG ID:** `005`
2. **Upload Image:**
   - Pilih file: `system_overview.png` (2.3 MB)
   - Otomatis disimpan sebagai: `005-arch.png`
   - Preview muncul di form
3. **Upload PDF:**
   - Pilih file: `paper_notes.pdf` (1.8 MB)
   - Otomatis disimpan sebagai: `005-annotated.pdf`
   - Info muncul: "✓ PDF Selected: paper_notes.pdf (1843.50 KB)"
4. Klik **"INITIATE BUILD SEQUENCE"**
5. Success page menampilkan:
   ```
   FILES UPLOADED:
   📷 Image: 005-arch.png
   📄 PDF: 005-annotated.pdf
   ```

---

## 📁 Struktur Folder

Setelah upload, struktur folder akan seperti ini:

```
Research-log/
├── assets/
│   ├── img/
│   │   ├── 001-arch.png
│   │   ├── 002-arch.jpg
│   │   └── 005-arch.png     ← File baru
│   └── pdf/
│       ├── 001-annotated.pdf
│       ├── 002-annotated.pdf
│       └── 005-annotated.pdf ← File baru
├── reviews/
│   └── 005-slam-paper.html  ← HTML hasil generate
└── papers.json
```

---

## 🔧 Technical Details

### Supported File Types

| Type | Extensions | Max Size |
|------|-----------|----------|
| **Image** | .png, .jpg, .jpeg, .gif, .webp | 16 MB |
| **PDF** | .pdf | 16 MB |

### Auto-Naming Convention

- **Image:** `{log_id}-arch.{extension}`
  - `001-arch.png`
  - `002-arch.jpg`
  
- **PDF:** `{log_id}-annotated.pdf`
  - `001-annotated.pdf`
  - `002-annotated.pdf`

### Validation

✅ File type checking (hanya format yang diizinkan)  
✅ File size limit (max 16MB per file)  
✅ Auto-create folders jika belum ada  
✅ Secure filename handling (prevent path traversal)

---

## 🎨 UI Features

### Image Upload
- ✅ Live preview dengan animasi fade-in
- ✅ File info (nama & ukuran)
- ✅ Drag & drop support (browser default)
- ✅ Visual feedback dengan glow effect

### PDF Upload
- ✅ File info display
- ✅ Green success indicator
- ✅ Ukuran file dalam KB

---

## 🚨 Troubleshooting

### Problem: "File too large"
**Solution:** Compress file atau gunakan file < 16MB

### Problem: "Invalid file type"
**Solution:** Pastikan format file sesuai (PNG/JPG untuk image, PDF untuk document)

### Problem: "Upload failed"
**Solution:** 
1. Pastikan folder `assets/img` dan `assets/pdf` ada
2. Check file permissions
3. Restart Flask server

### Problem: "Preview tidak muncul"
**Solution:** Browser cache issue - hard refresh (Ctrl+Shift+R)

---

## 🔄 Compatibility

| Feature | Status |
|---------|--------|
| Chrome/Edge | ✅ Full Support |
| Firefox | ✅ Full Support |
| Safari | ✅ Full Support |
| Mobile | ✅ Supported (dengan limitasi preview) |

---

## 📝 Notes

- **Upload bersifat opsional** - Anda tetap bisa isi manual jika file sudah ada
- **File lama akan ditimpa** jika log_id sama dan upload file baru
- **Pastikan log_id sudah diisi** sebelum upload agar penamaan konsisten
- Jika upload dan manual input keduanya diisi, **upload akan diprioritaskan**

---

## 🎯 Future Enhancements (Planned)

- [ ] Multiple image upload support
- [ ] Automatic image compression
- [ ] Drag & drop area visual indicator
- [ ] Upload progress bar
- [ ] File rename/delete dari UI
- [ ] Cloud storage integration (optional)

---

**Last Updated:** December 23, 2025  
**Version:** 2.0 - File Upload Support
