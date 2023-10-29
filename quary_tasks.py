import sqlite3

def connect_to_data_base(data_base, query_file_name) -> list():
    conn = sqlite3.connect(data_base)
    cursor = conn.cursor()

    with open(query_file_name, "r") as query_file:
        queries = query_file.read().split(';')

    for query in queries:
        if query.strip():
            cursor.execute(query)

    results = cursor.fetchall()
    conn.close()
    return results

def first_query():
    con_result = connect_to_data_base("home.db", "query_one.sql")
    print(con_result)

def second_query():
    con_result = connect_to_data_base("home.db", "query_two.sql")
    print(con_result)

def third_query():
    con_result = connect_to_data_base("home.db", "query_three.sql")
    print(con_result)

def fourth_query():
    con_result = connect_to_data_base("home.db", "query_four.sql")
    print(con_result)

def fifth_query():
    con_result = connect_to_data_base("home.db", "query_five.sql")
    print(con_result)

def sixth_query():
    con_result = connect_to_data_base("home.db", "query_six.sql")
    print(con_result)

def seventh_query():
    con_result = connect_to_data_base("home.db", "query_seven.sql")
    print(con_result)

def eighth_query():
    con_result = connect_to_data_base("home.db", "query_eight.sql")
    print(con_result)

def ninth_query():
    con_result = connect_to_data_base("home.db", "query_nine.sql")
    print(con_result)

def tenth_query():
    con_result = connect_to_data_base("home.db", "query_ten.sql")
    print(con_result)

if __name__ == "__main__":
    first_query()
    # second_query()
    # third_query()
    # fourth_query()
    # fifth_query()
    # sixth_query()
    # seventh_query()
    # eighth_query()
    # ninth_query()
    # tenth_query()
