# Real-Time Day Trade Analytics with AI Agents

## Project Overview

This project is a complete Streamlit web application that provides real-time day trading analytics for NASDAQ stocks using AI agents. The application leverages the power of DeepSeek models through Groq API and is designed to support day trading strategies for monetization.

## What the Application Does

The `app.py` file contains a comprehensive day trading analytics application with the following features:

### Core Functionality

1. **Real-time Stock Data Analysis**: Fetches and analyzes stock data from Yahoo Finance for any valid ticker symbol
2. **AI-Powered Insights**: Uses multiple AI agents to provide analyst recommendations and the latest news
3. **Interactive Visualizations**: Generates multiple chart types for comprehensive market analysis
4. **User-Friendly Interface**: Built with Streamlit for easy interaction

### Key Features

#### Data Analytics Functions:
- `extrai_dados()`: Extracts historical stock data for a specified period (default: 6 months)
- `plot_stock_price()`: Creates interactive line charts showing stock price movements
- `plot_candlestick()`: Generates candlestick charts for detailed price analysis
- `plot_media_movel()`: Displays moving averages (SMA and EMA) for trend analysis
- `plot_volume()`: Shows trading volume patterns

#### AI Agent System:
- **Web Search Agent**: Performs web searches for the latest market news and information
- **Financial Agent**: Provides analyst recommendations, stock fundamentals, and company news
- **Multi-Agent Coordinator**: Combines insights from both agents for comprehensive analysis

#### Interactive Web Interface:
- Streamlit-based user interface with sidebar instructions
- Real-time data processing with loading indicators
- Error handling for invalid ticker symbols
- Support contact information

## Technology Stack

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **yfinance**: Yahoo Finance API for stock data
- **Plotly**: Interactive data visualization
- **Phi Framework**: AI agent orchestration
- **Groq**: AI model API (DeepSeek models)
- **DuckDuckGo**: Web search functionality

## Usage Instructions

### Local Execution

1. **Install Anaconda Python** from the official repository:
   - Windows: `Anaconda3-2024.10-1-Windows-x86_64.exe`
   - macOS (Apple Silicon): `Anaconda3-2024.10-1-MacOSX-arm64.pkg`
   - macOS (Intel): `Anaconda3-2024.10-1-MacOSX-x86_64.pkg`
   - Linux: `Anaconda3-2024.10-1-Linux-x86_64.sh`

2. **Create Virtual Environment**:
   ```bash
   conda create --name deployai python=3.12
   conda activate deployai
   ```

3. **Install Dependencies**:
   ```bash
   conda install pip
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the Application**: Open your web browser and navigate to the provided local URL

### AWS Deployment

1. **Create AWS Account**: Set up a free AWS account
2. **Launch EC2 Instance**: Create a free-tier EC2 instance
3. **Install Miniconda**: Download and install Miniconda for lightweight deployment
4. **Deploy Application**: Upload files and run the application on the cloud instance
5. **Configure Access**: Set up security groups and access permissions
6. **Monitor Usage**: Track application performance and costs

## Application Interface

### How to Use:
1. Enter a valid stock ticker symbol (e.g., MSFT, TSLA, AMZN, GOOG)
2. Click the "Analyze" button to get real-time analysis
3. View AI-generated insights and recommendations
4. Explore interactive charts and visualizations

### Available Visualizations:
- **Stock Price Charts**: Line graphs showing price movements over time
- **Candlestick Charts**: Detailed OHLC (Open, High, Low, Close) analysis
- **Moving Averages**: SMA and EMA trend indicators
- **Volume Analysis**: Trading volume patterns and trends

## Business Application

This application serves as a complete example for:
- Data and AI consulting services
- Day trading strategy development
- Real-time market analysis
- Financial technology solutions
- AI-powered decision support systems

## Support

For questions and support, contact: suporte@datascienceacademy.com.br

## Project Structure

```
├── app.py          # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # This documentation
└── .env               # Environment variables (API keys)
```

## Environment Setup

Make sure to set up your environment variables:
- Groq API key for AI model access
- Any other required API credentials

## Notes

- The application uses a 6-month historical data period by default
- All AI responses are processed to remove technical debugging information
- The interface is optimized for both desktop and mobile access
- AWS deployment requires a proper security configuration for production use

---

*This project is part of the Data Science Academy consulting module and serves as a practical example for those starting in Data and AI consulting.*
