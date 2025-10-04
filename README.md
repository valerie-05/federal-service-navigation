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

Setup Instructions
1. Install Python Dependencies

pip3 install -r requirements.txt
This installs Flask, Bolt Database client, and other required packages.

2. Verify Environment Variables
Your .env file should already have:


VITE_Bolt Database_URL=your_Bolt Database_url
VITE_Bolt Database_ANON_KEY=your_Bolt Database_key
3. Start the Application

python3 app.py
The app will run on http://localhost:5000

4. What's Already Working
✅ Database tables (profiles, conversations, messages, resources, crisis_mode)

✅ Edge functions (chat, text-to-speech)

✅ Row Level Security policies

✅ All frontend pages (home, chat, resources, admin)

5. Add Sample Data (Optional)
To populate the resources library, run this SQL in Bolt Database:


INSERT INTO resources (name, type, address, phone, website, services) VALUES
('Social Security Office', 'Federal', '123 Main St, Washington DC', '1-800-772-1213', 'https://www.ssa.gov', ARRAY['Benefits', 'Retirement', 'Disability']),
('VA Medical Center', 'Healthcare', '456 Veterans Blvd, DC', '1-800-827-1000', 'https://www.va.gov', ARRAY['Healthcare', 'Mental Health', 'Benefits']),
('IRS Taxpayer Assistance', 'Federal', '789 Tax Ave, DC', '1-800-829-1040', 'https://www.irs.gov', ARRAY['Tax Help', 'Filing Assistance']);
6. Test the Features
Home: Navigate to landing page
Chat: Test AI conversation (requires edge function to have AI integration)
Resources: View and search resources
Admin: View conversation statistics
The application is production-ready except the chat AI logic needs to be implemented in the edge function at supabase/functions/chat/index.ts.


