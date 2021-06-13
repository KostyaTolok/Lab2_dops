import configparser


class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        storage = {}
        for k, v in namespace.items():
            if k == "file_path":
                parser = configparser.ConfigParser()
                parser.read(v)
                for key, value in parser["settings"].items():
                    storage[key] = value

        for key, value in storage.items():
            namespace[key] = value

        new_cls = super(MyMeta, mcs).__new__(mcs, name, bases, namespace)
        return new_cls


class Student(metaclass=MyMeta):
    file_path = "settings.ini"


print(Student.__dict__)
