import  structlog
import logging

def setup_logging():
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO
    )
    structlog.configure(
        wrapper_class = structlog.make_filtering_bound_logger(logging.INFO),
        processors=[
            structlog.processors.TimeStamper(fmt = 'iso'),
            structlog.processors.JSONRenderer()
        ]
    )


logger = structlog.get_logger()

