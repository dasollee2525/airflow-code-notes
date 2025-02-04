from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator
from airflow import DAG
import pendulum

with DAG(
    dag_id="dags_seoul_api",
    schedule="7 * * * *",
    start_date=pendulum.datetime(2025, 2, 5, tz="Asia/Seoul"),
    catchup=False
) as dag:

    # 서울시 코로나19 확진자 발생동향
    viewNightSpot_info = SeoulApiToCsvOperator(
        task_id="viewNightSpot_info",
        dataset_nm="viewNightSpot",
        path="/opt/airflow/files/viewNightSpot/{{ data_interval_end.in_timezone('Asia/Seoul') | ds_nodash }}",
        file_name="viewNightSpot.csv"
    )

    viewNightSpot_info
