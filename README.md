# zabbix-aruba-sensor-monitoring

This python module provides Zabbix monitoring support for Aruba sensors using the Aruba User Experience Insight API. This API is currently in closed beta state and subjective to change at any time.



## Requirements

- Zabbix agent
- pip
- requests (installed automatically as dependency)



## Installation

1. Install the python module using pip.

```
pip install https://github.com/digiaiiris/zabbix-aruba-sensor-monitoring/releases/download/1.0.1/aruba-sensor-monitoring-1.0.1.tar.gz
```

2. Copy the [Zabbix agent configuration](etc/zabbix/zabbix_agentd.d/ic_aruba.conf) to /etc/zabbix/zabbix_agentd.d directory.

3. Restart the Zabbix agent.



## Usage

### Resource discovery

Item Syntax | Description | Units |
----------- | ----------- | ----- |
aruba.discover.sensors[api_url, api_key, app_id] | Discover sensors from Aruba's status API. | {#SENSOR_NAME}, {#SENSOR_UID} |



### Aruba sensor status

Item Syntax | Description | Units |
----------- | ----------- | ----- |
aruba.sensor.status[api_url, api_key, app_id, sensor_uid] | Retrieve sensor status from Aruba's status API. | error, warning, offline, pending, good |



### API URL
The current URL for Aruba sensor API is https://api.capenetworks.com/v1/nodes



## Examples

### List available sensors from Aruba's status API
```
aruba_discover_sensors "<api_url>" "<api_key>" "<app_id>"
```



### Retrieve sensor status from Aruba's status API
```
aruba_sensor_status "<api_url>" "<api_key>" "<app_id>" "<sensor_uid>"
```
