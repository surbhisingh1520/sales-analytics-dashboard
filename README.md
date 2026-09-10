# 📊 Sales Analytics Dashboard

An interactive data analytics dashboard built with **Streamlit**, **Pandas**, and **Plotly**.
Analyzes sales, revenue, and profit trends across regions, categories, and products with
dynamic filters, KPIs, and charts.

## Features
- Date range, Region, and Category filters
- KPI cards: Revenue, Profit, Orders, Avg Order Value
- Revenue trend over time (line chart)
- Revenue by category (bar chart)
- Revenue share by region (pie chart)
- Top 10 products by profit
- Downloadable filtered data (CSV)

## Files
- `app.py` — main Streamlit app
- `sales_data.csv` — sample dataset (synthetic, 2024 sales data)
- `requirements.txt` — Python dependencies

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy for FREE (get a live link in ~5 minutes)

### Step 1: Push to GitHub
1. Create a new GitHub repo (e.g. `sales-analytics-dashboard`)
2. Upload these 3 files: `app.py`, `sales_data.csv`, `requirements.txt`
   (via GitHub web UI: "Add file" → "Upload files", or via git commands below)

```bash
git init
git add .
git commit -m "Initial commit: sales analytics dashboard"
git branch -M main
git remote add origin https://github.com/<your-username>/sales-analytics-dashboard.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Community Cloud
1. Go to **https://share.streamlit.io**
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repo, branch (`main`), and main file (`app.py`)
5. Click **Deploy**

That's it — in about a minute you'll get a live URL like:
`https://your-app-name.streamlit.app`

Put that link in your resume under "Live Hosted Data Analytics Project" 🎉

## Customize
- Replace `sales_data.csv` with your own dataset — just keep matching column names,
  or update the `load_data()` function in `app.py`.
- Add more charts/filters as you like to make it stand out.
