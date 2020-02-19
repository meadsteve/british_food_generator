import logging
from asyncio import get_running_loop, sleep, AbstractEventLoop

log = logging.getLogger(__name__)


class Monitor:
    lag: float = 0

    def __init__(self, interval: float):
        self._interval = interval

    def start(self):
        loop = get_running_loop()
        loop.create_task(self._monitor_lag(loop))

    async def _monitor_lag(self, loop: AbstractEventLoop):
        log.info("Monitoring async lag started")
        while loop.is_running():
            start = loop.time()
            await sleep(self._interval)
            # The closer this gap is to our intended sleep time
            # the less load the system is under. Large gaps mean
            # the running loop is dealing with a lot of work
            time_slept = loop.time() - start
            self.lag = time_slept - self._interval
            log.debug(f"Current async lag (ms): {self.lag * 1000}")
        log.info("Monitoring async lag stopped")
