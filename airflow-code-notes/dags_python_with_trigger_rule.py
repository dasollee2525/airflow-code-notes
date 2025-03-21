from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_trigger_rule",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023,3,1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_upstream_1 = BashOperator(
        task_id='bash_upstream_1',
        bash_command = 'echo upstream1'
    )

    @task(task_id='python_upstream_1')
    def python_upstream_1():
        raise AirflowException('downstream_1 Exception!')

    @task(task_id='python_upstream_2')
    def python_upstream_2():
        print("Success")

    @task(task_id='python_downstream_1', trigger_rule='all_done')
    def python_downstream_1():
        print("Success")

    [bash_upstream_1, python_upstream_1(), python_upstream_2()] >> python_downstream_1()