import sqlfluff
import argparse

def lint_sql_file(file_path):
    lint_results = sqlfluff.lint(file_path)
    return lint_results

def main():
    parser = argparse.ArgumentParser(description="Lint an SQL file using sqlfluff.")
    parser.add_argument("file_path", type=str, help="Path to the SQL file to lint.")
    args = parser.parse_args()

    results = lint_sql_file(args.file_path)
    if results:
        for result in results:
            print(result)
    else:
        print("No linting errors found.")

if __name__ == "__main__":
    main()
