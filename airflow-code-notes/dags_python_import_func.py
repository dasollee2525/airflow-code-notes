from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp


with DAG(
    dag_id="dags_python_operator", #DAG 이름(DAG 파일명과 DAG 이름은 통일하는 것이 좋음)
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 10, 1, tz="Asia/Seoul"), #DAG가 언제 돌기 시작하는지(timezone을 설정해야 함)
    catchup=False, #누락된 구간을 업데이트 할 것인가(DAG 구조에 따라 문제가 될 수 있기 때문에 기본값은 False로 두자)
    tags=["2025-01-08"] #태그를 눌렀을 떄, 해당 태그에 대응하는 값만 볼 수 있다
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id = 'task_get_sftp',
        python_callable = get_sftp
    )

    py_t1