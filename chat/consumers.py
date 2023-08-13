from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "room"
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )


class Notification(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "room"
        self.room_group_name = "notify_%s" % self.room_name

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )
