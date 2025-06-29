# BeatBinder 🥁

A file sharing and social media platform designed specifically for drummers and percussionists to share music, charts, and exercises.

## About

BeatBinder is a Django-based web application that serves as a community hub for percussionists. It allows users to:

- Share drum charts and sheet music
- Upload and share practice exercises
- Connect with other drummers and percussionists
- Build a social network within the percussion community
- Access a library of shared musical resources

## Features

- **File Sharing**: Upload and share drum charts, exercises, and sheet music
- **Social Networking**: Connect with other percussionists
- **User Profiles**: Create and customize your drummer profile
- **Search & Discovery**: Find charts and exercises by genre, difficulty, or artist
- **Community Features**: Like, comment, and follow other users

## Technology Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Image Processing**: Pillow 11.2.1
- **Python**: 3.12+

## Getting Started

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/blevinspercussion/beat-binder.git
   cd beat-binder
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**
   Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

```
beatbinder/
├── beatbinder/          # Main Django project settings
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Project Link**: https://github.com/blevinspercussion/beat-binder
- **Maintainer**: Blevins Percussion

## Roadmap

- [ ] User authentication and profiles
- [ ] File upload and sharing functionality
- [ ] Social networking features
- [ ] Search and discovery
- [ ] Mobile-responsive design
- [ ] Advanced file management
- [ ] Community features (comments, likes, follows)
- [ ] Music notation viewer
- [ ] Practice tracking tools

---

**Built with ❤️ for the percussion community**
