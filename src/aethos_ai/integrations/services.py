"""Service integration stubs."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class IntegrationStatus:
    name: str
    ready: bool
    detail: str


class BaseIntegration:
    name: str = "base"

    def status(self) -> IntegrationStatus:
        return IntegrationStatus(name=self.name, ready=False, detail="not configured")


class GoogleIntegration(BaseIntegration):
    name = "google"


class OpenAIIntegration(BaseIntegration):
    name = "openai"


class LlamaIntegration(BaseIntegration):
    name = "llama"


class AlpacaIntegration(BaseIntegration):
    name = "alpaca"


class AutoGPTIntegration(BaseIntegration):
    name = "autogpt"
