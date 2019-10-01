from library import Base

# How do you make sure that self.bar exists ?
# assert hasattr(Base, "bar")


class Derived(Base):
    def baz(self):
        return "baz"

