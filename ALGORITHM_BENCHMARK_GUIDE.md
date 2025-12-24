# 🚀 New Features: Algorithm Logic & Performance Benchmark

## ✨ What's New?

Sistem Paper Research Log telah diupgrade dengan **2 fitur baru** yang krusial untuk dokumentasi paper:

### 1. **ALGORITHM CORE LOGIC** 📝
Dokumentasi langkah-langkah algoritma utama paper dalam format code-style.

### 2. **SYSTEM DIAGNOSTICS** (Performance Benchmark) 📊
Perbandingan performa metode Anda vs baseline/competitor dalam format HUD.

---

## 📋 Cara Menggunakan

### 1. Algorithm Logic

#### Di Form (templates/form.html):
Temukan bagian **"ALGORITHM CORE LOGIC"** dan isi textarea dengan langkah-langkah algoritma:

```
1. Initialize pose estimation from previous frame
2. Extract ORB features from current image
3. Match features with map points using RANSAC
4. Optimize camera pose using bundle adjustment
5. Update local map with new keyframes
6. Detect loop closure candidates
7. Perform global optimization if loop detected
```

**Tips:**
- Satu langkah per baris
- Bisa pseudocode atau deskripsi step-by-step
- Numbering otomatis di output
- Gunakan bahasa yang clear dan concise

