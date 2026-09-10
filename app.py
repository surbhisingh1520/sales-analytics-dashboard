import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
    return df

df = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("🔍 Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df["Date"].min(), df["Date"].max()),
    min_value=df["Date"].min(),
    max_value=df["Date"].max()
)

regions = st.sidebar.multiselect(
    "Select Region(s)", options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Select Category(ies)", options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

# ---------------- Apply Filters ----------------
if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
else:
    start_date, end_date = df["Date"].min(), df["Date"].max()

filtered_df = df[
    (df["Date"] >= start_date) &
    (df["Date"] <= end_date) &
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories))
]

# ---------------- Header ----------------
st.title("📊 Sales Analytics Dashboard")
st.markdown("Interactive dashboard analyzing sales, revenue, and profit across regions and product categories.")

if filtered_df.empty:
    st.warning("No data available for the selected filters. Please adjust your selection.")
    st.stop()

# ---------------- KPI Cards ----------------
total_revenue = filtered_df["Revenue"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)
avg_order_value = total_revenue / total_orders if total_orders else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Avg Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")

# ---------------- Charts Row 1 ----------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("Revenue Trend Over Time")
    trend = filtered_df.groupby(pd.Grouper(key="Date", freq="W"))["Revenue"].sum().reset_index()
    fig1 = px.line(trend, x="Date", y="Revenue", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.subheader("Revenue by Category")
    cat_rev = filtered_df.groupby("Category")["Revenue"].sum().reset_index().sort_values("Revenue", ascending=False)
    fig2 = px.bar(cat_rev, x="Category", y="Revenue", color="Category")
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- Charts Row 2 ----------------
c3, c4 = st.columns(2)

with c3:
    st.subheader("Revenue Share by Region")
    region_rev = filtered_df.groupby("Region")["Revenue"].sum().reset_index()
    fig3 = px.pie(region_rev, names="Region", values="Revenue", hole=0.4)
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    st.subheader("Top 10 Products by Profit")
    top_products = filtered_df.groupby("Product")["Profit"].sum().reset_index().sort_values("Profit", ascending=False).head(10)
    fig4 = px.bar(top_products, x="Profit", y="Product", orientation="h")
    fig4.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# ---------------- Data Table ----------------
st.subheader("📄 Filtered Data")
st.dataframe(filtered_df.sort_values("Date", ascending=False), use_container_width=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download Filtered Data as CSV", data=csv, file_name="filtered_sales_data.csv", mime="text/csv")

st.markdown("---")
st.caption("Built with Streamlit • Data is synthetic sample data for demonstration purposes.")
