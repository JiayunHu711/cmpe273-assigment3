from collections import OrderedDict

def lru_cache(size):
    my_cache = OrderedDict()

    def decorator_lru_cache(func):
        func_name = func.__name__

        def wrapper_lru_cache(*args, **kwargs):
            key = args[0]
            output = func_name + "(" + str(key) + ") -> " 
                
            if key in my_cache:
                # Delete existing key before refreshing it
                value = my_cache[key]
                print("[cache-hit]: " + output + str(value))
                del my_cache[key]
            else:
                value = func(*args, **kwargs)
                print(output + str(value) )
            my_cache[key] = value

            if len(my_cache) > size:
                # Delete oldest
                my_cache.popitem(last=False)



            return value
        return wrapper_lru_cache
    return decorator_lru_cache
    
    

