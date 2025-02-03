from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator
import random


with DAG(
    dag_id="dags_bash_with_template", #DAG 이름(DAG 파일명과 DAG 이름은 통일하는 것이 좋음)
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 12, tz="Asia/Seoul"), #DAG가 언제 돌기 시작하는지(timezone을 설정해야 함)
    catchup=False, #누락된 구간을 업데이트 할 것인가(DAG 구조에 따라 문제가 될 수 있기 때문에 기본값은 False로 두자)
    tags=["jinja_template"] #태그를 눌렀을 떄, 해당 태그에 대응하는 값만 볼 수 있다
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command='echo "data_interval_end: {{data_interval_end}}"'
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        env={
            'START_DATE':'{{data_interval_start | ds}}',
            'END_DATE':'{{data_interval_end | ds}}'
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    bash_t1 >> bash_t2