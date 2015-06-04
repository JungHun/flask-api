# -*- coding: utf-8 -*-
import sys , os
sys.path.append(os.getcwd().replace('/api','',1))
from   flask          import Flask , request
from   sqlalchemy.sql import func
from   model          import Host
from   database       import init_db, db_session
import json
import pytest
import logging
import time

# subject : fizzbuz
# Auther  : Junghun , Kim
# Date    : 2015-06-04

app = Flask(__name__)

@app.route('/<int:number>/fizzbuzz/' , methods = ['POST','GET'])

# get_number
# arg    : number     , 입력 수
# retrun : set_log    , 입력 수 DB 저장 함수
#@pytest.fixture(scope="function", params=[1,378])
def get_number(number):
    return set_log(number)

# set_log
# arg     : number      , 입력 수
# return  : request_sum , 현재까지 입력된 전체 수의 합
#@pytest.fixture(scope="function", params=[182,01])
def set_log(number):
    logging.basicConfig(filename = '../log/fizzbuzz_' + time.strftime("%Y%m%d") + '.log' , level = logging.DEBUG)
    # 시작로그
    logging.info('Started')

    request_verb  = request.method
    send_number   = None
    action_verb   = None
    request_sum   = None

    if   request_verb  == 'POST':
         send_number    = number + 1  # 입력 수에 1를 더함.
         action_verb    = 1;
    elif request_verb  == 'GET':
         send_number    = number
         action_verb    = 0;

    #DB 설정

    try :
        init_db()
    except Exception as e :
        logging.warning('DB Connection Error|MSG:'+Exception)

    try :
        #Data 삽입
        host = Host(send_number , action_verb)

        #DB Session 설정
        db_session.add(host)
        db_session.commit()

        #Data 조회 , 현재까지 입력된 전체 수의 합
        query = db_session.query(func.sum(Host.send_number))
        request_sum = int(query.scalar())

        if request_sum == '' :
            raise RuntimeError('DB Select Error')

        db_session.remove()

    except Exception as e :
        logging.warning('DB Select Error|MSG:'+Exception)
        db_session.remove()

    return json_result(request_sum)

# json_result
# arg     : request_sum  , 현재까지 입력된 전체 수의 합
# return  : JSON         , {"fizzbuzz" : "fizz"}
#@pytest.fixture(scope="function", params=[182,01])
def json_result(request_sum):

    x      = request_sum
    result = None

    if x % 3 == 0 and x % 5 == 0 :
        result = 'FizzBuzz'
    elif x % 5 == 0 :
        result = 'Buzz'
    elif x % 3 == 0 :
        result = 'Fizz'
    else :
        result = 'None'

     # 종료로그
    logging.info('Finished')

    return json.dumps({"fizzbuzz" : result})

# 404 에러 log
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
