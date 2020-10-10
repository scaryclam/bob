rabbitmq_plugin_rabbitmq_management:
  rabbitmq_plugin:
    - name: rabbitmq_management
    - enabled
    - runas: root

manager:
  rabbitmq_user.present:
    - password: vagrant
    - tags:
      - administrator
    - perms:
      - '/':
        - '.*'
        - '.*'
        - '.*'
