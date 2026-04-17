# Java AI Reviewer

A Python-based CLI tool that leverages Google's Gemini AI to review Java code, debug errors, and provide expert architecture advice.

## Description

Java AI Reviewer is an interactive command-line application that acts as a senior Java software architect with 15+ years of experience. It analyzes Java code, error messages, and architecture questions, providing detailed, structured responses in Spanish.

## Features

- 🤖 **AI-Powered Code Review**: Get expert feedback on Java code snippets
- 🏗️ **Architecture Consultation**: Discuss software architecture patterns and best practices
- 🐛 **Error Debugging**: Analyze Java errors and get solution recommendations
- 🇪🇸 **Spanish Responses**: All responses are provided in clear, professional Spanish
- 💬 **Interactive CLI**: Easy-to-use command-line interface for real-time interaction

## Requirements

### System Requirements
- Python 3.8 or higher

### Dependencies
- `google-genai` - Google's Generative AI Python client library

## Installation

1. **Clone or download the project** to your local machine

2. **Install dependencies**:
   ```bash
   pip install google-genai
   ```

3. **Configure Google API credentials**:
   - Obtain a Google Generative AI API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Set your API key as an environment variable:
     ```bash
     # On Windows (PowerShell)
     $env:GOOGLE_API_KEY = "your-api-key-here"
     
     # On Windows (Command Prompt)
     set GOOGLE_API_KEY=your-api-key-here
     
     # On macOS/Linux
     export GOOGLE_API_KEY=your-api-key-here
     ```

## Configuration

The application uses the following configuration:

- **Model**: `gemini-3-flash-preview` - Google's latest Flash model optimized for speed
- **System Instruction**: Configured to respond as a senior Java architect with 15+ years of expertise
- **Language**: Spanish (all responses are in Spanish)
- **Response Style**: Clear, structured, and professional with code examples when relevant

## Usage

1. **Run the application**:
   ```bash
   python java_ai_reviewer.py
   ```

2. **Interactive session**:
   - The program will display: `🤖 Java AI Reviewer listo. Escribe 'salir' para terminar.`
   - Enter your Java code, error message, or architecture question at the prompt
   - The AI will analyze and provide an expert response
   - Continue with more questions or type `salir` to exit

### Example Inputs

- **Code Review**: Paste a Java code snippet for architectural review
- **Error Analysis**: Paste an error stack trace to get debugging assistance
- **Architecture Questions**: Ask about design patterns, best practices, microservices, etc.

## Example Session

```
🤖 Java AI Reviewer listo. Escribe 'salir' para terminar.

Pega tu código, error o pregunta de arquitectura:
> public class UserService { ... }

✅ Respuesta del LLM:
[AI response with architectural feedback in Spanish]

Pega tu código, error o pregunta de arquitectura:
> salir
```

## Notes

- Ensure your API key is properly configured before running the application
- The application requires an active internet connection to communicate with Google's API
- Response quality and speed depend on your internet connection and API availability
- All interactions are processed by Google's Gemini API

## Troubleshooting

**API Key Error**: Verify that your `GOOGLE_API_KEY` environment variable is set correctly

**Connection Issues**: Check your internet connection and API availability

**Model Not Found**: Ensure you're using a valid model ID (`gemini-3-flash-preview`)

## Author

Reinaldo Aru - for the Python for Everyone Project.