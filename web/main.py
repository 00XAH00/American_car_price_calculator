from app import app
# noinspection PyUnresolvedReferences
import callbacks
from core.settings import settings

if __name__ == '__main__':
    app.run_server(
        host=settings.host,
        port=settings.port,
        debug=settings.debug_mode
    )
