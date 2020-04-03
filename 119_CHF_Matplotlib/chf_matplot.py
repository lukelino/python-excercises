#! python3
""" Pobiera dane kursu z PostgreSQL i rysuje wykres """

import chf_functions


def main():
    conn, cur = chf_functions.connect()
    chf_functions.select_data(conn, cur)
    user_data = str(input('User data yyyy-mm-dd: '))
    chf_functions.select_user_data(conn, cur, user_data)
    chf_functions.close_connection(conn, cur)


if __name__ == '__main__':
    main()
