from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()
engine = create_engine('sqlite:///my_users')
users = Table('Users', metadata, 
        Column('id', Integer, primary_key = True),
        Column('name', String)
)
metadata.create_all(engine)
insert_query = users.insert().values(id=1, name='Sashka')


