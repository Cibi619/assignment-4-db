
# Assignment 4 — Database Migrations with Flyway, Ansible & CI/CD

For Q2, I did these main things:

1. Used Ansible to:

- start a MySQL 8 container
- create DB + user
- run initial Flyway migrations automatically

2. Flyway migration scripts:

- migrations_initial → base schema
- migrations_incremental → extra column + index

3. Add GitHub Actions (ci.yml):

- spin up MySQL service on runner
- run initial + incremental migrations
- run pytest CRUD test
- print “Deployment done for commit...”

4. Write test_subscribers.py:

- test full CRUD: create, read, update, delete

Local Setup – How I run it on my machine

I am using Windows + WSL2 (Ubuntu) + Docker Desktop.
All Ansible commands I ran inside Ubuntu terminal.

Prerequisites:

On my system I made sure I have:

- Docker Desktop (WSL integration enabled)
- WSL2 (Ubuntu)
- Python 3 + pip
- Ansible
- pytest and pymysql (installed from requirements.txt)

Ansible – Bring MySQL Up & Down

All Ansible files are in ansible/ folder.

ansible/up.yml performs these steps:

- Starts a Docker container: a4-mysql using mysql:8
- Waits for MySQL to become healthy
- Creates DB user:
- user: sub_user
- password: sub_pass
- Runs initial Flyway migrations using Flyway Docker image
- Runs scripts from flyway/migrations_initial

To run up.yml:

From inside Ubuntu:

cd ~/assignment4/ansible,

ansible-playbook up.yml


If everything is ok, play recap shows:

0 failed

Run initial Flyway migrations → changed
