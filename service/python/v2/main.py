from apistar import App, Route
import platform
import requests


def env():
    resp = requests.get('http://' + 'service-go' + '/env')
    data = resp.json()
    return {
        "message": 'Python' + platform.python_version() + '----->' + data['message']
    }


routes = [
    Route('/env', method='GET', handler=env),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('0.0.0.0', 80)