# COVID-19 Data Analysis and Visualization

This project provides comprehensive analysis and visualization of COVID-19 data from around the world.

## ?? Features

- **Global Statistics**: Total confirmed cases, deaths, and mortality rates
- **Time Series Analysis**: Track trends over time with daily and cumulative views
- **Country Comparisons**: Compare COVID-19 impact across multiple countries
- **Mortality Rate Analysis**: Understand death rates by country
- **Growth Rate Tracking**: Monitor recent growth trends (7-day and 30-day)
- **Visual Heatmaps**: See patterns across countries and time
- **Data Export**: Export summary statistics to CSV

## ?? Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Analysis

1. Launch Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `covid_analysis.ipynb` in your browser

3. Run all cells (Cell ? Run All) or execute them one by one

## ?? Project Structure

```
.
??? covid_analysis.ipynb    # Main analysis notebook
??? requirements.txt         # Python dependencies
??? COVID_ANALYSIS_README.md # This file
```

## ?? Data Source

The analysis uses real-time data from the **Johns Hopkins University COVID-19 Data Repository**:
- GitHub: [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
- Data is automatically fetched when you run the notebook
- No manual data download required!

## ?? Analysis Sections

The notebook is organized into the following sections:

1. **Setup and Data Loading** - Import libraries and fetch latest COVID data
2. **Data Preprocessing** - Clean and aggregate data by country
3. **Global Trends** - Visualize worldwide pandemic progression
4. **Country Comparisons** - Compare cases and deaths across nations
5. **Top Countries Analysis** - Detailed look at most affected countries
6. **Mortality Rate Analysis** - Calculate and compare death rates
7. **Growth Rate Analysis** - Track recent infection trends
8. **Heatmap Visualization** - See patterns across time and geography
9. **Summary Statistics** - Comprehensive overview of key metrics
10. **Key Insights** - Data-driven conclusions
11. **Export Results** - Save findings to CSV

## ?? Sample Visualizations

The notebook generates multiple visualizations including:

- ? Cumulative case trends over time
- ? Daily new cases with 7-day rolling average
- ? Country-by-country comparisons
- ? Top countries bar charts
- ? Mortality rate rankings
- ? Growth rate comparisons
- ? Temporal heatmaps

## ?? Output Files

Running the notebook will generate:
- `covid19_summary.csv` - Summary statistics for all countries

## ?? Updating Data

The notebook fetches the latest data automatically from Johns Hopkins University each time you run it. Simply re-run the cells to get updated statistics!

## ?? Customization

You can easily customize the analysis:

- **Change countries**: Modify the `top_countries` list in section 4
- **Adjust time periods**: Change the date ranges in various analyses
- **Minimum cases threshold**: Adjust `min_cases` variable in section 6
- **Number of days for trends**: Modify the `days` parameter in growth calculations
- **Visual styles**: Change color schemes and plot styles

## ?? Notes

- Data quality depends on reporting standards in each country
- Testing rates vary significantly between countries
- Some countries may have incomplete or delayed reporting
- Mortality rates are affected by many factors including age demographics, healthcare capacity, and testing rates

## ?? Contributing

Feel free to enhance this analysis by:
- Adding more visualization types
- Implementing predictive models
- Including vaccination data
- Adding geographic map visualizations
- Performing statistical hypothesis testing

## ?? License

This project uses publicly available COVID-19 data from Johns Hopkins University. Please cite the data source when using this analysis.

## ?? Acknowledgments

- Johns Hopkins University Center for Systems Science and Engineering (CSSE)
- All healthcare workers and data scientists tracking the pandemic

---

**Last Updated**: 2025-10-31

For questions or issues, please refer to the notebook documentation within each cell.
