# Flask SocketIO Server for swergio communication

This is a simple implementation of a Flask-SocketIO server to handle the communication in a swergio setup.

The default server settings are:
    HOST = '0.0.0.0'
    PORT = 5000

The list of available namespaces is required and can be provided as environment variable "NAMESPACES" (e.g. NAMESPACES = namespace1,namespace2). These namespaces must be aligned with the other swergio components.

#### References

Flask-SocketIO (https://github.com/miguelgrinberg/Flask-SocketIO)