from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 10, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["2024-10-26"]
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoareyou"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2