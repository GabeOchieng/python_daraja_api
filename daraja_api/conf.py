import abc

class AbstractConfig(abc.ABC):

    @abc.abstractmethod
    def get_consumer_key(self)->str:
        raise NotImplementedError('Not implemented error')

    @abc.abstractmethod
    def get_consumer_secret(self)->str:
        raise NotImplementedError('Not implemented error')

    @abc.abstractmethod
    def get_environment(self)->str:
        raise NotImplementedError('Not implemented error')

    @abc.abstractmethod
    def get_shortcode(self)->str:
        raise NotImplementedError('Not implemented error')

    @abc.abstractmethod
    def get_express_shortcode(self)->str:
        raise NotImplementedError('Not implemented error')

    @abc.abstractmethod
    def get_shortcode_type(self)->str:
        raise NotImplementedError('Not implemented error')

    @abc.abstractmethod
    def get_passkey(self)->str:
        raise NotImplementedError('Not implemented error')

class ConfigFromObject(AbstractConfig):
    
    def __init__(self,obj):
        self.obj=obj
        required_attrs=['MPESA_ENVIRONMENT','MPESA_CONSUMER_KEY','MPESA_CONSUMER_SECRET']
        for i in required_attrs:
            self.get_attr_from_obj(i)
        allowed_env = ['sandbox','production']
        setattr(obj,'MPESA_ENVIRONMENT',getattr(obj,'MPESA_ENVIRONMEN').lower())
        if getattr(obj,'MPESA_ENVIRONMENT') not in allowed_env:
            raise Exception('Allowed environments values:'+','.join(allowed_env))
        
    def get_attr_from_obj(self, attr):
        try:
            _v=getattr(self.obj,attr)
            if type(_v) != str or _v='':
                raise Exception('{attr} must be a string, cannot be empty'.format(attr=attr))
            return _v
        except AttributeError:
            if raise_exception:
                raise Exception('{attr} is required'.format(attr=attr))

    def get_consumer_key(self)->str:
        return self.get_attr_from_obj('MPESA_CONSUMER_KEY')

    def get_consumer_secret(self)->str:
        return self.get_attr_from_obj('MPESA_CONSUMER_SECRET')

    def get_environment(self)->str:
        return self.get_attr_from_obj('MPESA_ENVIRONMENT')

    def get_shortcode(self)->str:
        return self.get_attr_from_obj('MPESA_SHORTCODE')

    @abc.abstractmethod
    def get_express_shortcode(self)->str:
        return self.get_attr_from_obj('MPESA_EXPRESS_SHORTCODE')

    @abc.abstractmethod
    def get_shortcode_type(self)->str:
        return self.get_attr_from_obj('MPESA_SHORTCODE_TYPE')

    @abc.abstractmethod
    def get_passkey(self)->str:
        return self.get_attr_from_obj('MPESA_PASSKEY')



