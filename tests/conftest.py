import sys, os
import pytest

path = os.path.join(os.path.dirname(__file__), "..", "source")

sys.path.insert(0, path)  # add 'hybridmethod' library path for importing into the tests


from hybridmethod import hybridmethod


class MyClass(object):
    """This sample class provides hybrid methods that allow items to be added to and
    removed from the class-level list and the item-level list without needing to define
    separate methods to manage either list. The class also offers some helper methods to
    provide access to the class-level list, instance-level lists and a combined list."""

    items: list[object] = []

    def __init__(self):
        # Create an 'items' instance variable; note that this shadows the class variable
        # of the same name which can still be accessed directly via self.__class__.items
        self.items: list[str] = []

    @hybridmethod
    def add_item(self, item: object):
        # We can use the following line to differentiate between the call being made on
        # an instance or directly on the class; isinstance(self, <class>) returns True
        # if the method was called on an instance of the class, or False if the method
        # was called on the class directly; the 'self' variable will reference either
        # the instance or the class; although 'self' is traditionally used in Python as
        # reference to the instance
        if isinstance(self, MyClass):
            self.items.append(item)
        else:
            self.items.append(item)

    @hybridmethod
    def remove_item(self, item: object):
        if (index := self.items.index(item)) >= 0:
            del self.items[index]

    def get_class_items(self) -> list[object]:
        return self.__class__.items

    def get_instance_items(self) -> list[object]:
        return self.items

    def get_combined_items(self) -> list[object]:
        return self.__class__.items + self.items
