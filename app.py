# Deployment of App for Real-Time Day Trade Analytics with AI Agents, Groq, DeepSeek, and AWS for Monetization

# Imports
import re
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# Load the environment variable file
load_dotenv()

########## Analytics ##########

# Uses Streamlit's data cache to store the results of the function and avoid reprocessing
# Defines the function that extracts historical data of a stock based on the specified ticker and period
@st.cache_data
def extrai_dados(ticker, period="6mo"):

    # Create a Ticker object from Yahoo Finance for the specified stock.
    stock = yf.Ticker(ticker)
    
    # Get the stock price history for the defined period
    hist = stock.history(period=period)
    
    # Resets the DataFrame index to transform the date column into a normal column.
    hist.reset_index(inplace=True)
    
    return hist

# Define the function to plot the stock price based on the provided history.
def plot_stock_price(hist, ticker):
    # Creates an interactive line chart using Plotly Express
    # The X axis represents the date and the Y axis represents the stock's closing price
    # The chart title includes the stock ticker and the analysis period
    fig = px.line(hist, x="Date", y="Close", title=f"{ticker} Stock Prices (Last 6 Months)", markers=True)
    
    # Displays the graph in Streamlit
    st.plotly_chart(fig)

# Define the function to plot a candlestick chart based on the provided history.
def plot_candlestick(hist, ticker):

    # Create a Figure object from Plotly to store the graph
    fig = go.Figure(

        # Add a candlestick chart with the stock's historical data.
        data = [
            go.Candlestick(
                x = hist['Date'],        # Define the dates on the X axis
                open = hist['Open'],     # Define the opening prices
                high = hist['High'],     # Define the highest prices
                low = hist['Low'],       # Define the lowest prices
                close = hist['Close']
            )
        ]  # Define the closing prices
    )
    
    # Updates the chart layout, including a dynamic title with the stock ticker.
    fig.update_layout(title=f"{ticker} Candlestick Chart (Últimos 6 Meses)")
    
    # Displays the graph in Streamlit
    st.plotly_chart(fig)

# Define the function to plot moving averages based on the provided history
def plot_media_movel(hist, ticker):

    # Calculates the Simple Moving Average (SMA) of 20 periods and adds it to the DataFrame
    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    
    # Calculates the 20-period Exponential Moving Average (EMA) and adds it to the DataFrame
    hist['EMA_20'] = hist['Close'].ewm(span=20, adjust=False).mean()
    
    # Creates an interactive line chart using Plotly Express
    # Plots the closing prices, the 20-period SMA, and the 20-period EMA
    fig = px.line(hist, 
                  x='Date', 
                  y=['Close', 'SMA_20', 'EMA_20'],
                  title=f"{ticker} Moving Averages (Last 6 Months)",  # Defines the title of the chart
                  labels={'value': 'Price (USD)', 'Date': 'Date'})    # Define the axis labels
    
    st.plotly_chart(fig)

# Define the function to plot the trading volume of the stock based on the provided history.
def plot_volume(hist, ticker):

    # Creates an interactive bar chart using Plotly Express
    # The X axis represents the date and the Y axis represents the traded volume.
    fig = px.bar(hist, 
                 x='Date', 
                 y='Volume', 
                 title=f"{ticker} Trading Volume (Últimos 6 Meses)")  # Define the title of the chart
    
    st.plotly_chart(fig)

########## AI Agents ##########

# AI Agents
agente_web_search = Agent(name="Web Search Agent",
                              role="Perform web search",
                              model=Groq(id="deepseek-r1-distill-llama-70b"),
                              tools=[DuckDuckGo()],
                              instructions=["Always include sources"],
                              show_tool_calls=True, markdown=True)

agente_financeiro = Agent(name="Financial Agent",
                              model=Groq(id="deepseek-r1-distill-llama-70b"),
                              tools=[YFinanceTools(stock_price=True,
                                                   analyst_recommendations=True,
                                                   stock_fundamentals=True,
                                                   company_news=True)],
                              instructions=["Use tables to display data"],
                              show_tool_calls=True, markdown=True)

multi_ai_agent = Agent(team=[agente_web_search, agente_financeiro],
                       model=Groq(id="llama-3.3-70b-versatile"),
                       instructions=["Always include sources", "Use tables to display data"],
                       show_tool_calls=True, markdown=True)

########## App Web ##########

# Streamlit page configuration
st.set_page_config(page_title="Day Trade App", page_icon=":100:", layout="wide")

# Sidebar with instructions
st.sidebar.title("Instruções")
st.sidebar.markdown("""
### How to Use the App:

- Insert the ticker symbol of the desired stock in the central field.
- Click the **Analyze** button to get real-time analysis with visualizations and insights generated by AI.

### Examples of valid tickers:
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)
- GOOG (Alphabet)

More tickers can be found here: https://stockanalysis.com/list/nasdaq-stocks/

### Purpose of the App:
This app does advanced real-time stock price analysis for Nasdaq using AI agents with the DeepSeek model through Groq and AWS infrastructure to support Day Trading strategies for making money. It’s a full-on example app for anyone looking to get into Data and AI consulting.
""")

# Main Title
st.title(":100: Day Trade App")

# Main Interface
st.header("Real-Time Day Trade Analytics with AI Agents")

# Text box for user input
ticker = st.text_input("Type the code (ticker simbol):").upper()

# If the user presses the button, we enter this block
if st.button("Analyse"):
    # If we have the stock ticker code
    if ticker:
        # Starts the processing
        with st.spinner('Searching for Real-Time Data. Please wait...'):
            # Gets the data
            hist = extrai_dados(ticker)

            # Renders a subtitle
            st.subheader("AI Generated Analysis")

            # Executes the AI Agent task
            ai_response = multi_ai_agent.run(f"Summarize the analyst's recommendation and share the latest news to {ticker}")

            # Removes lines that start with "Running:"
            # Removes the block "Running:" and also lines "transfer task to finance ai agent"
            clean_response = re.sub(r'(Running:[\s\S]*)\n\n(transfer_task_to_finance_ai_agent.\n?)', "", ai_response.content, flags=re.MULTILINE).strip()

            # Prints the response
            st.markdown(clean_response)

            # Renders the graphics
            st.subheader("Data Visualization")
            plot_stock_price(hist, ticker)
            plot_candlestick(hist, ticker)
            plot_media_movel(hist, ticker)
            plot_volume(hist, ticker)
    else:
        st.error("Invalid Ticker. Please enter a valid stock symbol.")

# End
# Obrigado DSA!




