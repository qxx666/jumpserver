from .escape.manager import EscapeRouteExecutionManager
from .escape.handlers import EscapeRouteHandler


class ExecutionManager:
    manager_type = {
        'escape': EscapeRouteExecutionManager
    }

    def __new__(cls, execution):
        manager = cls.manager_type[execution.manager_name]
        return manager(execution)


class TaskHandler:
    handler_type = {
        'escape': EscapeRouteHandler
    }

    def __new__(cls, task):
        handler = cls.handler_type[task.handler_name]
        return handler(task)
