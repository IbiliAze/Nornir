from nornir import InitNornir
# from nornir.plugins.functions.text import print_result
# from nornir.plugins.tasks.networking import netmiko_send_commands

nr = InitNornir(config_file='/home/ibi/Documents/Git/Nornir/Blueprints/config.yaml')

# def show_command(task):
#     showVer = task.run(netmiko_send_commands, command_string="show ver")
#     result = showVer.result
#     print(result)

# nr.run(task=show_command)
