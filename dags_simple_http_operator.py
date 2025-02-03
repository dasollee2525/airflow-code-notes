from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id = 'dags_simple_http_operator',
    start_date=pendulum.datetime(2023,4,1,tz='Asia/Seoul'),
    catchup=False,
    schedule=None
) as dag:
    '''서울시 야겸명소 정보'''
    seoul_night_view_info = SimpleHttpOperator(
        task_id = 'seoul_night_view_info',
        http_conn_id = 'openapi.seoul.go.kr',
        endpoint='{{var.value.apikey_openapi_seoul_go_kr}}/xml/viewNightSpot/1/5/',
        method='GET',
        headers={'Content-Type' : 'application/json',
        'charset':'utf-8',
        'Accept': '*/*'
        }
    )

    @task(task_id='python_2')
    def python_2(**kwargs):
        ti=kwargs['ti']
        rslt = ti.xcom_pull(task_ids='seoul_night_view_info')
        print("XCom pulled value:", rslt)

    seoul_night_view_info >> python_2()
