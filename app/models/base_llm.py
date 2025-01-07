from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    async def generate_response(self, prompt: str, **kwargs):
        pass
    
    @abstractmethod
    async def generate_stream(self, prompt: str, **kwargs):
        pass 