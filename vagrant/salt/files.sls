/home/vagrant/.bashrc:
  file:
    - managed
    - source: salt://bashrc
    - user: vagrant
    - group: vagrant

