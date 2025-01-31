from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg1",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023,3,1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_push = BashOperator(
        task_id='bash_push',
        bash_command="echo START && "
                     "echo XCOM_PUSHED "
                     "{{ti.xcom_push(key='bash_pushed', value='first_bash_message')}} && "
                     "echo COMPLETE"  
                     # 마지막 값을 출력값으로 인지함 
    )

    bash_pull = BashOperator(
        task_id='bash_pull',
        env={
            'PUSHED_VALUE':"{{ti.xcom_pull(key='bash_pushed)}}",
            'RETURN_VALUE':"{{ti.xcom_pull(task_ids='bash_push)}}"
        },
        bash_command="echo $PUSHED_VALUE && echo $RETURN_VALUE ",
        do_xcom_push=False #값이 xcom에 올라가지 않도록 함
    )

    bash_push >> bash_pull

