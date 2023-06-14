
# GUIDED PROJECT: Covid-19 Analysis

This guided project involves performing analysis on COVID-19 data using SQL queries. The project covers various aspects of the data, including total cases, total deaths, population, vaccinations, and more. The SQL queries are executed using SQL Server Management Studio (SSMS) against the database named `proj1`.




## Prerequisites 

Before running the SQL queries, make sure you have the following: 

- Microsoft SQL Server 2019 is installed, 2022 version throughs error while importing the csv files.
- SQL Server Management Studio (SSMS) installed.
## Roadmap

- Open SQL Server Management Studio (SSMS) and connect to the appropriate database or create a new one
- Retrieve all records from the CovidDeaths table
- Alter the datatype of the `total_cases` and `total_deaths` columns in the `CovidDeaths` table to float
- Calculate the death percentage for each date in India
- Calculate the percentage of total cases with respect to the population for each date in India
- Determine the highest infection rates by country
- Find the number of people who died in each country
- Find the number of people who died in each continent
- Calculate global numbers per day, including `total cases`, `total deaths`, and `death percentage`
- Calculate global numbers in total, including` total cases`, `total deaths`, and `death percentage`
- Join the `CovidDeaths` and `CovidVaccinations` tables based on location and date
- Retrieve total population and new vaccinations data by location and date, along with the rolling count of vaccinations
- Calculate the percentage of the vaccinated population using a Common Table Expression (CTE)



## Lessons Learned

When I first encountered window functions and common table expressions (CTEs), I must admit that I was quite unfamiliar with these concepts. They seemed complex and daunting at first. However, as I delved into learning about them, I came across an excellent example that made everything so much easier to understand. The example showcased how window functions can be used to calculate rolling counts and percentages within groups, while CTEs provided a structured and readable way to break down complex queries. The step-by-step explanation and the visual representation of the data in the example made it crystal clear how these powerful tools can be used to manipulate and analyze data effectively. I was pleasantly surprised by how quickly I grasped the concept and could apply it to my own analysis. Now, I feel more confident in using window functions and CTEs in my SQL queries to gain deeper insights from my data. I need to practice more SQL commands utilising CTEs and Window functions so I can get familiarized.


## Documentation

- [Dataset](https://ourworldindata.org/covid-deaths)
- [YouTube Tutorial](https://www.youtube.com/watch?v=qfyynHBFOsM&t=1070s)

