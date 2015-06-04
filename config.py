#Configuration

#DBMS Setting

dbms_host = {  'MySQL'      : 'mysql+mysqldb://root@localhost/log_host'
             , 'PostgreSQL' : 'postgresql+psycopg2://owen@localhost/'

            }

__SQLALCHEMY_DATABASE_URI = dbms_host['MySQL']

