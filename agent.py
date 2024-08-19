import psutil
import platform
import requests

def get_system_info():
    info = {}
    info['processor'] = platform.processor()
    info['os_name'] = platform.system()
    info['os_version'] = platform.version()
    info['users'] = [user.name for user in psutil.users()]
    info['processes'] = [proc.name() for proc in psutil.process_iter()]
    return info

def send_info_to_api(info):
    api_url = 'http://localhost:5000/collect'
    response = requests.post(api_url, json=info)
    if response.status_code == 200:
        print('Información enviada correctamente')
    else:
        print('Error al enviar información')

if __name__ == '__main__':
    info = get_system_info()
    send_info_to_api(info)