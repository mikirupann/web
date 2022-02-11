from flask import Flask

app = Flask(__name__)


def main():
    pass


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
