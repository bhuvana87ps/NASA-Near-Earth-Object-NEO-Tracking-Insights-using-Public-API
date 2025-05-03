🚀 NASA NEO Tracker App
A full-stack project that fetches Near-Earth Object (NEO) data from NASA's public API, stores it in a MySQL database, and presents it with a powerful Streamlit web dashboard for real-time exploration, filtering, and advanced asteroid insights.

📂 Project Structure
plaintext
Copy
Edit
nasaapi.ipynb      # Jupyter notebook: Data collection and database setup
app.py             # Streamlit web application for interactive asteroid exploration
requirements.txt   # List of required Python packages
README.md          # Project overview and setup guide
🌎 Overview
This project does the following:

Fetches NEO data from NASA's API.

Extracts detailed information such as:

Asteroid ID, Name, Size, Brightness, Hazard Potential.

Close Approach Date, Miss Distance, Speed, and Orbiting Body.

Populates two MySQL tables:

asteroids (asteroid-specific information)

close_approach (approach event information)

Provides a Streamlit dashboard where users can:

View asteroid metrics.

Filter based on size, velocity, hazard status, and date ranges.

Run over 20+ Advanced SQL Queries to explore trends.

🛠️ Tech Stack
Python

Pandas - Data manipulation

Requests - API handling

MySQL - Database storage

Pymysql - MySQL-Python connection

Streamlit - Interactive UI and dashboard

Streamlit Option Menu - Sidebar navigation

⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/nasa-neo-tracker.git
cd nasa-neo-tracker
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required packages
bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

plaintext
Copy
Edit
requests
pymysql
pandas
streamlit
streamlit-option-menu
4. Setup MySQL Database
Create a database named nasa_project_one.

Run the table creation and insertion code (nasaapi.ipynb) to populate tables asteroids and close_approach.

Make sure MySQL server credentials match:

python
Copy
Edit
host="localhost"
user="root"
password="123456"
database="nasa_project_one"
🛡️ Important: Secure your credentials using .env files or environment variables for production.

5. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
The app will open automatically in your web browser at http://localhost:8501.

🛰️ NASA API Used
NeoWs (Near Earth Object Web Service)

API URL: https://api.nasa.gov/neo/rest/v1/feed

You need a NASA API Key (a free key from api.nasa.gov).

🧠 Key Features
🚀 Dashboard View: Key metrics and line charts.

🔍 Filter Panel: Fine-grained asteroid filtering (magnitude, diameter, velocity, hazard, date).

📊 Advanced Queries: 25+ powerful SQL-driven asteroid insights (velocity, hazard risk, diameter ranking, approach frequency, etc.).

📅 Date Range Selector: Focus analysis on specific periods.

🌖 Distance Metrics: Astronomical Units, kilometers, lunar distances.

📸 Sample Screenshots
Dashboard View	Filter Criteria	Advanced Queries

(Optional: Add screenshots to an /images folder.)

🧹 Improvements Planned
Pagination and infinite scroll for large query results.

Authentication for Admin vs Guest users.

Integration with NASA's real-time API for auto-refreshing data.

Deployment to cloud (Streamlit Sharing, AWS, etc.).

🤝 Contributing
Contributions, issues, and feature requests are welcome!

Please open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙌 Acknowledgments
NASA Open APIs

Streamlit Documentation

MySQL Official Docs

🚀 Made with ❤️ and curiosity about space!
