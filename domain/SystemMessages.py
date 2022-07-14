
class SystemMessages:

    def detailed(description, system_message):
        if issubclass(type(description), Exception):
            description = str(description)

        system_message['description'] = description
        return system_message

    class General:
        COULD_NOT_CONNECT_TO_SERVER = {
            "error": {"reason": "The requested system server was not avaliable, try again later."}
        },
        SERVER_NOT_FOUND = {
            "error": {"reason": "The requested system server was not found."}
        },
        INVALID_TOKEN = {
            "error": {"reason": "Access denied because your token is invalid."}
        },
        INVALID_QUERY_PARAMETER = {
            "error": {"reason": "The query parameter used is invalid."}
        },
        QUERY_PARAMETER_NOT_FOUND = {
            "error": {"reason": "The query parameter used was not found."}
        }
        
