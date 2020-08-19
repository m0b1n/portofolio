from logging.handlers import RotatingFileHandler


class IpFinderHandler(RotatingFileHandler, object):
    def emit(self, record):
        record.ip = '0.0.0.0'
        try:
            request = record.args[0]
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                record.ip = x_forwarded_for.split(',')[0]
            else:
                record.ip = request.META.get('REMOTE_ADDR')

            record.args = None
        except:
            pass

        super(IpFinderHandler, self).emit(record)
