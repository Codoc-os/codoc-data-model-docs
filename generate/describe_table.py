import os
import psycopg2
import csv
import argparse
from dotenv import load_dotenv

load_dotenv()


def describe_table(table_name, save=False):
    connection_params = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
    }
    conn = psycopg2.connect(**connection_params)
    cur = conn.cursor()

    # Columns infos
    cur.execute(f"""
        SELECT
            cols.column_name,
            cols.data_type,
            cols.is_nullable,
            cols.is_identity,
            cols.character_maximum_length,
            cols.numeric_precision,
            cols.numeric_scale
        FROM
            information_schema.columns cols
        WHERE
            cols.table_name = '{table_name}'
        ORDER BY
            cols.ordinal_position;
    """)
    columns = cur.fetchall()

    # Foreign Key infos
    cur.execute(f"""
        SELECT
            kcu.column_name,
            ccu.table_name AS foreign_table,
            ccu.column_name AS foreign_column
        FROM
            information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
            ON tc.constraint_name = kcu.constraint_name
        JOIN information_schema.constraint_column_usage AS ccu
            ON ccu.constraint_name = tc.constraint_name
        WHERE
            tc.constraint_type = 'FOREIGN KEY'
            AND tc.table_name = '{table_name}';
    """)
    fks = cur.fetchall()
    fk_map = {col: (ftable, fcol) for col, ftable, fcol in fks}

    desc = [["Field", "User Guide", "ETL Conventions", "Datatype", "Required", "Primary Key", "Foreign Key", "FK Table"]]
    for col_name, data_type, is_nullable, is_identity, char_max_len, num_precision, num_scale in columns:
        type_str = data_type
        type_str = type_str.replace("character varying", "varchar")
        type_str = type_str.replace("timestamp with time zone", "timestamptz")
        if char_max_len:
            type_str += f"({char_max_len})"
        elif num_precision:
            type_str += f"({num_precision},{num_scale})" if num_scale else f"({num_precision})"

        required = 'Yes' if is_nullable == 'NO' else 'No'
        pk = 'Yes' if is_identity == 'YES' else 'No'
        fk_info = fk_map.get(col_name)
        has_fk = 'Yes' if fk_info else 'No'
        fk_table = fk_info[0] if fk_info else '\" \"'

        desc.append([col_name, " ", " ", type_str, required, pk, has_fk, fk_table])

    for row in desc:
        print(",".join(row))

    if save:
        current_dir = os.path.dirname(__file__)
        files_dir = os.path.join(current_dir, "files")
        file_path = os.path.join(files_dir, f"{table_name}.csv")
        with open(file_path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerows(desc)

    cur.close()
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate description of a table"
    )
    parser.add_argument("--table", required=True, type=str, help="table name to describe")
    parser.add_argument("--save", action="store_true", help="save the results in files/<table>.csv")
    args = parser.parse_args()
    describe_table(args.table, args.save)
