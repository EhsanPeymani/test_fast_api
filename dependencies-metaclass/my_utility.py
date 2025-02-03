from my_service import MyService


# we do not instantiate the service in the module. We simply use a factory method to get the [unique] service instance.
def get_service() -> MyService:
    return MyService()
