
# Calculate Order History

I used numpy in python to analyze amazon data to see how much money I spent on the e-commerce website. (All figures are in rupees.)


## Procedure

    1. Download report from amazon.in/amazon.com
    2. Import necessary dependencies
    3. Read the downloaded report and store it as a dataframe
    4. Remove any NULL placeholders with 0 using df.fillna(0)
    5. In my document, since the last line was an unnecessary string, I removed the row using df.iloc(:-1,:)
    6. Replace 'Rs.' with a blank string and convert to float
    7. Sum the total
    8. Plot the graph



## Run Locally

Clone the project

```bash
  git clone https://github.com/adithyaravi12/online_courseworks/tree/main/amazon-bill
```

Go to the project directory

```bash
  cd amazon-bill
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Screenshots

![App Screenshot](https://github.com/adithyaravi12/online_courseworks/blob/main/amazon-bill/calc.png)

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://adithyaravi12.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adithya-ravi-707443126/)
