# 🌌 NASA NEO (Near-Earth Object) Tracker Dashboard 🚀

An interactive **Streamlit** web app that uses NASA's Near-Earth Object API to visualize, analyze, and filter asteroid approach data.

---

## 📦 Project Structure
├── nasaapi.ipynb        # Jupyter Notebook to extract, transform, and load asteroid data from NASA API into MySQL <br>
├── app.py               # Streamlit dashboard frontend to explore asteroid data<br>
├── requirements.txt     # Python dependencies<br>
└── README.md            # Project documentation (this file)<br>

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

## 1. Clone the repo

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

### 1. Clone the repo

```bash
git clone [https://github.com/bhuvana87ps/NASA-Near-Earth-Object-NEO-Tracking-Insights-using-Public-API]
cd nasa-neo-tracker
```
### 2. Install dependencies

```bash
pip install -r requirements.txt

```
## 3. Set up MySQL
```bash
CREATE DATABASE nasa;
-- Then run the table creation and ETL from nasaapi.ipynb
```
## 4. Run the app
```bash
streamlit run app.py
```

---

## 📷 Screenshots

```bash


```

---

## 🧪 Sample SQL Queries

```bash
-- Top 10 Fastest Asteroids
SELECT a.name, MAX(c.relative_velocity_kmph) AS max_velocity
FROM close_approach c
JOIN asteroids a ON c.neo_reference_id = a.id
GROUP BY a.name
ORDER BY max_velocity DESC
LIMIT 10;


- Hazardous Asteroids with > 3 Approaches
SELECT a.name, COUNT(*) AS approach_count
FROM asteroids a
JOIN close_approach c ON a.id = c.neo_reference_id
WHERE a.hazardous = 1
GROUP BY a.name
HAVING approach_count > 3;

```

---

## 🧾 Requirements

```bash
-  Python 3.8+

-  streamlit

-  plotly

-  pandas

-  pymysql

-  streamlit-option-menu

```

---

## 📚 References

```bash
-  [NASA NEO Web Service API](https://api.nasa.gov/)

-  [NEO Feed API Reference](www.google.com)

-  [Streamlit Documentation](https://docs.streamlit.io/) 
```

---
