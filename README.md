# 💼 LinkedIn Automation Platform

A powerful, modular, and ethical LinkedIn automation project built with Python — production-ready and designed for safe, responsible usage with a beautiful real-time dashboard.

## 🎯 Overview
This project automates LinkedIn workflows intelligently: searching profiles, sending personalized connection requests with AI-powered message generation, tracking responses, and analyzing campaign performance through a stunning interactive Streamlit dashboard.

**Key Highlights:**
- 🤖 **AI-Powered Messages** - OpenAI integration for personalized connection requests
- 📊 **Real-time Dashboard** - Beautiful Streamlit analytics with live metrics
- 🔐 **Safe & Ethical** - Built-in rate limiting, delays, and daily caps
- 📈 **Advanced Tracking** - CSV persistence for leads, requests, responses, and logs
- ⚡ **Intelligent Automation** - Selenium-based browser automation with smart waits

## ✨ Features
- **Selenium-based Browser Automation** - Safe waits, intelligent element detection, and error handling
- **OpenAI Message Generation** - Creates personalized, contextual connection requests
- **Smart Rate Limiting** - Randomized delays, daily request caps, and retry logic
- **Data Persistence** - CSV-based tracking for leads, sent requests, responses, and logs
- **Beautiful Dashboard** - 4-tab Streamlit interface with:
  - 📊 Campaign Overview & Daily Performance Charts
  - 📋 Lead Database Management
  - ✉️ Sent Requests Tracking
  - 💬 Response Analytics
- **Profile Search** - Find targeted professionals by job title and location
- **Follow-up Automation** - Automated message sequences with scheduling

## 🛠️ Tech Stack
- **Python** 3.10+
- **Selenium** - Web automation
- **Pandas** - Data analysis & CSV handling
- **Streamlit** - Interactive web dashboard
- **OpenAI** - AI message generation
- **Schedule** - Task scheduling
- **python-dotenv** - Environment management
- **Faker** - Test data generation

## 📁 Project Structure
```
linkedin-automation-project/
├── main.py                 # Entry point for automation
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create from .env.example)
├── .env.example           # Template for environment setup
├── README.md              # This file
│
├── config/
│   ├── settings.py        # Application settings
│   └── linkedin_config.json # Target job titles, locations, keywords
│
├── automation/            # Core automation modules
│   ├── login.py          # LinkedIn login handling
│   ├── search_profiles.py # Profile discovery
│   ├── send_connection.py # Connection requests
│   ├── send_message.py    # Message sending
│   └── follow_up.py       # Follow-up sequences
│
├── ai/                    # AI & personalization
│   ├── message_generator.py # OpenAI message creation
│   └── personalization.py   # Token substitution & customization
│
├── workflows/            # Workflow orchestration
│   ├── automation_flow.py # Main automation flow
│   └── scheduler.py       # Task scheduling
│
├── dashboard/            # Streamlit analytics dashboard
│   ├── dashboard.py       # Main dashboard app
│   ├── analytics.py       # Analytics calculations
│   └── __init__.py
│
├── data/                 # Data storage
│   ├── leads_input.csv   # Extracted lead profiles
│   ├── sent_requests.csv # Connection requests sent
│   ├── responses.csv     # Received responses
│   ├── logs.csv          # Automation logs
│   └── generate_fake_data.py # Test data generator
│
└── utils/               # Utilities
    ├── logger.py        # Logging configuration
    └── helpers.py       # Helper functions
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- LinkedIn account (with verified email)
- OpenAI API key (for AI message generation)
- Chrome/Chromium browser (for Selenium)

### Installation Steps

1. **Clone or Download the Project**
   ```bash
   cd linkedin-automation-project
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add:
   ```env
   LINKEDIN_EMAIL=your_email@gmail.com
   LINKEDIN_PASSWORD=your_secure_password
   OPENAI_API_KEY=sk-your-openai-api-key
   MAX_DAILY_REQUESTS=50
   HEADLESS=true
   ```

5. **Update Configuration**
   
   Edit `config/linkedin_config.json`:
   ```json
   {
     "job_titles": ["Software Engineer", "Product Manager"],
     "locations": ["United States", "India"],
     "keywords": ["Python", "Automation"],
     "experience_levels": ["Mid-Senior level"]
   }
   ```

### Running the Project

#### Option 1: Run Automation Only
```bash
python main.py
```
The automation will run in the background, searching profiles and sending connection requests based on your config.

