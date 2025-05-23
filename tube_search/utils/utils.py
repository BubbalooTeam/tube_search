from typing import List, Union

class TubeUtils:
    def getValue(self, source: dict, path: List[str]) -> Union[int, str, dict, None]:
        """
        Get the result of a dict, using the keys passed by [path].

        Args:
            source - (dict): The dictionary with all the information needed for get.
            path: List(str): The key directory that guides you to the final result requested from the dictionary.
        
        Returns:
            Union[int, str, dict, None]: Result of the information requested from the dictionary by the key directory.
        """

        value = source
        for key in path:
            if type(key) is str:
                if key in value.keys():
                    value = value[key]
                else:
                    value = None
                    break
            elif type(key) is int:
                if len(value) != 0:
                    value = value[key]
                else:
                    value = None
                    break
        return value