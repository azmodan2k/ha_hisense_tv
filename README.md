# Hisense TV Integration for Home Assistant

Integration an Hisense TV as media player into Home Assistant. The communication is handled via the integrated MQTT broker and wake-on-LAN.
Requires Home Assistant >= `2021.12.x`.

## Current features:
* Turn on / off
* Display current status
  * Source (TV, HDMI, Apps)
  * Channel name / number
  * EPG data of current show
* Volume control
* Media browser
  * LNB selector
  * Channel selector
  * Apps
* Read picture setting

TBD:
* Expose ON/OFF as switch
* Expose all keys as buttons
* Enhance EPG/guide handling

## Configuration

The TV provides a MQTT broker on port `36669`. Home Assistant can only communicate with one MQTT broker, so you have to create a bridge between the two broker.

## MQTT

Implementation of direct mqtt connection to Hisense MQTT Broker. I've created a seperate HomeAssistant instance because I wasn't able to get the mosquitto mqtt bridge working

Connection shema:
```
+-----------+          +-------------+
| Home      |  client  | Hisense TV  |
| Assistant |--------->| MQTT Broker |
+-----------+          +-------------+
```
## Wake-on-LAN

The TV can be turned on by a Wake-on-LAN packet. The MAC address must be configured during integration setup.

## Setup in Home Assistant

The integration can be added via the Home Assistant UI. Add the integration and setup your TV. During the first setup your TV should be turned on. The integration requires a PIN code from you TV. The PIN will be triggered automatically during setup. This is a onetime step where the client `HomeAssistant` is requesting access to remote controll the TV.

# YMMV

Tested on an [Hisense A71 Series](https://hisenseme.com/product/75-65-58-55-50-43-a71-series/) with mandatory client certificates. `gettvstate` does not return a `state` but can be used to authenticate the client.
The 

# Acknowledgment
Everything I needed to write this integration could be gathered from these sources. Information about the MQTT topics, credentials or certificates can be found there.

* [@sehaas](https://github.com/sehaas/ha_hisense_tv)
* [@Krazy998's mqtt-hisensetv](https://github.com/Krazy998/mqtt-hisensetv)
* [@newAM's hisensetv_hass](https://github.com/newAM/hisensetv_hass)
* [HA Community](https://community.home-assistant.io/t/hisense-tv-control/97638/1)
* [RemoteNOW App](https://play.google.com/store/apps/details?id=com.universal.remote.ms)
* [@d3nd3](https://github.com/d3nd3/Hisense-mqtt-keyfiles)
