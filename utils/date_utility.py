
class DateUtility():

    @staticmethod
    def find_root_user(users):
        """Find root user
        """
        root_user = None
        for user in users:
            if root_user is None:
                root_user = user
            if user.get('CreateDate')<root_user.get('CreateDate'):
                root_user = user
        return root_user
