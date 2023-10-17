import os


class CreateMixin:
    def perform_create(self, serializer):
        new_object = serializer.save()
        new_object.owner = self.request.user
        new_object.save()