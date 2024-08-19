from flask import Flask, request, jsonify
import csv
import datetime
import os

app = Flask(__name__)

@app.route('/collect', methods=['POST'])
def collect_info():
    info = request.get_json()
    ip_address = request.remote_addr
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f'{ip_address}_{timestamp}.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Processor', 'OS Name', 'OS Version', 'Users', 'Processes'])
        writer.writerow([info['processor'], info['os_name'], info['os_version'], ', '.join(info['users']), ', '.join(info['processes'])])
    return jsonify({'message': 'Información almacenada correctamente'})

@app.route('/query', methods=['GET'])
def query_info():
    ip_address = request.args.get('ip')
    if ip_address:
        filename = f'{ip_address}_{datetime.datetime.now().strftime("%Y-%m-%d")}.csv'
        if os.path.exists(filename):
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                return jsonify({'data': data})
        else:
            return jsonify({'message': 'No se encontró información para la IP especificada'})
    else:
        return jsonify({'message': 'Debe proporcionar una IP'})

if __name__ == '__main__':
    app.run(debug=True)