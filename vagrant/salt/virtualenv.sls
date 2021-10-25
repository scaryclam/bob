bob_env:
  file.directory:
    - name: /virtualenv/bob
    - user: vagrant
    - group: vagrant
    - makedirs: True
    - recurse:
      - user
      - group
      - mode

/virtualenv/bob/scheduler:
  virtualenv.managed:
    - use_wheel : False
    - system_site_packages: False
    - requirements: /build/requirements-scheduler.txt
    - user: vagrant
    - python: /usr/bin/python3.9

/virtualenv/bob/runner:
  virtualenv.managed:
    - use_wheel : False
    - system_site_packages: False
    - requirements: /build/requirements-runner.txt
    - user: vagrant
    - python: /usr/bin/python3.9

/virtualenv/bob/manager:
  virtualenv.managed:
    - use_wheel : False
    - system_site_packages: False
    - requirements: /build/requirements-manager.txt
    - user: vagrant
    - python: /usr/bin/python3.9

/virtualenv/bob/viewer:
  virtualenv.managed:
    - use_wheel : False
    - system_site_packages: False
    - requirements: /build/requirements-viewer.txt
    - user: vagrant
    - python: /usr/bin/python3.9

