from app import app
# noinspection PyUnresolvedReferences
from callbacks import change_menu_page, upload_file


if __name__ == '__main__':
    app.run_server(debug=False)
