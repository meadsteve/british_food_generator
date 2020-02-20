import logging

GUNICORN_ERROR_LOG = "gunicorn.error"
LOGGER_NAME = "british.food"

gunlog = GUNICORN_ERROR_LOG in logging.root.manager.loggerDict  # type: ignore
if gunlog:
    log = logging.getLogger(GUNICORN_ERROR_LOG).getChild(LOGGER_NAME)
else:
    log = logging.getLogger(LOGGER_NAME)
