from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository


def save(album):
    sql = f'INSERT INTO albums (title, artist, genre, id = None) VALUES (%s, %s, %s, %s) RETURNING *'
    values = [album.title, album.artist, album.genre, album.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


# def delete_all():
#     # sql = 'DELETE FROM albums'
#     # run_sql(sql)

# def select(id):
#     # album = None 
#     # sql = 'SELECT * FROM albums WHERE id = %s'
#     # values = [id]
#     # result = run_sql(sql, values)[0]

# def select_all():
#     albums = []
#     sql = f'SELECT * FROM albums'
#     results = sql_run(sql)
#     for row in results:
#         artist = artist_repository.select(row['artist id'])
#         album = Album(row['title'], row['artist'], row['genre'], row['id'])
#         albums.append(artist)



# Extensions

def delete(id):
    pass


def update(album):
    pass
