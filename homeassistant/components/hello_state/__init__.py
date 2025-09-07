"""Test adding a new feature."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "hello_state"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Hello State component."""
    hass.states.set("hello_state.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True
