import inspect

class PrintMixin:


    def __init__(self,*args, **kwargs):
        print(repr(self))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        # Пытаемся получить параметры из __init__
        try:
            sig = inspect.signature(self.__class__.__init__)
            init_params = set(sig.parameters.keys()) - {'self'}

            params = []
            # Сначала добавляем параметры из __init__
            for param_name in init_params:
                if hasattr(self, param_name):
                    value = getattr(self, param_name)
                    params.append(f'{param_name}={value!r}')

            # Затем добавляем остальные атрибуты
            for key, value in self.__dict__.items():
                if key not in init_params and not key.startswith('_'):
                    params.append(f'{key}={value!r}')

        except (ValueError, TypeError):
            # Если не удалось получить сигнатуру, используем все атрибуты
            params = [f'{key}={value!r}' for key, value in self.__dict__.items()
                      if not key.startswith('_')]

        params_str = ', '.join(params)
        return f'{self.__class__.__name__}({params_str})'