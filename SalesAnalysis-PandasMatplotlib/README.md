# Ecommerce Sales Analysis

### Project Objectives
The primary objectives of this project were to identify the best performing month for sales, determine the top-selling city, optimize advertisement timing, and understand which products were frequently sold together.

### Project Scope
The scope of this project included cleaning and analyzing sales data collected from multiple CSV files. The focus was on addressing missing values, transforming data types, and generating visualizations to support data-driven decision-making.

### Technologies Used
- Python (Pandas, NumPy)
- Matplotlib

### Solution and Approach:
1. Data Cleaning: NaN values were dropped from the DataFrame to ensure accurate analysis. Rows not meeting specific conditions were also removed. Columns were transformed using methods like to_numeric, to_datetime, and astype to ensure consistency.

2. Aggregation: Using the pd.concat function, multiple CSV files were combined into a comprehensive DataFrame. Columns were added to enhance the dataset. String parsing techniques were employed to extract meaningful information.

3. Data Analysis: The .apply() method was used to calculate total sales and extract month and city information. The groupby function was utilized to aggregate data and answer key questions.

4. Data Visualization: Bar charts and line graphs were created using Matplotlib to visualize insights. These visualizations provided an intuitive way to understand sales trends and patterns.

### Results and Achievements:
The project successfully answered the following questions:

- The best month for sales and the corresponding revenue.
- The city with the highest sales.
- Optimal advertisement timing for maximizing customer engagement.
- Frequently sold together product combinations.

### Future Enhancements:
In the future, this project could be expanded to incorporate predictive modeling to forecast sales trends. Additionally, integrating external data sources could provide further context for analysis and decision-making.

### Visuals

<img width="425" alt="image" src="https://github.com/tejaswini-girish/Data-Analytics-Projects/assets/136778982/c2953252-a388-48ac-8989-d107a39c6e28">
<br>
<img width="421" alt="image" src="https://github.com/tejaswini-girish/Data-Analytics-Projects/assets/136778982/a56491ad-dc7b-4017-8c88-2ea9813ad661">
<br>
<img width="420" alt="image" src="https://github.com/tejaswini-girish/Data-Analytics-Projects/assets/136778982/2a542337-61e6-462a-b9d3-8e47adbd66ac">
<br>
<img width="380" alt="image" src="https://github.com/tejaswini-girish/Data-Analytics-Projects/assets/136778982/0a057e92-4ab3-48f7-b3f7-258e4cd446ce">



