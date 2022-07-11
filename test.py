import copy
import psycopg2
import pandas


def get_all_cols(cursor):
    cursor.execute(
        'SELECT column_name, data_type FROM information_schema.columns WHERE table_schema=\'public\' AND table_name=\'loan_data\'')
    columns_output = cursor.fetchall()
    return [column[0] for column in columns_output]


def get_all_rows(cursor):
    cursor.execute('SELECT * from loan_data')
    return cursor.fetchall()


def update_loan_data(dataframe):
    # Creating a copy of dataframe as we don't want to change the original one
    new_dataframe = copy.copy(dataframe)
    exisiting_int_rate = new_dataframe['int_rate']
    new_dataframe['int_rates_add_2pct'] = exisiting_int_rate + 0.02*(exisiting_int_rate)

    new_dataframe = new_dataframe[(new_dataframe['term'] == '36 months') & (
        new_dataframe['loan_status'] != 'Fully Paid')]
    updated_months = int(new_dataframe['term'].str.split(' ')[0][0]) + 12
    new_dataframe['new_term'] = f'{updated_months} months'
    new_dataframe.to_csv('new_loan_data.csv')


if __name__ == "__main__":
    conn = psycopg2.connect(
        host="f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud",
        database="q2c",
        port="30835",
        user="q2c_user",
        password="passw0rd")

    # create a cursor
    cursor = conn.cursor()

    # create DataFrame
    dataframe = pandas.DataFrame(data=get_all_rows(cursor), columns=get_all_cols(cursor))
    update_loan_data(dataframe)
