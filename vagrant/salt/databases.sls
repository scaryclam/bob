vagrant_user:
  postgres_user.present:
    - name: vagrant
    - password: vagrant
    - createdb: true
    - user: postgres
    - superuser: true

scheduler_db:
  postgres_database:
    - present
    - name: scheduler
    - encoding: UTF8
    - user: postgres

manager_db:
  postgres_database:
    - present
    - name: manager
    - encoding: UTF8
    - user: postgres