#### Option 2: Run Dashboard Only (Recommended)
```bash
streamlit run dashboard/dashboard.py
```
Access the dashboard at **http://localhost:8501**

#### Option 3: Run Both Simultaneously
```bash
# Terminal 1 - Start automation
python main.py

# Terminal 2 - Start dashboard
streamlit run dashboard/dashboard.py
```

## 📊 Dashboard Features

The beautiful Streamlit dashboard provides real-time monitoring:

### 📈 Overview Tab
- Campaign performance metrics
- Daily activity charts
- Response rate statistics
- Pending response count

### 📋 Leads Tab
- View all extracted leads
- Profile details: name, role, company, location
- Search and filter capabilities

### ✉️ Sent Requests Tab
- Track all connection requests
- View timestamps and status
- Analytics on request distribution

### 💬 Responses Tab
- Monitor incoming responses
- Track engagement
- Response patterns and trends

### Sidebar Controls
- Quick metrics summary
- Refresh interval settings
- Campaign statistics

## ⚖️ Ethical Usage & Safety Guidelines

**IMPORTANT:** This tool should be used responsibly and ethically.

### Guidelines
- ✅ **Do:**
  - Build genuine professional relationships
  - Use personalized messages, not templated spam
  - Respect LinkedIn's Terms of Service
  - Set reasonable daily limits (50-100 requests/day)
  - Include randomized delays between actions
  - Monitor responses and engagement

- ❌ **Don't:**
  - Send bulk spam messages
  - Use fake profiles or misleading information
  - Bypass LinkedIn's security measures
  - Violate LinkedIn's Terms of Service
  - Automate actions 24/7 without breaks
  - Share personal data without consent

### Legal Disclaimer
- This project is for **educational and authorized use only**
- Users are responsible for complying with LinkedIn's Terms of Service
- The authors assume no liability for misuse of this tool
- Use at your own risk

## 🔧 Advanced Configuration

### Rate Limiting
Adjust `MAX_DAILY_REQUESTS` in `.env`:
- 50-100: Conservative (recommended for safety)
- 100-200: Moderate (acceptable with delays)
- 200+: Aggressive (high risk of account suspension)

### Headless Mode
Set `HEADLESS=true` in `.env` to run without visible browser window.

### Message Personalization
Edit `ai/personalization.py` to customize token substitution:
```python
tokens = {
    '{name}': lead['name'],
    '{role}': lead['role'],
    '{company}': lead['company'],
    '{location}': lead['location']
}
```

### Scheduling
Use `workflows/scheduler.py` to run automation on a schedule:
```python
schedule.every().day.at("09:00").do(run_automation)
```

## 📝 Logging & Monitoring

All activities are logged to `data/logs.csv`:
- Connection requests
- Messages sent
- Responses received
- Errors and exceptions
- Timestamp for each action

Monitor logs in the dashboard's **Overview** tab.

## 🐛 Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError"**
- Solution: Ensure you're in the virtual environment and all packages are installed
  ```bash
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

**Issue: "Missing LINKEDIN_EMAIL or LINKEDIN_PASSWORD"**
- Solution: Check your `.env` file has correct values
  ```bash
  cat .env
  ```

**Issue: Dashboard shows blank pages**
- Solution: Wait for automation to run and generate data, or generate test data
  ```bash
  python data/generate_fake_data.py
  ```

**Issue: Selenium WebDriver errors**
- Solution: Ensure Chrome/Chromium is installed and up to date

**Issue: OpenAI API errors**
- Solution: Verify your API key is valid and has available credits

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional message templates
- More analytics features
- Support for other platforms (Twitter, GitHub, etc.)
- Enhanced personalization
- Better error handling

## 📚 Resources

- [Selenium Documentation](https://selenium.dev/documentation/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [LinkedIn API Documentation](https://docs.microsoft.com/en-us/linkedin/)

## 📄 License

This project is provided as-is for educational purposes. Users are responsible for ensuring compliance with all applicable laws and platform terms of service.

## 💡 Tips for Success

1. **Start Small** - Begin with 50 requests/day to test
2. **Monitor Engagement** - Check dashboard daily for response patterns
3. **Refine Messages** - Adjust message templates based on response rates
4. **Mix It Up** - Vary connection request timing and content
5. **Respect Limits** - Take breaks between batches
6. **Build Relationships** - Focus on quality over quantity
7. **Follow Up** - Engage with responses promptly

---

**Made with ❤️ for ethical LinkedIn automation**
