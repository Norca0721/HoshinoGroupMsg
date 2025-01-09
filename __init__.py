from hoshino import Service, priv
from hoshino.log import new_logger

log = new_logger('HoshinoBroadcast')

SV_HELP = 'nothing'
sv = Service('HoshinoBC', manage_priv=priv.SUPERUSER, enable_on_default=False, help_=SV_HELP, visible=False)