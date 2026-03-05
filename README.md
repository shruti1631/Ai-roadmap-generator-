# AI Roadmap Generator

A Flask-based web application that generates personalized learning roadmaps using AI. Enter your topic, skill level, and time commitment to get a customized study plan with resources and recommendations.

## Features

- **AI-Powered Roadmaps**: Uses machine learning to generate tailored learning paths
- **Multiple Skill Levels**: Beginner, Intermediate, and Advanced options
- **Flexible Duration**: Customize roadmap length from 4 to 52 weeks
- **Resource Recommendations**: Curated links to courses, books, and tools
- **Download Functionality**: Export roadmaps as text files
- **Responsive Design**: Clean, mobile-friendly interface
- **REST API**: JSON API endpoint for programmatic access

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/ML**: Custom trained model (Pickle)
- **Deployment**: Ready for Heroku (Procfile included)

## Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shruti1631/Ai-roadmap-generator-.git
   cd Ai-roadmap-generator-
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. **Web Interface**: Fill out the form with your topic, skill level, and duration
2. **Generate Roadmap**: Click "Generate Roadmap" to get your personalized plan
3. **View Resources**: Explore recommended courses, books, and tools
4. **Download**: Save your roadmap as a text file for offline access

## API Usage

### Generate Roadmap via API

```bash
curl -X GET "http://127.0.0.1:5000/api/generate?topic=python&level=beginner&weeks=8"
```

**Response:**
```json
{
  "topic": "python",
  "level": "beginner",
  "weeks": 8,
  "roadmap": "Week 1: Python Basics...",
  "resources": {
    "courses": ["..."],
    "books": ["..."],
    "tools": ["..."]
  }
}
```

## Project Structure

```
Ai-roadmap-generator-/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── static/
│   └── style.css         # CSS styles
├── templets/
│   └── index.html        # Main template
├── ml_model/             # ML model training and files
│   ├── train_model.py
│   ├── requirements.txt
│   └── README.md
├── model.pkl             # Trained AI model
└── train_model.py        # Model training script (root)
```

## ML Model

The application uses a custom-trained AI model to generate roadmaps. The model is trained on learning path data and serialized using Pickle.

### Training the Model

```bash
cd ml_model
python train_model.py
```

## Deployment

### Heroku Deployment

1. **Install Heroku CLI**
2. **Login to Heroku**
   ```bash
   heroku login
   ```
3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```
4. **Deploy**
   ```bash
   git push heroku main
   ```

### Local Development

The app includes Flask's development server. For production, consider using Gunicorn:

```bash
pip install gunicorn
gunicorn app:app
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

- [ ] User authentication and profiles
- [ ] Database storage for roadmaps
- [ ] Search and filter functionality
- [ ] Social sharing features
- [ ] Progress tracking
- [ ] Integration with learning platforms
- [ ] Advanced AI model improvements

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you find this project helpful, please give it a ⭐ on GitHub!

For questions or issues, please open an issue on GitHub.