#### Output Display:
- **Lokasi:** Kolom Kiri (Main Content), setelah Executive Summary
- **Style:** Terminal/Code Editor dengan:
  - Background hitam pekat (#0a0a0a)
  - Font monospace (JetBrains Mono)
  - Line numbers di kiri
  - Syntax highlighting (green text)
  - Border merah subtle
  - Status footer dengan jumlah steps

---

### 2. Performance Benchmark

#### Di Form (templates/form.html):
Temukan bagian **"PERFORMANCE BENCHMARK"** dan isi dengan format CSV:

```
Format: Metric Name | Our Score | Competitor Score
```

**Contoh:**
```
ATE RMSE (cm) | 0.30 | 2.15
RPE Translation (%) | 0.18 | 1.42
Loop Closure Recall (%) | 95.3 | 87.1
Tracking Success Rate (%) | 99.2 | 94.8
Runtime (ms/frame) | 28 | 45
Memory Usage (MB) | 156 | 203
```

**Format Rules:**
- Pisahkan kolom dengan `|` (pipe symbol)
- Metric Name | Score Kita | Score Baseline/SOTA
- Spasi akan otomatis dibersihkan
- Bisa pakai satuan dalam kurung

#### Output Display:
- **Lokasi:** Kolom Kanan (Sidebar), setelah Attribute Radar
- **Style:** HUD/Dashboard dengan:
  - Background dark dengan border pulse
  - Green box untuk "OURS" (winning score)
  - Red box untuk "BASELINE" (competitor)
  - Live metrics indicator
  - Record counter di footer

---

## 🎨 Design Details

### Algorithm Logic Section
```css
Design: Terminal/Code Editor Style
├── Header: "// ALGORITHM_CORE.execute()" (red text)
├── Content Area:
│   ├── Background: Pure black (#0a0a0a)
│   ├── Line numbers: Gray, right-aligned
│   ├── Code text: Bright green (#00ff88)
│   ├── Border: Red subtle left border per line
│   └── Font: JetBrains Mono, monospace
└── Footer: Status bar dengan step count
```

### Performance Benchmark Section
```css
Design: HUD/Diagnostic Display
├── Header: "SYSTEM_DIAGNOSTICS" dengan pulse indicator
├── Each Metric Row:
│   ├── Metric name: Gray, small caps
│   ├── Our Score Box:
│   │   ├── Background: Green tint (#0f0 5% opacity)
│   │   ├── Border: Green (#0f0 30% opacity)
│   │   ├── Text: Bright green dengan glow
│   │   └── Label: "OURS"
│   └── Competitor Score Box:
│       ├── Background: Red tint (#f87171 5% opacity)
│       ├── Border: Red (#f87171 30% opacity)
│       ├── Text: Red
│       └── Label: "BASELINE"
└── Footer: Live status dengan record count
```

---

## 🔧 Backend Processing

### Algorithm Logic (app.py)
```python
# Input dari textarea
algorithm_logic = """
1. Initialize system
2. Process data
3. Output results
"""

# Proses menjadi list
paper_data['algorithm_logic'] = [
    step.strip() 
    for step in data.get('algorithm_logic', '').split('\n') 
    if step.strip()
]

# Output: ['1. Initialize system', '2. Process data', '3. Output results']
```

### Performance Benchmark (app.py)
```python
# Input dari textarea (CSV format)
benchmark_text = """
ATE RMSE (cm) | 0.30 | 2.15
Runtime (ms) | 28 | 45
"""

# Parse dengan fungsi parse_benchmark()
benchmarks = [
    {
        'metric': 'ATE RMSE (cm)',
        'ours': '0.30',
        'competitor': '2.15'
    },
    {
        'metric': 'Runtime (ms)',
        'ours': '28',
        'competitor': '45'
    }
]
```

**Fungsi parse_benchmark():**
- Split per baris (`\n`)
- Split per kolom (`|`)
- Clean whitespace dengan `.strip()`
- Return list of dictionaries
- Handle missing columns (default `-`)

---

## 📸 Visual Preview

### Algorithm Core Display
```
┌─────────────────────────────────────────────┐
│ // ALGORITHM_CORE.execute()                 │
├─────────────────────────────────────────────┤
│  1  │ Initialize pose estimation            │
│  2  │ Extract ORB features                  │
│  3  │ Match with map points                 │
│  4  │ Optimize camera pose                  │
│  5  │ Update local map                      │
├─────────────────────────────────────────────┤
│ ● CORE_ALGORITHM_LOADED ✓ 5 STEPS          │
└─────────────────────────────────────────────┘
```

### System Diagnostics Display
```
┌─────────────────────────────────────────────┐
│ ● SYSTEM_DIAGNOSTICS                        │
├─────────────────────────────────────────────┤
│ ATE RMSE (cm)                               │
│ ┌──────────┐  ┌──────────┐                 │
│ │ OURS     │  │ BASELINE │                 │
│ │ 0.30 ✓   │  │ 2.15     │                 │
│ └──────────┘  └──────────┘                 │
│                                             │
│ Runtime (ms/frame)                          │
│ ┌──────────┐  ┌──────────┐                 │
│ │ OURS     │  │ BASELINE │                 │
│ │ 28 ✓     │  │ 45       │                 │
│ └──────────┘  └──────────┘                 │
├─────────────────────────────────────────────┤
│ ● LIVE_METRICS          2 RECORDS          │
└─────────────────────────────────────────────┘
```

---

## 🎯 Example Workflow

### Input di Form:

**Algorithm Logic:**
```
1. Extract keypoints using ORB detector (500 features/frame)
2. Build vocabulary tree from training sequences
3. Compute BoW vectors for place recognition
4. Track features across consecutive frames
5. Triangulate 3D map points from stereo pairs
6. Perform local bundle adjustment every 10 keyframes
7. Detect loop closures using DBoW2 similarity score
8. Optimize pose graph with g2o when loop detected
```

**Performance Benchmark:**
```
ATE RMSE (cm) | 0.34 | 2.18
RPE Rotation (deg/m) | 0.0025 | 0.0087
Loop Closure Precision (%) | 98.7 | 89.2
Avg Runtime (ms/frame) | 31 | 52
Peak Memory (MB) | 248 | 412
Initialization Time (s) | 1.2 | 3.8
```

### Output di Paper Review:

**Algorithm Section** → Clean code-style display dengan 8 numbered steps  
**Benchmark Section** → HUD dengan 6 metric comparisons (green vs red)

---

## 🔍 Data Validation

### Optional Fields
Kedua fitur ini **opsional**. Jika tidak diisi:
- Section tidak akan ditampilkan di output
- Menggunakan Jinja2 `{% if %}` conditional
- No errors, graceful degradation

### Error Handling
- Empty lines diabaikan
- Incomplete benchmark rows (< 3 columns) → skip atau default '-'
- Whitespace otomatis di-strip
- Safe untuk input kosong

---

## 📊 Database Storage

Data disimpan di `papers.json`:

```json
{
  "log_id": "003",
  "title": "ORB-SLAM3...",
  "algorithm_logic": [
    "1. Extract keypoints using ORB detector",
    "2. Build vocabulary tree",
    "..."
  ],
  "performance_benchmark": [
    {
      "metric": "ATE RMSE (cm)",
      "ours": "0.34",
      "competitor": "2.18"
    },
    {
      "metric": "Runtime (ms/frame)",
      "ours": "31",
      "competitor": "52"
    }
  ]
}
```

---

## 🎨 Color Scheme

| Element | Color | Hex/RGBA |
|---------|-------|----------|
| Algorithm background | Pure black | #0a0a0a |
| Line numbers | Dark gray | #666 |
| Code text | Bright green | #00ff88 |
| Border accent | Red | rgba(255,26,26,0.2) |
| Our score box | Green tint | rgba(0,255,100,0.05) |
| Baseline box | Red tint | rgba(255,50,50,0.05) |
| Our score text | Neon green | #0f0 |
| Baseline text | Light red | #f87171 |
| Status indicator | Pulse green | #0f0 (animated) |

---

## 🚀 Quick Start

1. **Jalankan server:**
   ```bash
   ./start-upload.sh
   ```

2. **Isi form:**
   - Scroll ke section "ALGORITHM CORE LOGIC"
   - Tulis steps (satu per baris)
   - Scroll ke "PERFORMANCE BENCHMARK"
   - Isi dengan format: `Metric | Ours | Competitor`

3. **Submit & Review:**
   - Klik "INITIATE BUILD SEQUENCE"
   - Buka generated HTML
   - Algorithm muncul setelah Summary
   - Benchmark muncul di sidebar setelah Radar

---

## 🎭 Advanced Tips

### Algorithm Logic
- Gunakan numbering konsisten (1. 2. 3. atau • • •)
- Tambahkan detail teknis di dalam kurung
- Pisahkan major steps vs sub-steps
- Bisa pakai pseudocode syntax

### Performance Benchmark
- Lower is better? Label jelas di metric name
- Tambahkan satuan dalam kurung
- Bandingkan dengan paper yang sama (fair comparison)
- Prioritaskan metrics yang penting (top 5-8)

---

**Version:** 3.0 - Algorithm & Benchmark Update  
**Date:** December 24, 2025  
**Compatibility:** All browsers, Mobile responsive
