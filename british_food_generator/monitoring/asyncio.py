import collections
from asyncio import get_running_loop, sleep, AbstractEventLoop, Task
from typing import Any

from british_food_generator.app_logging import log


class Monitor:
    lag: float = 0
    active_tasks: int = 0

    def __init__(self, interval: float, warn_threshold: float = 0.1):
        self._interval = interval
        self._warn_threshold = warn_threshold

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

            tasks = [task for task in Task.all_tasks(loop) if not task.done()]
            self.active_tasks = len(tasks)
            log.debug(f"Active tasks: {self.active_tasks}")

            self._warn(tasks)
        log.info("Monitoring async lag stopped")

    def _warn(self, tasks):
        if self.lag >= self._warn_threshold:
            tasks_count = collections.Counter(_get_coroutine_name(task) for task in tasks)
            log.warning(f"Slow loop detected. Lag: {self.lag * 1000}ms Tasks: {str(tasks_count)}")


def _get_coroutine_name(task: Any) -> str:
    try:
        return task._coro.__name__
    except:
        return "unknown"
