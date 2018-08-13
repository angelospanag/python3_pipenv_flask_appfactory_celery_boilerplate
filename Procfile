web: gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app('development')"
worker_1: celery worker -A celery_worker.celery --loglevel=info -n worker1@%h
worker_2: celery worker -A celery_worker.celery --loglevel=info -n worker2@%h
worker_3: celery worker -A celery_worker.celery --loglevel=info -n worker3@%h
worker_4: celery worker -A celery_worker.celery --loglevel=info -n worker4@%h
worker_5: celery worker -A celery_worker.celery --loglevel=info -n worker5@%h
worker_6: celery worker -A celery_worker.celery --loglevel=info -n worker6@%h
worker_7: celery worker -A celery_worker.celery --loglevel=info -n worker7@%h
worker_8: celery worker -A celery_worker.celery --loglevel=info -n worker8@%h
worker_9: celery worker -A celery_worker.celery --loglevel=info -n worker9@%h
worker_10: celery worker -A celery_worker.celery --loglevel=info -n worker10@%h
