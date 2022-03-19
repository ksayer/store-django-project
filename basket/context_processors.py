from .basket import Basket


def basket(request):
    """
    Allow change and take session data
    """
    return {'basket':  Basket(request)}
