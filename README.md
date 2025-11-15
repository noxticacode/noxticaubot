# PyroUbot

<div align="center">
  <img src="https://img.shields.io/github/stars/noxticacode/noxticaubot?style=for-the-badge&logo=github" alt="Stars">
  <img src="https://img.shields.io/github/forks/noxticacode/noxticaubot?style=for-the-badge&logo=github" alt="Forks">
  <img src="https://img.shields.io/github/issues/noxticacode/noxticaubot?style=for-the-badge&logo=github" alt="Issues">
  <img src="https://img.shields.io/github/license/noxticacode/noxticaubot?style=for-the-badge&logo=github" alt="License">
  <br>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Pyrogram-2.0+-red?style=for-the-badge&logo=telegram" alt="Pyrogram">
  <img src="https://img.shields.io/badge/MongoDB-Cloud-green?style=for-the-badge&logo=mongodb" alt="MongoDB">
</div>

---

## Tentang PyroUbot

PyroUbot adalah bot Telegram yang powerful dan multifungsi yang dibangun menggunakan Pyrogram dan PyTgCalls. Bot ini dirancang untuk mengelola userbot Telegram secara otomatis dengan fitur-fitur canggih dan sistem plugin yang modular.

### Keunggulan Utama

- Performa Tinggi: Menggunakan Pyrogram untuk API Telegram yang stabil
- Voice & Video Calls: Dukungan panggilan suara dan video melalui PyTgCalls
- Multi-Userbot: Kelola hingga 100 userbot secara bersamaan
- Plugin System: Sistem plugin modular untuk kemudahan pengembangan
- Auto Cleanup: Pembersihan otomatis userbot yang expired
- Monitoring: Sistem monitoring dan logging yang comprehensive
- Entertainment: Berbagai fitur hiburan dan utility

---

## Quick Start

### Persyaratan Sistem

| Komponen | Versi Minimum | Keterangan |
|----------|---------------|------------|
| Python | 3.10+ | Runtime utama |
| Node.js | Latest | Untuk UglifyJS |
| MongoDB | 4.0+ | Database penyimpanan |
| RAM | 512MB+ | Minimum untuk operasi |
| Storage | 1GB+ | Untuk cache dan logs |

### Instalasi Cepat

```bash
# Clone repository
git clone https://github.com/noxticacode/noxticaubot.git
cd noxticaubot

# Install dependencies
pip install -r requirements.txt
npm install -g uglify-js

# Setup environment
cp sample.env .env
# Edit .env dengan kredensial Anda

# Jalankan bot
python3 -m PyroUbot
```

---

## Daftar Fitur Lengkap

### Userbot Management
- Multi-account management (hingga 100 bot)
- Auto-login dan session management
- Userbot expiration monitoring
- Bulk userbot operations
- Session backup dan restore
- Userbot statistics dan analytics

### Media & Entertainment
- Music Player: Spotify, YouTube, SoundCloud, Deezer
- Video Calls: Group voice/video calls dengan PyTgCalls
- Media Downloader: Instagram, TikTok, YouTube, Twitter, Facebook
- Image Tools: Remove background, enhancer, converter, compressor
- Games: Tic-tac-toe, quiz, word games, mini-games
- Streaming: Live streaming support

### Utilities
- System Monitor: CPU, RAM, disk usage, network stats
- Weather: Real-time weather information
- Reminder: Scheduled notifications dan alarms
- Search: Google, Wikipedia, lyrics, news
- Converter: Currency, units, formats, file converter
- Notes: Personal notes, reminders, todo lists
- Calculator: Advanced calculator dengan scientific functions

### Administration
- Anti-Spam: Auto-mute/ban spammers dengan AI detection
- Group Management: Welcome messages, rules, moderation tools
- Broadcast: Mass messaging ke groups dan users
- Security: Anti-flood, anti-porn, content filtering
- Analytics: User statistics, group analytics, bot usage reports

