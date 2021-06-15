import configparser
import json


class MyMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        storage = {}
        with open(kwargs.get('file_path'), 'r') as file:
            storage = json.load(file)

        namespace.update(storage)
        new_cls = super(MyMeta, mcs).__new__(mcs, name, bases, namespace)
        return new_cls


class Student(metaclass=MyMeta, file_path="settings.json"):
    pass


print(Student.__dict__)
