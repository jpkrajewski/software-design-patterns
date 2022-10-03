from abc import ABC, abstractmethod


class MQTTDevice:
    """Interface used by client code"""
    def get_current_info(self):
        return 'device=thermometer,value=32.4342'


class Chart3rdPartyService:
    """Service requires JSON format to properly create chart"""
    def create_chart(self):
        print(f'Creating chart from {self.data}')


class MQTTDeviceFormatToJSONChart(MQTTDevice, Chart3rdPartyService):
    def create_chart(self):
        print(f'Formatting mqtt device info...({self.get_current_info()})')
        self.data = [{'device': 'thermometer', 'value': 32.4342}]
        super().create_chart()


adapter = MQTTDeviceFormatToJSONChart()
adapter.create_chart()

# Formatting mqtt device info...(device=thermometer,value=32.4342)
# Creating chart from [{'device': 'thermometer', 'value': 32.4342}]