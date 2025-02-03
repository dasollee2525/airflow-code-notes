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
    bash_var = BashOperator(
        task_id = "bash_var"
        bash_command="echo variable:{{var.value.sample_key}}"
    )