### Creative Tools
- Logo Maker: Custom logo generator dengan templates
- Text Tools: Stylish text, fonts, ASCII art
- Image Editor: Filters, effects, stickers, memes
- Fun Features: Quotes, jokes, memes generator
- Text-to-Speech: Convert text to audio
- Speech-to-Text: Convert audio to text

### Developer Tools
- Code Runner: Execute code in multiple languages
- API Testing: Test REST APIs dan webhooks
- Database Tools: MongoDB query interface
- File Manager: Upload, download, manage files
- Backup Tools: Automatic backup system

---

## Instalasi Detail

### 1. Persiapan Sistem

```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Install Python 3.10+
sudo apt install python3.10 python3.10-venv -y

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install MongoDB (opsional, bisa pakai cloud)
sudo apt install mongodb -y
```

### 2. Setup Project

```bash
# Clone repository
git clone https://github.com/noxticacode/noxticaubot.git
cd noxticaubot

# Buat virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# atau venv\Scripts\activate  # Windows

# Install Python packages
pip install -r requirements.txt

# Install Node.js packages
npm install -g uglify-js
```

### 3. Konfigurasi Environment

```bash
# Copy template
cp sample.env .env

# Edit file .env
nano .env  # atau editor favorit Anda
```

**Isi file .env dengan:**

```env
# Bot Configuration
MAX_BOT=100
DEVS=6924389613
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OWNER_ID=6924389613

# Database
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/dbname

# APIs (opsional)
RMBG_API=your_removebg_api_key
OPENAI_API=your_openai_key

# Logging
BLACKLIST_CHAT=-1002125842026 -1002056443221
LOGS_MAKER_UBOT=-1002807087960
```

### 4. Mendapatkan Kredensial

