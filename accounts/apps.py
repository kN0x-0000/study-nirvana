from django.apps import AppConfig
from django.utils.autoreload import autoreload_started


def my_watchdog(sender, **kwargs):
	sender.watch_file('/tmp/foo.bar')
	

class AccountsConfig(AppConfig):
	name = 'accounts'

	def ready(self):
		import accounts.signals
