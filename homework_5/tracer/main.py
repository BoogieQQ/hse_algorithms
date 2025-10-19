def trace_recursion(func):
    depth = [0]
    
    def wrapper(*args, **kwargs):
        tabs = "\t" * depth[0] + f'{depth[0]+1}. '
    
        args_str = ", ".join(
            filter(
                None, 
                [
                    ", ".join([str(arg) for arg in args]), 
                    ", ".join([f"{k}={str(v)}" for k, v in kwargs.items()])
                ]
                )
            )
        
        print(f"{tabs} put {func.__name__}({args_str})")
        depth[0] += 1
    
        result = func(*args, **kwargs)
        
        depth[0] -= 1
        
        print(f"{tabs} get {func.__name__}() = {str(result)}")
        
        return result
    
    return wrapper
