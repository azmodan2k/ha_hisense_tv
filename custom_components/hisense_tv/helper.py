"""Hisene TV integration helper methods."""
import asyncio
import logging

from homeassistant.components import mqtt
from homeassistant.const import MAJOR_VERSION, MINOR_VERSION

from .const import DEFAULT_CLIENT_ID

_LOGGER = logging.getLogger(__name__)


async def mqtt_pub_sub(hass, pub, sub, payload=""):
    """Wrapper for publishing MQTT topics and receive replies on a subscibed topic."""
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    def put(*args):
        loop.call_soon_threadsafe(queue.put_nowait, args)

    async def get():
        while True:
            yield await asyncio.wait_for(queue.get(), timeout=10)

    unsubscribe = await mqtt.async_subscribe(hass=hass, topic=sub, msg_callback=put)
    await mqtt.async_publish(hass=hass, topic=pub, payload=payload)
    return get(), unsubscribe


class HisenseTvBase(object):
    """Hisense TV base entity."""

    def __init__(
        self,
        hass,
        name: str,
        mac: str,
        uid: str,
        ip_address: str,
    ):
        self._client = DEFAULT_CLIENT_ID
        self._hass = hass
        self._name = name
        self._mac = mac
        self._ip_address = ip_address
        self._unique_id = uid
        self._icon = (
            "mdi:television-clean"
            if MAJOR_VERSION <= 2021 and MINOR_VERSION < 11
            else "mdi:television-shimmer"
        )
        self._subscriptions = {
            "tvsleep": lambda: None,
            "state": lambda: None,
            "volume": lambda: None,
            "sourcelist": lambda: None,
        }

    def _out_topic(self, topic=""):
        try:
            out_topic = topic % self._client
        except:
            out_topic = topic % self._client
        _LOGGER.debug("_out_topic: %s", out_topic)
        return out_topic

    def _in_topic(self, topic=""):
        try:
            in_topic = topic % self._client
        except:
            in_topic = topic
        _LOGGER.debug("_in_topic: %s", in_topic)
        return in_topic
