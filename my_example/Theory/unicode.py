import subprocess

res = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'], stdout=subprocess.PIPE, encoding="utf-8")
print(res.stdout)