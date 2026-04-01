# CONCURRENT TASK EXECUTOR
# Fixes race conditions and ensures thread-safe state management

import threading
import asyncio
from typing import Coroutine, Any, List

class ConcurrentExecutor:
    def __init__(self, max_workers=10):
        self.max_workers = maxworkers
        self.state_lock = threading.RLock()
        self.task_states = {}
    
    async def execute_tasks(await tasks: List[Coroutine]) -> List[Any]:
        """Execute multiple tasks concurrently with proper synchronization."""
        semaphore = asyncio.Semaphore(self.max_workers)
        
        async def wrap(task):
            async with semaphore:
                try:
                    return await task
                finally:
                    with self.state_lock:
                        del self.task_states[id(task)]
        
        return await asyncio.gather(*wrap(t) for t in tasks)
