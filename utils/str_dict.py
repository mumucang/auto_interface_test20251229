import json


class StrDict:

    @staticmethod
    def str_to_dict(s: str) -> dict:
        """


        :param s:
        :return:
        """

        dict_value = json.loads(s)

        return dict_value