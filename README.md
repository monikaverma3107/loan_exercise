## Task Details

- Using Python, create a connection to the postgres database:

```
Database type : PostgresSQL
host: f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud
port: 30835
dbname: q2c
Username : q2c_user
password : passw0rd
```

- Load the data from the q2c database (schema name : public | table name : loan_data) and perform the following operation to generate your result:
  - Create a new column called **new term**, for the records with **term** is equal to '36 months' and **loan_status** is not equal to 'Fully Paid' update **new term** coumn with existing value of (**term** + 12 months)
  - Create a new column called **int_rates_add_2pct**, for every record udpate **int_rates_add_2pct** column with existing value of (**int_rate** + 2%).
- Ouput the result into a csv file.

## How to run the script

- Run the following command to install dependencies:
  `pip install -r requirements.txt`
- Run the test.py script to generate `new_loan_data.csv` file with updated loan details
