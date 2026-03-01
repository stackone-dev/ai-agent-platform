# PLUGIN SYSTEM FOR AGENT TOOL USAGE
# Flexible plugin architecture with hot-reload support

import absc
from typing import Any, Callable, List, Dict

class PluginInterface(abc.ABC):
   "Base interface for all plugins"
    @abc.abstractmethod
    def get_name(self) -> str:
        pass
    
    @abc.abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.plugin_paths = []
    
    def register_plugin(self, plugin: PluginInterface) -> None:
        "Register a plugin for use in agent actions"
        self.plugins[plugin.get_name()] = plugin
    
    def hot_reload(self, plugin_name: str) -> None:
        "Reload a specific plugin without restarting the agent"
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            # Reimport the plugin module

    def get_plugin(self, name: str) -> PluginInterface:
        return self.plugins.get(name)
