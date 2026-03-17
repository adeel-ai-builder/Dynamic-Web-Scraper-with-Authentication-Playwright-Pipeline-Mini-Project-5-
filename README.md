# Dynamic-Web-Scraper-with-Authentication-Playwright-Pipeline-Mini-Project-5-

## Project Overview

This project is an advanced, industry-level web scraping system that automates login, navigates dynamic pages, extracts structured data, and stores it for analysis.

Unlike basic scrapers, this system uses browser automation with authentication, making it suitable for scraping protected or login-based platforms.

The project follows a modular architecture, separating browser handling, login logic, scraping, parsing, and storage—just like real-world production systems.

## Business Objective

### The goal of this project is to:

Automate data extraction from login-protected websites

Simulate real user interaction (login + navigation)

Collect structured product data

Build a reusable automation pipeline

This type of system is commonly used in:

             Market intelligence platforms

             Competitor analysis tools

             E-commerce monitoring systems

## Key Features

✔ Automated login using credentials

✔ Browser automation using Playwright

✔ Handles dynamic content & scrolling

✔ Extracts structured product data:

Product Title

Price

✔ Data cleaning and deduplication
✔ Stores output in CSV format
✔ Robust error handling

## Technologies Used

Python

Playwright (Automation)

BeautifulSoup

Pandas

Data Pipeline Design

## Project Structure

dynamic-web-scraper/

             │
             ├── data/
             │   └── output.csv
             │
             ├── scripts/
             │   ├── browser.py
             │   ├── login.py
             │   ├── scraper.py
             │   ├── parser.py
             │   ├── database.py
             │   └── main.py
             │
             ├── README.md
             └── requirements.txt
             
## Pipeline Architecture

### 1️⃣ Browser Initialization

Launches Chromium browser

Sets viewport for consistent scraping

Handles startup errors

👉 Implemented in browser.py

### 2️⃣ Authentication (Login System)

Navigates to login page

Fills credentials automatically

Waits for successful login

👉 Implemented in login.py

### 3️⃣ Dynamic Scrolling

Scrolls page to load all content

Handles lazy loading

Prevents infinite loops

👉 Implemented in scraper.py

### 4️⃣ Data Extraction

Parses HTML content using BeautifulSoup

Extracts:

Product title

Price

👉 Implemented in parser.py

### 5️⃣ Data Storage

Converts data into DataFrame

Removes duplicates

Saves structured data into CSV

👉 Implemented in database.py

### 6️⃣ Orchestration

Manages full pipeline flow

Handles errors and cleanup

Ensures browser closes safely

👉 Implemented in main.py

## How to Run the Project

### Step 1: Clone Repository
             git clone https://github.com/yourusername/dynamic-web-scraper.git
             cd dynamic-web-scraper
             
### Step 2: Install Dependencies
             pip install -r requirements.txt
             playwright install
             
### Step 3: Run the Scraper
             python main.py
             
### Output

CSV file → data/output.csv

Contains:

Product titles

Prices

## Example Output

Title     	  Price

Product A	    $29.99

## Industry-Level Highlights

### This project demonstrates advanced skills:

✔ Login-based scraping (very important in real world)

✔ Browser automation (Playwright instead of simple requests

✔ Dynamic content handling (scrolling + JS rendering)

✔ Modular architecture (production-ready design

✔ Error handling and resource cleanup

## Future Improvements

Add proxy rotation

Implement CAPTCHA handling

Store data in database (PostgreSQL)

Build REST API for data access

Deploy using Docker

Add scheduling (Airflow / Cron)

## Author

### Adeel Khan
#### Aspiring Data Engineer / Automation Engineer
