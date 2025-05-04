# --------- SETUP PACKAGES---------
import streamlit as st
import pandas as pd
import time
import pymysql
import plotly.express as px 
from streamlit_option_menu import option_menu 


# First command must be page config used wide or centered, anyone
st.set_page_config(page_title="🚀 NASA NEO Tracker", layout="wide")
#st.set_page_config(page_title="🚀 NASA NEO Tracker", layout="centered")

# --------- TITLE ---------
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🌌 NASA Near-Earth Object (NEO) Tracking & Insights 🚀</h1>", unsafe_allow_html=True)
st.markdown("---")
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

# --------- SIDEBAR NAVIGATION ---------
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Dashboard", "Filter Criteria", "Advanced Queries"],
        icons=["speedometer", "funnel-fill", "database"],
        menu_icon="rocket",
        default_index=0,
    )

# --------- WELCOME MESSAGE ---------
if 'welcome_shown' not in st.session_state:
    st.success("👋 Welcome to the NASA NEO Tracker App! Explore asteroid approaches, filter insights, and stay updated with near-Earth data!", icon="🚀")
    st.session_state['welcome_shown'] = True

# --------- DATABASE CONNECTION FUNCTION ---------
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="nasa",
        cursorclass=pymysql.cursors.DictCursor 
        #This is the object used to interact with the database.
    )

# --------- PAGE SELECTIONS ---------
if selected == "Dashboard":
    # database connection establish data to show in dashboard
    def load_metrics():
        connection = get_connection()
        with connection.cursor() as cursor:
            # 🌍 Total Approaches
            cursor.execute("SELECT COUNT(*) AS total FROM close_approach;")
            total_approaches = cursor.fetchone()["total"]

            # ☄️ Hazardous Asteroids
            cursor.execute("SELECT COUNT(*) AS hazardous FROM asteroids WHERE is_potentially_hazardous_asteroid = 1;")
            hazardous_count = cursor.fetchone()["hazardous"]

            # 🚀 Fastest Velocity
            cursor.execute("SELECT MAX(relative_velocity_kmph) AS fastest FROM close_approach;")
            fastest_velocity = cursor.fetchone()["fastest"]

        connection.close()
        return total_approaches, hazardous_count, fastest_velocity

    def load_trend_data():
        connection = get_connection()
        query = """
            SELECT DATE_FORMAT(close_approach_date, '%Y-%m') AS month, COUNT(*) AS count
            FROM close_approach
            GROUP BY month
            ORDER BY month;
        """
        df = pd.read_sql(query, connection)
        connection.close()
        return df
     # Display Metrics
    st.subheader("🌌 NASA NEO Tracker Dashboard")
    st.markdown("Real-time insights into asteroid approaches from NASA's Near-Earth Object API.")
    # Load and show metrics
    total, hazardous, fastest = load_metrics()
    col1, col2, col3 = st.columns(3)
    col1.metric(label="🌍 Total Approaches", value=f"{total:,}")
    col2.metric(label="☄️ Hazardous Asteroids", value=f"{hazardous}")
    col3.metric(label="🚀 Fastest Velocity", value=f"{fastest:,.0f} km/h")

    # Line Chart for Asteroid Approaches Over Time
     

elif selected == "Filter Criteria":
    # FILTER PAGE
    st.subheader("🔎 Apply Filter Criteria to Asteroids")

    with st.form("filters_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            mag = st.slider("Magnitude", 13.80, 32.61, (13.80, 32.61))
            dia_min = st.slider("Min Diameter (km)", 0.0, 4.62, (0.0, 4.62))
            dia_max = st.slider("Max Diameter (km)", 0.0, 10.33, (0.0, 10.33))

        with col2:
            vel = st.slider("Velocity (km/h)", 1418.21, 173071.83, (1418.21, 173071.83))
            au = st.slider("Astronomical Units", 0.0, 1.0, 0.5)
            hazardous = st.selectbox("Potentially Hazardous?", ["All", "Yes", "No"])

        with col3:
            start_date = st.date_input("Start Date", pd.to_datetime("2024-01-01"))
            end_date = st.date_input("End Date", pd.to_datetime("2025-01-01"))

        submitted = st.form_submit_button("Apply Filters")

    if submitted:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = f"""
            SELECT a.name, a.absolute_magnitude_h, a.estimated_diameter_min_km,
                   a.estimated_diameter_max_km, a.is_potentially_hazardous_asteroid,
                   c.close_approach_date, c.relative_velocity_kmph, c.astronomical_au
            FROM asteroids a
            JOIN close_approach c ON a.id = c.neo_reference_id
            WHERE a.absolute_magnitude_h BETWEEN {mag[0]} AND {mag[1]}
              AND a.estimated_diameter_min_km BETWEEN {dia_min[0]} AND {dia_min[1]}
              AND a.estimated_diameter_max_km BETWEEN {dia_max[0]} AND {dia_max[1]}
              AND c.relative_velocity_kmph BETWEEN {vel[0]} AND {vel[1]}
              AND c.astronomical_au <= {au}
              AND c.close_approach_date BETWEEN '{start_date}' AND '{end_date}'
            """

            if hazardous == "Yes":
                query += " AND a.is_potentially_hazardous_asteroid = 1"
            elif hazardous == "No":
                query += " AND a.is_potentially_hazardous_asteroid = 0"

            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data)

            if df.empty:
                st.warning("No matching asteroids found.")
            else:
                st.dataframe(df)

        except Exception as e:
            st.error(f"Database error: {e}")
        finally:
            conn.close()

