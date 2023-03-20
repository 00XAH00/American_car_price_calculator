from app import app
# noinspection PyUnresolvedReferences
import callbacks


if __name__ == '__main__':
    app.run_server(debug=False)
