class MultiSerializerMixin:
  """
  A mixin that lets you choose a different Mixin based on the action

  e.g. You might want to .show and .list a foreign key's name
  whereas when you'll want to send the foreign primary key id when you .create or .update
  """
  serializer_classes = {}
  default_serializer_class = None

  def get_serializer_class(self):
    if hasattr(self, 'action'):
      return self.serializer_classes.get(self.action, self.default_serializer_class)
    return self.default_serializer_class
