## flask-api

### Run
./api/controllers.py로 실행


### Table Name : log_host.host_info

| column        | data type  | description     |
|:-------------:|:----------:|:---------------:|
| access_no     | int        | sequence        |
| send_number   | int        | response number |
| action_verb   | char(1)    | request type    |

### File Structure
```python
~/flask-api
    |-- config.py
    |-- database.py
    |-- alembic.ini
    |__ /venv              # Virtual Environment (/lib/alembic/)
    |__ /api               # fizzbuz API
         |-- controllers.py
         |-- model.py
    |__ /log
```
