# Pour le "design pattern" "Singleton"

class SingletonMeta(type):
    """
    Utilisation de MetaClass (pour palier au problème de l'input qui continue pas)
    """
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            # Crée une nouvelle instance si elle n'existe pas
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        else:
            # Ré-initialise l'instance avec de nouveaux arguments
            cls._instance.__init__(*args, **kwargs)
        return cls._instance
