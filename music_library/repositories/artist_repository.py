from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album


def save(artist):
    sql = f'INSERT INTO artists (name, id = None) VALUES (%s, %s) RETURNING *'
    values = [artist.name, artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def delete_all():
#      sql = 'DELETE FROM artists'
# #     # run_sql(sql)


def select(id):
    album = None 
#     # sql = 'SELECT * FROM artists WHERE id = %s'
#     # values = [id]
#     # result = run_sql(sql, values)[0]


def select_all():
    albums = []
#     sql = f'SELECT * FROM artists'
#     results = sql_run(sql)
#     for row in results:
#         album = album_repository.select(row['album id'])
#         artist = Artist(row['name'], row['id'])
#         albums.append(artist)


# Extensions


def albums(artist):
    pass


def delete(id):
    pass


def update(artist):
    pass
