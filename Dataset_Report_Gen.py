# imports
import pandas as pd
import os
from ydata_profiling import ProfileReport

def make_report():
    # Create a list of all files in 'datasets' using os
    files = []
    for file in os.listdir('datasets'):
        if file.endswith('.csv'):
            files.append(file)

    # Generate reports for each file with a counter
    counter = 0
    for file in files:
        df = pd.read_csv('datasets/' + file)
        df_report = ProfileReport(df)
        df_report.to_file('reports/' + file + str(counter) + '.html')
        counter += 1
        print(f'Generated report {counter} of {len(files)}')
    print("Generated all reports")

def edit_reports():
    counter = 0
    for file in os.listdir('reports'):
        if file.endswith('html'):
            os.rename('reports/' + file, 'reports/' + str(counter) + file[:-6] + '.html')
            counter += 1
            

if __name__ == "__main__":
    # make_report()
    edit_reports()