elif selected == "Advanced Queries":
    st.subheader("🧠 Smart Insights and Asteroid Statistics")

    query_list = [
        "1. Count how many times each asteroid has approached Earth",
        "2. Average velocity of each asteroid over multiple approaches",
        "3. List top 10 fastest asteroids",
        "4. Find potentially hazardous asteroids that have approached Earth more than 3 times",
        "5. Find the month with the most asteroid approaches",
        "6. Get the asteroid with the fastest ever approach speed",
        "7. Sort asteroids by maximum estimated diameter (descending)",
        "8. Asteroids whose closest approach is getting nearer over time",
        "9. Display asteroid name, date, and miss distance of closest approach",
        "10. List asteroids with velocity > 50,000 km/h",
        "11. Count how many approaches happened per month",
        "12. Find asteroid with highest brightness (lowest magnitude)",
        "13. Get number of hazardous vs non-hazardous asteroids",
        "14. Find asteroids passed closer than Moon (<1 LD)",
        "15. Find asteroids that came within 0.05 AU",
        "16. List all approaches of potentially hazardous asteroids ordered by closest distance",
        "17. Get average miss distance per asteroid",
        "18. Find asteroids that have both high speed and are potentially hazardous",
        "19. Find asteroids that approached multiple times in a single year",
        "20. Find the top 5 brightest potentially hazardous asteroids",
        "21. Compare average speeds of hazardous vs non-hazardous asteroids",
        "22. Get most recent close approach per asteroid",
        "23. Find minimum and maximum diameter range per asteroid",
        "24. Get asteroids that only approached once",
        "25. Calculate the average number of approaches per asteroid"
    ]

    selected_query = st.selectbox("Select a Query", query_list)

    if selected_query:
        st.info(f"Showing results for: **{selected_query}**")

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Write SQL for each query
            if selected_query.startswith("1"):
                sql = """
                    SELECT name, COUNT(*) AS approach_count
                    FROM close_approach c
                    JOIN asteroids a ON c.neo_reference_id = a.id
                    GROUP BY name
                    ORDER BY approach_count DESC;
                """
            elif selected_query.startswith("2"):
                sql = """
                    SELECT a.name, AVG(c.relative_velocity_kmph) AS avg_velocity
                    FROM close_approach c
                    JOIN asteroids a ON c.neo_reference_id = a.id
                    GROUP BY a.name
                    ORDER BY avg_velocity DESC;
                """
            elif selected_query.startswith("3"):
                sql = """
                    SELECT a.name, MAX(c.relative_velocity_kmph) AS max_velocity
                    FROM close_approach c
                    JOIN asteroids a ON c.neo_reference_id = a.id
                    GROUP BY a.name
                    ORDER BY max_velocity DESC
                    LIMIT 10;
                """
            elif selected_query.startswith("4"):
                sql = """
                    SELECT a.name, COUNT(*) AS approach_count
                    FROM asteroids a
                    JOIN close_approach c ON a.id = c.neo_reference_id
                    WHERE a.is_potentially_hazardous_asteroid = 1
                    GROUP BY a.name
                    HAVING approach_count > 3
                    ORDER BY approach_count DESC;
                """
            elif selected_query.startswith("5"):
                sql = """
                    SELECT MONTH(close_approach_date) AS month, COUNT(*) AS approaches
                    FROM close_approach
                    GROUP BY month
                    ORDER BY approaches DESC;
                """
            elif selected_query.startswith("6"):
                sql = """
                    SELECT a.name, MAX(c.relative_velocity_kmph) AS fastest_speed
                    FROM asteroids a
                    JOIN close_approach c ON a.id = c.neo_reference_id
                    GROUP BY a.name
                    ORDER BY fastest_speed DESC
                    LIMIT 1;
                """
            elif selected_query.startswith("7"):
                sql = """
                    SELECT name, estimated_diameter_max_km
                    FROM asteroids
                    ORDER BY estimated_diameter_max_km DESC;
                """
            elif selected_query.startswith("8"):
                sql = """
                    SELECT a.name, c.close_approach_date, c.miss_distance_km
                    FROM asteroids a
                    JOIN close_approach c ON a.id = c.neo_reference_id
                    ORDER BY a.name, c.close_approach_date ASC;
                """
            elif selected_query.startswith("9"):
                sql = """
                    SELECT a.name, c.close_approach_date, c.miss_distance_km
                    FROM asteroids a
                    JOIN close_approach c ON a.id = c.neo_reference_id
                    WHERE c.miss_distance_km IS NOT NULL
                    ORDER BY c.miss_distance_km ASC;
                """
            elif selected_query.startswith("10"):
                sql = """
                    SELECT a.name, c.relative_velocity_kmph
                    FROM asteroids a
                    JOIN close_approach c ON a.id = c.neo_reference_id
                    WHERE c.relative_velocity_kmph > 50000;
                """
            elif selected_query.startswith("11"):
                sql = """
                    SELECT MONTH(close_approach_date) AS month, COUNT(*) AS total_approaches
                    FROM close_approach
                    GROUP BY month
                    ORDER BY month;
                """
            elif selected_query.startswith("12"):
                sql = """
                    SELECT name, absolute_magnitude_h
                    FROM asteroids
                    ORDER BY absolute_magnitude_h ASC
                    LIMIT 1;
                """
            elif selected_query.startswith("13"):
                sql = """
                    SELECT 
                        CASE WHEN is_potentially_hazardous_asteroid = 1 THEN 'Hazardous' ELSE 'Non-Hazardous' END AS hazard_status,
                        COUNT(*) AS count
                    FROM asteroids
                    GROUP BY hazard_status;
                """
            elif selected_query.startswith("14"):
                sql = """
                    SELECT a.name, c.close_approach_date, c.miss_distance_km
                    FROM asteroids a
                    JOIN close_approach c ON a.id = c.neo_reference_id
                    WHERE c.miss_distance_ld < 1;
                """
            elif selected_query.startswith("15"):
                sql = """
                    SELECT a.name, c.close_approach_date, c.astronomical_au
                    FROM asteroids a
                    JOIN close_approach c ON a.id = c.neo_reference_id
                    WHERE c.astronomical_au < 0.05;
                """ 
            elif selected_query.startswith("16"):
                sql = """
                    SELECT a.name, ca.close_approach_date, ca.miss_distance_km
                    FROM asteroids a
                    JOIN close_approach ca ON a.id = ca.neo_reference_id
                    WHERE a.is_potentially_hazardous_asteroid = TRUE
                    ORDER BY ca.miss_distance_km ASC;
                """
            elif selected_query.startswith("17"):
                sql = """
                    SELECT ca.neo_reference_id, a.name, AVG(ca.miss_distance_km) AS avg_miss_distance_km
                    FROM close_approach ca
                    JOIN asteroids a ON ca.neo_reference_id = a.id
                    GROUP BY ca.neo_reference_id, a.name;
                                """
            elif selected_query.startswith("18"):
                sql = """
                    SELECT a.name, ca.relative_velocity_kmph
                    FROM asteroids a
                    JOIN close_approach ca ON a.id = ca.neo_reference_id
                    WHERE a.is_potentially_hazardous_asteroid = TRUE
                    AND ca.relative_velocity_kmph > 40000
                    ORDER BY ca.relative_velocity_kmph DESC;
                """
            elif selected_query.startswith("19"):
                sql = """
                    SELECT neo_reference_id, YEAR(close_approach_date) AS year, COUNT(*) AS count
                    FROM close_approach
                    GROUP BY neo_reference_id, year
                    HAVING count > 1;
                """
            elif selected_query.startswith("20"):
                sql = """
                    SELECT name, absolute_magnitude_h
                    FROM asteroids
                    WHERE is_potentially_hazardous_asteroid = TRUE
                    ORDER BY absolute_magnitude_h ASC
                    LIMIT 5;
                """
            elif selected_query.startswith("21"):
                sql = """
                    SELECT 
                        a.is_potentially_hazardous_asteroid,
                        AVG(ca.relative_velocity_kmph) AS avg_velocity
                    FROM asteroids a
                    JOIN close_approach ca ON a.id = ca.neo_reference_id
                    GROUP BY a.is_potentially_hazardous_asteroid;
                """
            elif selected_query.startswith("22"):
                sql = """
                    SELECT ca.neo_reference_id, a.name, MAX(ca.close_approach_date) AS last_approach
                    FROM close_approach ca
                    JOIN asteroids a ON a.id = ca.neo_reference_id
                    GROUP BY ca.neo_reference_id, a.name;
                """
            elif selected_query.startswith("23"):
                sql = """
                    SELECT id, name, estimated_diameter_min_km, estimated_diameter_max_km
                    FROM asteroids
                    ORDER BY estimated_diameter_max_km DESC;
                """
            elif selected_query.startswith("24"):
                sql = """
                    SELECT a.id, a.name
                    FROM asteroids a
                    JOIN close_approach ca ON a.id = ca.neo_reference_id
                    GROUP BY a.id, a.name
                    HAVING COUNT(*) = 1;
                """
            elif selected_query.startswith("25"):
                sql = """
                    SELECT AVG(approach_count) AS avg_approaches_per_asteroid
                    FROM (
                        SELECT neo_reference_id, COUNT(*) AS approach_count
                        FROM close_approach
                        GROUP BY neo_reference_id
                    ) AS sub;
                """ 
            cursor.execute(sql)
            data = cursor.fetchall()
            df = pd.DataFrame(data)
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error fetching query: {e}")
        finally:
            conn.close()

# --------- FOOTER ---------
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Bhuvaneswari G | NASA NEO Insights 🚀</p>", unsafe_allow_html=True)
