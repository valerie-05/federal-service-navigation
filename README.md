# ReGen - Federal Systems Navigator

An AI-powered web application to help users navigate federal systems and resources.

## Tech Stack

- **Backend**: Python 3.x with Flask
- **Database**: Supabase (PostgreSQL)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **AI**: Supabase Edge Functions

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
FLASK_SECRET_KEY=your_secret_key
```

3. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Features

- **AI Chat**: Interactive chat interface for navigating federal systems
- **Resource Library**: Searchable database of federal resources
- **Admin Dashboard**: Monitor conversations and usage statistics
- **Text-to-Speech**: Audio playback of AI responses
- **Crisis Support**: Prominent crisis hotline information

## Project Structure

```
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── chat.html         # Chat interface
│   ├── resources.html    # Resource library
│   └── admin.html        # Admin dashboard
└── supabase/             # Database and edge functions
    ├── migrations/       # Database schema
    └── functions/        # Edge functions for AI
```

## API Endpoints

- `GET /` - Home page
- `GET /chat` - Chat interface
- `GET /resources` - Resource library
- `GET /admin` - Admin dashboard
- `POST /api/chat` - Send chat message
- `POST /api/tts` - Text-to-speech conversion
- `GET /api/resources` - Get all resources
- `GET /api/conversations` - Get conversation history

## Database Schema

The application uses Supabase with the following tables:
- `conversations` - Chat conversation history
- `resources` - Federal resource database
- `feedback` - User feedback

## License

MIT
