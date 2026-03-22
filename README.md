Hackathon-Friendly Architecture (Markdown-Friendly)
+-------------------+
|   Vendor Data     |
| (CVE feeds, APIs, |
|  GitHub leaks)    |
+--------+----------+
         |
         v
+-------------------+
| Python Scraper /  |
| Data Processor    |
+--------+----------+
         |
         v
+-------------------+
|  SQL Database     |
| (Stores vendors,  |
|  risk scores,     |
|  dependencies)    |
+--------+----------+
         |
         v
+-------------------+
|  Predictive Model |
| (Python ML,       |
|  e.g., scikit-learn|
|  or simple logic) |
+--------+----------+
         |
         v
+-------------------+
|   Dash Dashboard  |
| (Risk maps,       |
|  vendor graph,    |
|  score tables)    |
+-------------------+
