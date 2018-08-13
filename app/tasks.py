from . import celery


# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(2.0, test.s(), name='Hello every 2 seconds')
#

