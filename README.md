# 🌌 NASA NEO (Near-Earth Object) Tracker Dashboard 🚀

An interactive **Streamlit** web app that uses NASA's Near-Earth Object API to visualize, analyze, and filter asteroid approach data.

---

## 📦 Project Structure
├── nasaapi.ipynb        # Jupyter Notebook to extract, transform, and load asteroid data from NASA API into MySQL
├── app.py               # Streamlit dashboard frontend to explore asteroid data
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation (this file)

---

## 🚀 Features

- 🔗 Connects to NASA's [NEO Web Service API](https://api.nasa.gov/)
- 🛠️ ETL pipeline to extract asteroid data and load into a MySQL database
- 📈 Interactive Streamlit dashboard:
  - Live metrics & visual trends
  - Filters by date, speed, magnitude, diameter, hazard level
  - Over 25 pre-built analytics using smart SQL queries
- 🧼 Clean, responsive UI with **Plotly** visualizations

---

## 📊 Dashboard Pages

### 1. **Dashboard**
- Summary metrics (e.g., total approaches, fastest speed)
- Time-series trends with line/area charts

### 2. **Filter Criteria**
- Filter asteroids based on:
  - Magnitude, diameter, velocity, hazard status
  - Date range and astronomical distance
- Results displayed in a searchable, sortable data table

### 3. **Advanced Queries**
- 25+ SQL insights like:
  - Top 10 fastest asteroids
  - Hazardous asteroids with multiple approaches
  - Closest approaches, average speeds, diameter trends

---

## 🔌 NASA API Data Collection (ETL)

The `nasaapi.ipynb` notebook:
- Fetches NEO data using NASA’s API
- Parses up to **10,000+** asteroid entries
- Extracts properties:
  - Name, magnitude, diameter, hazard status
  - Velocity, distance, approach date
- Loads into **MySQL** with two normalized tables:

### Table: `asteroids`
| id | name | magnitude | diameter_min_km | diameter_max_km | hazardous |

### Table: `close_approach`
| neo_reference_id | approach_date | velocity_kmph | au | miss_km | miss_lunar | orbiting_body |

---

## 🛠️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/nasa-neo-tracker.git
cd nasa-neo-tracker

<h1 align="center">Hi 👋, I'm Bhuvaneswari G</h1>
<h3 align="center">A passionate frontend developer and Entrepreneur from India</h3>

- 🌱 I’m currently learning **Data Science in [Guvi](https://www.guvi.in/).**

- 💬 Ask me about **Laravel, Front end Development**

- 📫 How to reach me **bhuvana87ps@gmail.com**

<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://angular.io" target="_blank" rel="noreferrer"> <img src="https://angular.io/assets/images/logos/angular/angular.svg" alt="angular" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://codeigniter.com" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/codeigniter.svg" alt="codeigniter" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.adobe.com/in/products/illustrator.html" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/adobe_illustrator/adobe_illustrator-icon.svg" alt="illustrator" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://laravel.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/laravel/laravel-plain-wordmark.svg" alt="laravel" width="40" height="40"/> </a> <a href="https://www.microsoft.com/en-us/sql-server" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="mssql" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://www.photoshop.com/en" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/photoshop/photoshop-line.svg" alt="photoshop" width="40" height="40"/> </a> <a href="https://www.php.net" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-original.svg" alt="php" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://sass-lang.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sass/sass-original.svg" alt="sass" width="40" height="40"/> </a> <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/> </a> <a href="https://vuejs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vuejs/vuejs-original-wordmark.svg" alt="vuejs" width="40" height="40"/> </a> </p>
