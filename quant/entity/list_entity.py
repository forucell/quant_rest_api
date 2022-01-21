from clean_architecture.entity import Entity


class ListEntity(Entity):
    def __init__(self, items=[]):
        self.items = items

    @classmethod
    def from_dict(cls, adict):
        _list = ListEntity(
            items=adict.get("items"),
        )
        return _list
