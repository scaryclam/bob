from datetime import datetime

from peewee import PostgresqlDatabase


database = PostgresqlDatabase(
    'manager',
    user='vagrant',
    password='vagrant',
    host='127.0.0.1',
    port=5432)


class JobService:
    def get_active_jobs(self):
        active_jobs = self._get_jobs_query(
            "SELECT * FROM job WHERE status IN ('created', 'running')")
        return active_jobs

    def get_jobs(self):
        jobs = self._get_jobs_query("SELECT * FROM job")
        return jobs

    def _get_jobs_query(self, query):
        columns = database.get_columns('job')

        cursor = database.execute_sql(query)

        jobs = []
        for row_index in range(0, cursor.rowcount):
            job_row = cursor.fetchone()
            job_row_data = {}

            for index, column in enumerate(columns):
                if column.data_type.startswith('timestamp'):
                    job_row_data[column.name] = datetime.strftime(
                        job_row[index], "%Y-%M-%d %H:%M:%S")
                else:
                    job_row_data[column.name] = job_row[index]

            jobs.append(job_row_data)
        return jobs
