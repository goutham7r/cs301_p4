import csv
import pandas as pd

def describe_data():
    df = pd.read_csv('IMDB-Movie-Data.csv')
    print(df.head().to_string(index=False))
    print()

def readData():
    imdb_movie_data = {}
    with open('IMDB-Movie-Data.csv') as csvimdb_movie_dataFile:
        csvReader = csv.reader(csvimdb_movie_dataFile)
        header=True
        for row in csvReader:
            if header:
                header=False
                continue
            # key = rank
            imdb_movie_data[int(row[0])] = {'Title':row[1],'Description':row[3],'Director':row[4],'Actors':row[5],'Year':int(row[6]),'Runtime':int(row[7]),'Rating':float(row[8]),'Revenue':float(row[9])}
            # key = title
            imdb_movie_data[row[1]] = {'Rank':int(row[0]),'Description':row[3],'Director':row[4],'Actors':row[5],'Year':int(row[6]),'Runtime':int(row[7]),'Rating':float(row[8]),'Revenue':float(row[9])}
    return imdb_movie_data

def getMovieData(field, MovieName=None, Rank=None):
    if MovieName is not None:
        if MovieName not in imdb_movie_data:
            print("Invalid Movie Name")
            return -1 
        if field not in imdb_movie_data[MovieName]:
            print("Invalid Field Name")
            return -1
        return imdb_movie_data[MovieName][field]

    if Rank is not None:
        if Rank not in imdb_movie_data:
            print("Invalid Rank, enter a number between 1 and 1000")
            return -1 
        if field not in imdb_movie_data[Rank]:
            print("Invalid Field Name")
            return -1
        return imdb_movie_data[Rank][field]

    print("Please specify either the Movie Name or Rank")


imdb_movie_data = readData()