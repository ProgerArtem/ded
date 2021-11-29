from sql_interface import DbChinook

class Search_engine():
    def __init__(self, db=DbChinook()):
        self.db = db

    def select_all_tracks(self):
        """Вибрати всі записи про треки та вивести їх"""
        res = self.db.select("""SELECT * FROM tracks;
        """)
    
    def search_track(self,search_text):
        search_text = '%'+search_text+'%'
        res=self.db.select('''SELECT Name FROM tracks
            WHERE Name LIKE ?
        ''', search_text)
        return res
    def select(self, search_info):
        search_info = '%'+search_info+'%'
        print(search_info)
        t1=self.db.select('''SELECT genres.Name FROM genres 
                             INNER JOIN tracks ON tracks.GenreId=genres.GenreId
                             WHERE tracks.Name LIKE ?;
                        ''', search_info);
            #SELECT TrackId FROM Tracks
            #WHERE Name LIKE ?;'''
        print("RESULT", t1)
        return t1
    def albom(self, search_info2):
        search_info2 = '%'+search_info2+'%'
        print(search_info2)
        t1=self.db.select('''SELECT albums.Title FROM albums
                             INNER JOIN tracks ON tracks.AlbumId=albums.AlbumId
                             WHERE tracks.Name LIKE ?;
                        ''', search_info2);
            #SELECT TrackId FROM Tracks
            #WHERE Name LIKE ?;'''
        print("RESULT", t1)
        return t1
    




if __name__=="__main__":
   from sql_interface import DbChinook
   db = DbChinook()
   engine = Search_engine(db)
   engine.select_all_tracks()
#skoro konez