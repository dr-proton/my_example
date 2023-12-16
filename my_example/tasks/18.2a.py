from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import yaml


def send_config_commands(device, config_commands, log=True):
        try:
            if log:
                print(f"Connecting: {device['host']}")
            with ConnectHandler(**device) as ssh:
                ssh.send_config_set(config_commands)
        except NetmikoTimeoutException:
             print("Не удалось подключиться к устройству!")
        except NetmikoAuthenticationException:
             print("Неверный логин или пароль!")
        except ValueError:
             print("Не настроен привилегированный  режим")
            


if __name__ == "__main__":
    commands = ["interface fa0/1", "speed 100", "full-duplex", "no shutdown"]
    with open("devices.yaml", "r") as file:
        lst_device = yaml.safe_load(file)

    for data in lst_device:
        send_config_commands(data, commands, True)
            