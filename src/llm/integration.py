# CORE LLM INTEGRATION LAYER
# This module provides the core LLM integration# multi-provider support for OpenAI, Anthropic, and local models.

class LLMIntegrator:
    def __init__(self, provider, model):
        self.provider = provider
        self.model = model
        self.retry_logic = IntelligentRetryLogic()
        self.prompt_optimizer = PromptOptimizer()

    def invoke(self, prompt, temperature=0.7):
        """Invoke the LLM with automatic retry logic and rate limiting."""
        optimized_prompt = self.prompt_optimizer.optimize(prompt)
        return self.retry_logic.execute(
            lambda: self._call_provider(optimized_prompt, temperature)
        )
