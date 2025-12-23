document.addEventListener('DOMContentLoaded', () => {

    /* --- 1. CUSTOM CURSOR & SLASH EFFECT --- */
    const cursor = document.querySelector('.cursor-follower');
    let isMoving = false;

    // Update posisi kursor
    document.addEventListener('mousemove', (e) => {
        if (!isMoving) {
            // Ubah bentuk jadi crosshair kecil saat mulai bergerak
            cursor.style.width = '10px';
            cursor.style.height = '10px';
            cursor.style.borderRadius = '0'; 
            isMoving = true;
        }
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';

        // 2. TAMBAHAN BARU: Kirim posisi X/Y ke Body CSS untuk Background
        const body = document.querySelector('body');
        body.style.setProperty('--x', e.clientX + 'px');
        body.style.setProperty('--y', e.clientY + 'px');
    });

    // Efek Sabetan Pedang saat klik
    document.addEventListener('click', () => {
        cursor.classList.add('cursor-slash');
        // Hapus kelas setelah animasi selesai (400ms sesuai CSS)
        setTimeout(() => {
            cursor.classList.remove('cursor-slash');
        }, 400);
    });


    /* --- 2. DYNAMIC SWORD SHEATH HEADER --- */
    const header = document.getElementById('main-header');
    const searchWrapper = document.getElementById('search-wrapper');
    const searchInput = document.getElementById('search-input');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            header.classList.add('shrunk');
        } else {
            header.classList.remove('shrunk');
            searchWrapper.classList.remove('expanded'); // Reset saat kembali ke atas
        }
    });

    // Logika ekspansi saat mode shrunk (pedang keluar dari sarung)
    searchWrapper.addEventListener('click', () => {
        if (header.classList.contains('shrunk')) {
            searchWrapper.classList.add('expanded');
            searchInput.focus();
        }
    });
    // Tutup kembali jika klik di luar
    document.addEventListener('click', (e) => {
        if (header.classList.contains('shrunk') && !searchWrapper.contains(e.target)) {
             searchWrapper.classList.remove('expanded');
        }
    });


    /* --- 3. VANILLA TILT INIT --- */
    // Inisialisasi efek 3D pada semua kartu
    VanillaTilt.init(document.querySelectorAll(".paper-card"), {
        max: 12,            // Maksimal kemiringan
        speed: 400,         // Kecepatan transisi
        glare: true,        // Efek kilau
        "max-glare": 0.3,   // Opasitas kilau
        scale: 1.02         // Sedikit zoom saat hover
    });


/* --- 4. DATA DIVE TRANSITION (UPDATED) --- */
    const morphTriggers = document.querySelectorAll('.js-trigger-morph');
    const overlay = document.getElementById('morph-overlay');

    morphTriggers.forEach(trigger => {
        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            const destination = this.getAttribute('href');
            
            // 1. Ambil posisi kartu
            const card = this.closest('.paper-card');
            const rect = card.getBoundingClientRect();

            // 2. Set posisi awal overlay TEPAT di tengah kartu
            overlay.style.width = rect.width + 'px';
            overlay.style.height = rect.height + 'px';
            overlay.style.top = rect.top + 'px';
            overlay.style.left = rect.left + 'px';
            
            // Reset transformasi sebelum animasi
            overlay.style.transform = 'scale(1)';
            overlay.style.opacity = '0.4'; // Mulai semi transparan
            overlay.style.borderRadius = '12px';

            // 3. Force Reflow
            void overlay.offsetWidth; 

            // 4. Jalankan "Zoom Dive"
            overlay.classList.add('morph-active');
            
            // 5. Pindah halaman sedikit lebih cepat agar terasa instan
            setTimeout(() => {
                window.location.href = destination;
            }, 500); 
        });
    });

    /* --- 5. FIRE PARTICLE ANIMATION --- */
    const canvas = document.createElement('canvas');
    canvas.id = 'bg-canvas';
    document.body.insertBefore(canvas, document.body.firstChild);
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Resize canvas saat window berubah ukuran
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });

    class FireParticle {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * canvas.width;
            this.y = canvas.height + Math.random() * 100;
            this.size = Math.random() * 3 + 1;
            this.speedY = Math.random() * 3 + 1;
            this.speedX = (Math.random() - 0.5) * 2;
            this.opacity = Math.random() * 0.5 + 0.5;
            // Warna merah api yang bervariasi
            const colorVariant = Math.floor(Math.random() * 3);
            if (colorVariant === 0) {
                this.color = `rgba(255, 50, 0, ${this.opacity})`; // Merah terang
            } else if (colorVariant === 1) {
                this.color = `rgba(255, 100, 0, ${this.opacity})`; // Orange
            } else {
                this.color = `rgba(255, 0, 0, ${this.opacity})`; // Merah murni
            }
        }

        update() {
            this.y -= this.speedY;
            this.x += this.speedX;
            this.opacity -= 0.003;
            this.size *= 0.99;

            // Reset particle jika keluar layar atau terlalu transparan
            if (this.y < -10 || this.opacity <= 0 || this.size < 0.5) {
                this.reset();
            }
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.globalAlpha = this.opacity;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
            
            // Tambahkan glow effect
            ctx.shadowBlur = 15;
            ctx.shadowColor = this.color;
        }
    }

    // Buat array partikel
    const particles = [];
    const particleCount = 150; // Jumlah partikel api
    for (let i = 0; i < particleCount; i++) {
        particles.push(new FireParticle());
    }

    // Animasi loop
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });

        requestAnimationFrame(animate);
    }

    animate();
});
// Background canvas animation added - fire particles effect