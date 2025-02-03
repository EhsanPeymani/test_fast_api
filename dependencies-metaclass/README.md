Here, I am going to use the module-based singleton pattern and FastAPI dependency injection.

The service generates random numbers to mimic receiving data from remote sensors.
The data is stored internally, and are accessible via `property: numbers`.

The idea is to fetch data in a loop, so `MyService::update` is called in a background thread,
and REST service is run on the main thread. 

In practice, one needs to make it thread safe.