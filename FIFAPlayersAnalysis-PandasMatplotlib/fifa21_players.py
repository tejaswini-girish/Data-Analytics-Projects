import pandas as pd
import zipfile
import numpy as np

pd.set_option('display.max_columns', None)


def read_datasets(zipf):
    datasets = {}
    with zipfile.ZipFile(zipf, "r") as arch:
        datafiles = [datafile for datafile in arch.namelist() if datafile.split(".")[1] == "csv"]
        for datafile in datafiles:
            datasets[datafile.split(".")[0]] = pd.read_csv(arch.open(datafile))
    return datasets


def main():
    datasets = read_datasets("archive.zip")
    #height_weight_dtype(datasets)
    #break_date_cols(datasets)
    #clean_and_transform_cols(datasets)
    age_classification(datasets)
    


## 1. Check for dtype of two columns
def height_weight_dtype(datasets):    
    for key, dataset in datasets.items():
        if(dataset["height_cm"].dtype == 'int64' and dataset["weight_kg"].dtype == 'int64'):
            print(f"{key} => Columns : Height and Weight are of type int64")


## 2. Break date column into multiple columns
def break_date_cols(datasets):
    for key, dataset in datasets.items():
        dataset[["joined_y","joined_d","joined_m"]] = dataset["joined"].str.split("-", expand=True)
        print(dataset.loc[:, ["joined","joined_y","joined_m", "joined_d"]])


## 3. Clean and transform specific columns
def clean_and_transform_cols(datasets):
    for key, dataset in datasets.items():
        dataset.fillna({"release_clause_eur":0, "wage_eur":0, "value_eur":0}, inplace=True)
        dataset = dataset.astype({"release_clause_eur":'int', "wage_eur":'int', "value_eur":'int'})


## 4. Check number of players in each age range category
def age_classification(datasets):
    for key, dataset in datasets.items():
        print(dataset.groupby(pd.cut(dataset['age'], np.arange(15,55,5)))['sofifa_id'].count().dtype)
        break
        



if __name__ == "__main__":
    main()




    