###########################################################################MODULES
from nornir import InitNornir
###########################################################################PLUGINS
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_jinja2.plugins.tasks import template_file
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
##################################################################################



nr = InitNornir(config_file='/home/ibi/Documents/Git/Nornir/Blueprints/config.yaml')

def show_command(task):
    showVer = task.run(netmiko_send_command, command_string="show ver")
    result = showVer.result
    print(result)

nr.run(task=show_command)