#### Bot Token
1. Buka [@BotFather](https://t.me/botfather) di Telegram
2. Kirim `/newbot`
3. Ikuti instruksi untuk membuat bot
4. Copy token yang diberikan

#### API ID & Hash
1. Kunjungi https://my.telegram.org
2. Login dengan akun Telegram
3. Buat aplikasi baru
4. Copy API ID dan API Hash

#### MongoDB URL
- **Cloud**: Gunakan [MongoDB Atlas](https://cloud.mongodb.com)
- **Local**: `mongodb://localhost:27017/pyroubot`

### 5. Menjalankan Bot

```bash
# Development mode
python3 -m PyroUbot

# Production mode (recommended)
python3 -m PyroUbot > logs.txt 2>&1 &

# Using startup script
chmod +x start.sh
./start.sh
```

---

## Struktur Proyek

```
PyroUbot/
├── PyroUbot/
│   ├── __init__.py              # Bot initialization & configuration
│   ├── __main__.py              # Main entry point & startup logic
│   ├── config.py                # Environment variables & settings
│   └── core/
│       ├── database/            # Database operations & models
│       │   ├── __init__.py      # Database initialization
│       │   ├── ubot.py          # Userbot database operations
│       │   ├── vars.py          # Global variables & constants
│       │   └── mongo.py         # MongoDB connection & queries
│       ├── function/
│       │   ├── __init__.py      # Function utilities
│       │   ├── plugins.py       # Plugin loader & manager
│       │   ├── inline.py        # Inline query handlers
│       │   └── assistant.py     # AI assistant functions
│       └── helpers/
│           ├── __init__.py      # Helper utilities
│           ├── _cmd.py          # Command decorators & handlers
│           ├── formatter.py     # Text & message formatting
│           ├── misc.py          # Miscellaneous helper functions
│           ├── aiohttp.py       # HTTP client utilities
│           └── pyrogram.py      # Pyrogram-specific helpers
├── modules/                     # Plugin modules (200+ files)
│   ├── __init__.py              # Module initialization
│   ├── admin.py                 # Administrative commands
│   ├── music.py                 # Music player & controls
│   ├── downloader.py            # Media download utilities
│   ├── games.py                 # Games & entertainment
│   ├── utilities.py             # General utilities
│   ├── converter.py             # File & format converters
│   ├── search.py                # Search & information tools
│   ├── creative.py              # Creative & design tools
│   ├── security.py              # Security & moderation
│   └── ...                      # Additional modules
├── storage/                     # Static files & assets
│   ├── fonts/                   # Custom fonts
│   ├── templates/               # Template files
│   └── cache/                   # Temporary cache files
├── requirements.txt             # Python dependencies
├── sample.env                  # Environment template
├── start.sh                    # Startup script
├── installnode.sh              # Node.js installer script
├── unknown_errors.txt          # Error logging
├── cookies.txt                 # Session cookies
├── README.md                   # Project documentation
└── LICENSE                     # MIT License
```

### Penjelasan Struktur

- **PyroUbot/**: Core bot package
  - `__init__.py`: Bot initialization, imports, dan konfigurasi awal
  - `__main__.py`: Entry point utama, startup sequence
  - `config.py`: Environment variable parsing dan validasi

- **core/**: Core functionality
  - `database/`: Semua operasi database (MongoDB, Redis)
  - `function/`: Utility functions dan business logic
  - `helpers/`: Helper functions untuk common tasks

- **modules/**: Plugin system
  - Setiap file adalah modul independen
  - Modular design untuk kemudahan maintenance
  - Hot-reload capability untuk development

- **storage/**: Static assets
  - Fonts untuk text generation
  - Templates untuk various features
  - Cache untuk performance optimization

---

## Cara Penggunaan

### Setup Awal

1. **Start Bot**: Kirim `/start` ke bot untuk memulai
2. **Authentication**: Bot akan memverifikasi akses Anda
3. **Configuration**: Setup preferensi dan pengaturan

### Menambah Userbot

#### Metode 1: Via Bot Commands
```
/add_ubot - Mulai proses penambahan userbot baru
```

#### Metode 2: Manual Setup
1. Kirim `/add_ubot` ke bot
2. Bot akan meminta nomor telepon
3. Masukkan kode verifikasi dari Telegram
4. Bot akan membuat session otomatis
5. Userbot siap digunakan

### Kelola Userbot

#### Perintah Dasar
| Perintah | Deskripsi |
|----------|-----------|
| `/start` | Memulai bot dan menampilkan menu |
| `/help` | Menampilkan bantuan dan daftar perintah |
| `/ping` | Mengecek status dan respon bot |
| `/stats` | Menampilkan statistik penggunaan |
| `/ubot` | Menu utama pengelolaan userbot |

#### Perintah Admin
```
/add_ubot     - Tambah userbot baru
/del_ubot     - Hapus userbot tertentu
/list_ubot    - List semua userbot aktif
/restart      - Restart semua userbot
/backup       - Backup sessions dan data
/restore      - Restore dari backup
```

#### Perintah Musik
```
/play <query> - Putar musik dari YouTube/Spotify
/pause        - Pause musik yang sedang diputar
/resume       - Lanjutkan musik
/skip         - Skip ke lagu berikutnya
/queue        - Lihat antrian musik
/volume <1-100> - Atur volume
/lyrics       - Lihat lirik lagu
```

#### Perintah Utility
```
/weather <kota>    - Cek cuaca
/remind <waktu>    - Set pengingat
/translate <teks>  - Terjemahkan teks
/download <url>    - Download media
/calc <ekspresi>   - Kalkulator
/currency <amt> <from> <to> - Konversi mata uang
```

#### Perintah Moderation
```
/ban <user>        - Ban user dari group
/mute <user>       - Mute user
/warn <user>       - Beri warning
/kick <user>       - Kick user dari group
/purge <jumlah>    - Hapus pesan dalam jumlah banyak
```

### Inline Features

Bot juga mendukung inline queries untuk fitur cepat:

- `@botusername play <lagu>` - Cari dan putar musik
- `@botusername weather <kota>` - Cek cuaca
- `@botusername calc <ekspresi>` - Kalkulasi matematika
- `@botusername translate <teks>` - Terjemahkan teks

### Group Management

Untuk mengelola group dengan bot:

1. **Add Bot to Group**: Tambahkan bot sebagai admin
2. **Configure Permissions**: Berikan izin yang diperlukan
3. **Set Welcome Message**: Konfigurasi pesan welcome
4. **Enable Features**: Aktifkan fitur moderation

---

## Troubleshooting

### Masalah Umum dan Solusi

#### 1. Module Import Error
```
Error: No module named 'geopy'
Solusi: pip install geopy speedtest-cli pytimeparse
```

#### 2. MongoDB Connection Failed
```
Error: MongoDB connection timeout
Solusi:
- Periksa status MongoDB: sudo systemctl status mongodb
- Gunakan MongoDB Atlas cloud
- Update MONGO_URL di file .env
- Periksa firewall dan koneksi internet
```

#### 3. Bot Token Invalid
```
Error: ACCESS_TOKEN_EXPIRED
Solusi:
- Dapatkan token baru dari @BotFather
- Jangan bagikan token ke orang lain
- Regenerate token jika compromised
- Pastikan token dalam format yang benar
```

#### 4. API Credentials Invalid
```
Error: API_ID_INVALID atau API_HASH_INVALID
Solusi:
- Kunjungi https://my.telegram.org
- Login dengan akun Telegram
- Buat aplikasi baru jika perlu
- Copy API ID dan API Hash dengan benar
- Pastikan tidak ada spasi berlebih
```

#### 5. FloodWait Error
```
Error: FLOOD_WAIT_X
Solusi:
- Bot terkena rate limit Telegram
- Tunggu beberapa menit sesuai pesan error
- Kurangi frekuensi request
- Implementasi delay antara requests
- Gunakan beberapa akun jika perlu
```

#### 6. Session Expired
```
Error: AUTH_KEY_INVALID
Solusi:
- Hapus userbot yang expired
- Tambah userbot baru dengan /add_ubot
- Periksa masa aktif session
- Backup session sebelum expired
```

#### 7. Permission Denied
```
Error: CHAT_ADMIN_REQUIRED
Solusi:
- Jadikan bot sebagai admin di group
- Berikan izin yang diperlukan
- Periksa hak akses bot
- Gunakan bot di chat pribadi jika memungkinkan
```

### Logs dan Debugging

#### Melihat Logs
```bash
# Real-time logs
tail -f logs.txt

# Logs dengan filter error
tail -f logs.txt | grep ERROR

# Logs dengan timestamp
tail -f logs.txt | grep "$(date +%Y-%m-%d)"
```

#### Debug Mode
```bash
# Jalankan dengan debug
python3 -m PyroUbot --debug

# Verbose logging
python3 -m PyroUbot --verbose

# Development mode
python3 -m PyroUbot --dev
```

#### System Monitoring
```bash
# Check system resources
htop
df -h
free -h
iostat -x 1

# Check network
ping -c 4 api.telegram.org
traceroute api.telegram.org

# Check Python processes
ps aux | grep python
```

#### Database Debugging
```bash
# Check MongoDB connection
mongosh --eval "db.stats()"

# Check database size
mongosh --eval "db.serverStatus().connections"

# Backup database
mongodump --db pyroubot --out backup/
```

### Performance Optimization

#### Memory Usage
- Monitor RAM usage dengan `free -h`
- Restart bot jika memory leak terdeteksi
- Gunakan virtual environment terpisah

#### CPU Usage
- Monitor dengan `htop` atau `top`
- Identifikasi proses yang intensive
- Optimize queries database

#### Network Issues
- Test koneksi dengan `ping api.telegram.org`
- Check bandwidth dengan `speedtest-cli`
- Monitor network traffic

---

## Kontribusi

Kami sangat menghargai kontribusi dari komunitas untuk pengembangan PyroUbot.

### Cara Berkontribusi

1. Fork repository ini
2. Clone fork Anda: `git clone https://github.com/username/noxticaubot.git`
3. Buat branch fitur: `git checkout -b feature/AmazingFeature`
4. Commit perubahan: `git commit -m 'Add some AmazingFeature'`
5. Push ke branch: `git push origin feature/AmazingFeature`
6. Buat Pull Request

### Guidelines Pengembangan

#### Code Style
- Ikuti PEP 8 style guide
- Gunakan type hints untuk function parameters
- Tambahkan docstrings pada semua functions
- Maksimal 79 karakter per baris
- Gunakan meaningful variable names

#### Testing
- Test kode sebelum submit
- Pastikan tidak ada syntax error
- Test di environment yang berbeda
- Dokumentasikan test cases

#### Documentation
- Update README jika menambah fitur baru
- Tambahkan komentar pada kode kompleks
- Dokumentasikan API changes
- Update changelog

#### Security
- Jangan commit file sensitif (.env, credentials)
- Validate input untuk mencegah injection
- Gunakan environment variables untuk secrets
- Follow principle of least privilege

### Contributors

Terima kasih kepada semua yang telah berkontribusi!

<a href="https://github.com/noxticacode/noxticaubot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=noxticacode/noxticaubot" />
</a>

---

## API Reference

### Bot Commands API

#### Userbot Management
```python
from PyroUbot import bot, ubot

# Add new userbot
await bot.add_ubot(user_id, phone_number)

# Remove userbot
await bot.del_ubot(user_id)

# List all userbots
userbots = await bot.list_ubot()

# Get userbot status
status = await bot.get_ubot_status(user_id)
```

#### Message Handling
```python
from PyroUbot.core.helpers import cmd_prefix

@ubot.cmd_prefix("ping")
async def ping_handler(client, message):
    await message.reply("Pong!")

# Inline query handler
@ubot.on_inline_query()
async def inline_handler(client, query):
    results = [
        InlineQueryResultArticle(
            title="Result",
            input_message_content=InputTextMessageContent("Content")
        )
    ]
    await query.answer(results)
```

#### Database Operations
```python
from PyroUbot.core.database import get_pref, set_pref

# Get user preferences
prefs = await get_pref(user_id)

# Set user preferences
await set_pref(user_id, {"theme": "dark", "language": "id"})
```

### Configuration API

#### Environment Variables
```python
from PyroUbot.config import *

# Access configuration
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN
mongo_url = MONGO_URL
```

#### Custom Configuration
```python
# Custom settings
CUSTOM_SETTING = os.getenv("CUSTOM_SETTING", "default_value")
```

---

## Deployment

### VPS Deployment

#### Ubuntu/Debian
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3.10 python3.10-venv mongodb nodejs -y

# Clone and setup
git clone https://github.com/noxticacode/noxticaubot.git
cd PyroUbot
pip install -r requirements.txt
npm install -g uglify-js

# Configure
cp sample.env .env
nano .env  # Edit configuration

# Run with PM2
npm install -g pm2
pm2 start "python3 -m PyroUbot" --name PyroUbot
pm2 save
pm2 startup
```

#### Docker Deployment
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "PyroUbot"]
```

```bash
# Build and run
docker build -t pyroubot .
docker run -d --name pyroubot pyroubot
```

### Cloud Deployment

#### Heroku
1. Fork repository
2. Connect ke Heroku
3. Set environment variables di Heroku dashboard
4. Deploy

#### Railway
1. Connect GitHub repository
2. Set environment variables
3. Deploy otomatis

#### Render
1. Connect repository
2. Configure build settings
3. Set environment variables
4. Deploy

---

## Changelog

### Version 2.0.0 (Latest)
- Complete rewrite dengan Pyrogram v2.0
- Improved userbot management system
- Enhanced plugin architecture
- Better error handling dan logging
- Performance optimizations
- New features: AI assistant, advanced media tools

### Version 1.5.0
- Added voice/video call support
- MongoDB integration
- Plugin system overhaul
- Security improvements

### Version 1.0.0
- Initial release
- Basic userbot functionality
- Core features implementation

---

## Lisensi

PyroUbot didistribusikan di bawah lisensi MIT License.

```
MIT License

Copyright (c) 2024 Noxtica

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Disclaimer & Terms

### Penggunaan

Bot ini dikembangkan untuk tujuan edukasi dan personal use saja. Dilarang menggunakan untuk:
- Spam atau flooding
- Phishing atau penipuan
- Distribusi konten ilegal
- Melanggar Terms of Service Telegram
- Aktivitas yang merugikan pengguna lain

Pengguna bertanggung jawab penuh atas penggunaan bot ini.

### Terms of Service

- Patuhi Terms of Service Telegram
- Jangan abuse API rate limits
- Respect privacy dan hak pengguna lain
- Gunakan dengan bijak dan bertanggung jawab

### Support & Contact

Jika ada pertanyaan, masalah, atau ingin berdiskusi tentang PyroUbot:

- **Telegram Group**: [Noxtica Community](https://t.me/noxtic) - Tempat diskusi, support, dan update
- **GitHub Issues**: [Report Bug](https://github.com/noxticacode/noxticaubot/issues) - Laporkan bug atau request fitur
- **GitHub Discussions**: [Q&A](https://github.com/noxticacode/noxticaubot/discussions) - Tanya jawab dan diskusi
- **Email**: noxtica@gmail.com - Contact developer

### Community Guidelines

- Gunakan bahasa yang sopan dan respektif
- Bantu sesama member jika memungkinkan
- Laporkan bug dengan detail yang lengkap
- Bagikan pengalaman dan tips menggunakan bot
- Respect privacy dan jangan spam

### Getting Help

1. **Cek Dokumentasi**: Baca README.md terlebih dahulu
2. **Search Existing Issues**: Cari masalah serupa yang sudah dilaporkan
3. **Telegram Group**: Tanyakan di group untuk support cepat
4. **GitHub Issues**: Buat issue baru jika belum ada solusi

---

## FAQ (Frequently Asked Questions)

### General Questions

**Q: Apa itu PyroUbot?**
A: PyroUbot adalah bot Telegram multifungsi yang dapat mengelola userbot secara otomatis dengan berbagai fitur entertainment dan utility.

**Q: Apakah PyroUbot gratis?**
A: Ya, PyroUbot adalah open source dan gratis untuk digunakan. Namun Anda perlu biaya untuk hosting dan API keys tertentu.

**Q: Berapa banyak userbot yang bisa dikelola?**
A: Secara default maksimal 100 userbot per instance, namun dapat dikonfigurasi sesuai kebutuhan.

**Q: Apakah PyroUbot aman digunakan?**
A: Bot ini aman jika digunakan sesuai guidelines. Selalu gunakan credentials Anda sendiri dan jangan bagikan token ke orang lain.

### Technical Questions

**Q: Bot tidak merespons perintah saya**
A: Pastikan bot sudah diaktifkan dan Anda memiliki akses. Cek status bot dengan `/ping` command.

**Q: Error "MongoDB connection failed"**
A: Periksa koneksi internet dan konfigurasi MONGO_URL. Gunakan MongoDB Atlas untuk hosting cloud.

**Q: Userbot sering expired**
A: Ini normal karena session Telegram memiliki batas waktu. Bot akan otomatis membersihkan userbot yang expired.

**Q: Bagaimana cara backup data?**
A: Bot memiliki fitur backup otomatis. Gunakan `/backup` command untuk manual backup.

### Installation Questions

**Q: VPS apa yang direkomendasikan?**
A: Minimum 1GB RAM, 1 core CPU. Recommended: DigitalOcean, Vultr, atau Linode dengan Ubuntu 20.04+.

**Q: Berapa biaya hosting per bulan?**
A: $5-15 per bulan tergantung provider dan spesifikasi. Termasuk VPS + MongoDB Atlas.

**Q: Bisakah dijalankan di Heroku?**
A: Ya, namun Heroku memiliki batasan free tier. Gunakan paid dyno untuk 24/7 uptime.

### Development Questions

**Q: Bagaimana cara menambah fitur baru?**
A: Buat file baru di folder `modules/` dan ikuti struktur yang ada. Lihat contoh di file lain.

**Q: Bagaimana cara debugging?**
A: Gunakan `python3 -m PyroUbot --debug` untuk verbose logging. Cek `logs.txt` untuk error details.

**Q: Dimana dokumentasi API lengkap?**
A: Lihat bagian "API Reference" di README ini. Juga cek Pyrogram documentation.

---

## Roadmap & Future Plans

### Version 2.1.0 (Next Release)
- [ ] AI Chatbot integration (GPT-4, Claude)
- [ ] Advanced media processing
- [ ] Multi-language support
- [ ] Web dashboard interface
- [ ] Plugin marketplace

### Version 2.2.0 (Future)
- [ ] Voice recognition features
- [ ] Advanced automation workflows
- [ ] Integration dengan external APIs
- [ ] Mobile app companion
- [ ] Advanced analytics dashboard

### Long-term Vision
- [ ] Cross-platform support (Discord, WhatsApp)
- [ ] Enterprise features
- [ ] White-label solutions
- [ ] API marketplace
- [ ] Decentralized architecture

### Contributing to Roadmap
Fitur apa yang ingin Anda lihat di PyroUbot? Berikan masukan di:
- [GitHub Discussions](https://github.com/noxticacode/noxticaubot/discussions)
- [Telegram Channel](https://t.me/noxtica)

---

## Performance & Optimization

### System Requirements

#### Minimum Requirements
- CPU: 1 core @ 2.4GHz
- RAM: 512MB
- Storage: 1GB SSD
- Network: 100Mbps
- OS: Ubuntu 18.04+

#### Recommended Requirements
- CPU: 2+ cores @ 3.0GHz+
- RAM: 2GB+
- Storage: 10GB+ SSD
- Network: 1Gbps
- OS: Ubuntu 20.04+ LTS

### Performance Tips

#### Database Optimization
```python
# Use connection pooling
client = AsyncIOMotorClient(MONGO_URL, maxPoolSize=10)

# Index important fields
db.userbots.create_index("user_id")
db.userbots.create_index("created_at")

# Use aggregation pipelines for complex queries
```

#### Memory Management
```python
# Clear cache periodically
@ubot.on_message(filters.command("clear_cache"))
async def clear_cache(client, message):
    # Clear various caches
    pass
```

#### Rate Limiting
```python
# Implement rate limiting
from pyrogram.errors import FloodWait
import asyncio

async def safe_request(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await func(*args, **kwargs)
```

### Monitoring & Metrics

#### Health Checks
```bash
# Check bot health
curl http://localhost:8000/health

# Monitor resource usage
htop
iotop
nload
```

#### Logging Configuration
```python
# Advanced logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs.txt'),
        logging.StreamHandler()
    ]
)
```

---

## Security Best Practices

### API Security
- Jangan commit API keys ke repository
- Gunakan environment variables
- Rotate keys secara berkala
- Monitor API usage

### User Data Protection
- Encrypt sensitive data di database
- Implement proper access controls
- Regular security audits
- GDPR compliance untuk data user

### Bot Security
- Validate semua input user
- Rate limiting pada commands
- Anti-spam protection
- Session management yang aman

### Hosting Security
- Gunakan firewall (ufw/iptables)
- Keep system updated
- Use SSL/TLS certificates
- Regular backups

---

## Troubleshooting Advanced

### Common Error Codes

#### Telegram API Errors
- `400 BAD_REQUEST`: Invalid parameter
- `401 UNAUTHORIZED`: Invalid token
- `403 FORBIDDEN`: Bot tidak memiliki akses
- `404 NOT_FOUND`: Chat/user tidak ditemukan
- `420 FLOOD`: Rate limit exceeded
- `500 INTERNAL`: Server error Telegram

#### Database Errors
- `ConnectionTimeout`: Database unreachable
- `AuthenticationFailed`: Invalid credentials
- `DuplicateKeyError`: Data sudah ada
- `ValidationError`: Invalid data format

#### System Errors
- `MemoryError`: Out of memory
- `TimeoutError`: Operation timeout
- `OSError`: System resource error
- `ImportError`: Missing dependencies

### Debug Commands

```bash
# Check system status
python3 -c "import PyroUbot; print('Import OK')"

# Test database connection
python3 -c "from PyroUbot.core.database import client; print('DB OK')"

# Test bot token
python3 -c "from PyroUbot.config import BOT_TOKEN; print('Token OK')"

# Check all dependencies
python3 -c "import pyrogram, pytgcalls, motor; print('Deps OK')"
```

### Recovery Procedures

#### Bot Crash Recovery
1. Check logs untuk error details
2. Restart bot dengan `python3 -m PyroUbot`
3. Verify database integrity
4. Check system resources

#### Data Loss Recovery
1. Restore dari backup terakhir
2. Recreate missing userbots
3. Verify configuration files
4. Test functionality

#### Performance Issues
1. Monitor system resources
2. Check database performance
3. Optimize queries
4. Scale up if necessary

---




## Community & Ecosystem

### Official Channels
- **Telegram Channel**: [Noxtica Community](https://t.me/noxtica)
- **GitHub**: [Repository (https://github.com/noxticacode/noxticaubot)
- **Website**: [Noxtica] (https://noxtica.web.id)
- **Documentation**: This README

### Related Projects
- **Pyrogram**: Core Telegram library
- **PyTgCalls**: Voice/video calls
- **MongoDB**: Database solution
- **TgCrypto**: Encryption library

### Learning Resources
- **Pyrogram Documentation**: [pyrogram.org](https://docs.pyrogram.org)
- **Telegram Bot API**: [core.telegram.org](https://core.telegram.org/bots/api)
- **Python Asyncio**: [docs.python.org](https://docs.python.org/3/library/asyncio.html)
- **MongoDB Manual**: [docs.mongodb.com](https://docs.mongodb.com)

### Community Projects
- Custom plugins dan modules
- Deployment scripts
- Docker configurations
- Alternative frontends

---

## Credits & Attribution

Dibuat dengan dedikasi oleh Noxtica dan teman-teman yang telah berkontribusi.

### Tim Pengembang

- **Ibra Decode** - Lead Developer & Project Owner
- **Contributors** - Bug fixes, features, dan improvements

### Special Thanks

- Pyrogram Team - Library utama untuk Telegram API
- PyTgCalls Team - Voice/video call functionality
- MongoDB Team - Database solution
- Open source community - Libraries dan tools

### Tech Stack

- Backend: Python 3.10+, Pyrogram, PyTgCalls
- Database: MongoDB Atlas
- Frontend: Telegram Bot API
- Deployment: VPS, Docker, Cloud platforms
- Tools: Git, GitHub, VS Code

---

<div align="center">

Jika Anda menyukai proyek ini, berikan star di GitHub!

[![GitHub stars](https://img.shields.io/github/stars/noxticacode/noxticaubot.svg?style=social&label=Star)](https://github.com/noxticacode/noxticaubot)
[![GitHub forks](https://img.shields.io/github/forks/noxticacode/noxticaubot.svg?style=social&label=Fork)](https://github.com/noxticacode/noxticaubot)

---

PyroUbot (c) 2025. Developed with passion in Indonesia

</div>
