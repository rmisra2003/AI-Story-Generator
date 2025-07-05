# AI-Story-Generator
An AI-powered story generator using Flask and Claude API.

# AI Story Generator

A modern web application that generates creative stories using AI. Built with Flask and powered by Claude API, this tool allows users to create personalized stories with customizable genres and word counts.

## Features

- AI-Powered Story Generation: Uses Claude API for high-quality, creative storytelling
- Genre Selection: Choose from Fantasy, Science Fiction, Romance, Adventure, Mystery, Horror, Comedy, or Any
- Customizable Length: Generate stories of 100, 200, or 500 words
- Export Functionality: Download generated stories as .txt files
- Modern UI: Clean, responsive design with Bootstrap 5
- Real-time Loading: Visual feedback during story generation
- Secure API Management: Environment variables for API key protection


## Project Structure

story-generator/
├── app.py                 # Main Flask application
├── .env                   # Environment variables (not tracked)
├── .env.example          # Template for environment variables
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
├── my_templates/         # HTML templates
│   └── index.html        # Main web interface
└── venv/                 # Virtual environment (not tracked)
(https://github.com/user-attachments/assets/3eeb75db-9a5b-4388-90c1-37ba9e8fced5)

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Claude API key from Anthropic

### Step 1: Clone the Repository
git clone https://github.com/YOUR_USERNAME/ai-story-generator.git
cd ai-story-generator

### Step 2: Create Virtual Environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

### Step 3: Install Dependencies
pip install flask anthropic python-dotenv

### Step 4: Set Up Environment Variables
1. Create a .env file in the root directory
2. Add your Claude API key:
ANTHROPIC_API_KEY=your_actual_claude_api_key_here

### Step 5: Run the Application
python app.py

### Step 6: Access the Application
Open your web browser and navigate to:
http://127.0.0.1:5000/

## Usage

1. Enter a Story Prompt: Type your creative prompt in the text area
   - Example: "A detective in a futuristic city discovers a conspiracy"

2. Select Genre: Choose from the dropdown menu
   - Options: Any, Fantasy, Science Fiction, Romance, Adventure, Mystery, Horror, Comedy

3. Choose Story Length: Select your preferred word count
   - Options: 100 words, 200 words, 500 words

4. Generate Story: Click the "Generate Story" button

5. Export Story: Once generated, click "Export as .txt" to download

## Technical Details

### Backend (Flask)
- Framework: Flask with Python
- API Integration: Claude API (Anthropic)
- Template Engine: Jinja2
- File Handling: BytesIO for text export

### Frontend
- Framework: Bootstrap 5
- JavaScript: Vanilla JS with Fetch API
- Responsive Design: Mobile-friendly interface
- Loading States: Spinner animation during generation

### Security Features
- Environment variable management with python-dotenv
- API key protection (never exposed in code)
- Input validation and error handling
- Secure file export functionality

## Security Notes

- Never commit your .env file to version control
- The .env file contains your actual API key and should remain local
- Use .env.example as a template for other developers
- API keys are loaded securely through environment variables

## Troubleshooting

### Common Issues

1. TemplateNotFound Error
- Ensure the my_templates folder exists
- Check that index.html is inside the my_templates folder
- Verify Flask is configured with the correct template folder

2. API Key Errors
- Confirm your .env file exists and contains the correct API key
- Check that the API key is valid and active
- Ensure python-dotenv is installed

3. Import Errors
- Verify all dependencies are installed: pip install flask anthropic python-dotenv
- Make sure your virtual environment is activated

4. Port Already in Use
- Change the port in app.py: app.run(debug=True, port=5001)

## API Usage

The application uses Claude API with the following configuration:
- Model: claude-3-haiku-20240307
- Temperature: 0.9 (for creative output)
- Max Tokens: Calculated based on word count (word_count × 1.5)

## Development

### Adding New Features
1. New Genres: Add options to the genre dropdown in index.html
2. Different Models: Modify the model parameter in the API call
3. Additional Lengths: Add new word count options
4. UI Improvements: Customize the CSS styles

### Testing
- Test with various prompt types and lengths
- Verify genre selection affects story content
- Check export functionality across different browsers
- Test error handling with invalid inputs

## Contributing

1. Fork the repository
2. Create a feature branch: git checkout -b feature-name
3. Make your changes
4. Test thoroughly
5. Commit your changes: git commit -m "Add feature"
6. Push to the branch: git push origin feature-name
7. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Anthropic for providing the Claude API
- Flask community for the excellent web framework
- Bootstrap for the responsive UI components

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the GitHub issues page
3. Create a new issue with detailed information about the problem

Note: This project is for educational and creative purposes. Please use responsibly and in accordance with Anthropic's usage policies.
