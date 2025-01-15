import pendulum
from airflow.decorators import dag, task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2024, 1, 12, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context('task_decorator 실행')