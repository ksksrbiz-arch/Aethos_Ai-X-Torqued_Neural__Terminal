"""Integration registry for external AI services."""

from __future__ import annotations

from dataclasses import dataclass, field

from .services import (
    AlpacaIntegration,
    AutoGPTIntegration,
    BaseIntegration,
    GoogleIntegration,
    IntegrationStatus,
    LlamaIntegration,
    OpenAIIntegration,
)


@dataclass
class IntegrationRegistry:
    _integrations: dict[str, BaseIntegration] = field(default_factory=dict)

    def load_defaults(self) -> None:
        self.register("google", GoogleIntegration())
        self.register("openai", OpenAIIntegration())
        self.register("llama", LlamaIntegration())
        self.register("alpaca", AlpacaIntegration())
        self.register("autogpt", AutoGPTIntegration())

    def register(self, name: str, integration: BaseIntegration) -> None:
        self._integrations[name] = integration

    def available(self) -> list[str]:
        return sorted(self._integrations.keys())

    def statuses(self) -> list[IntegrationStatus]:
        return [integration.status() for integration in self._integrations.values()]
