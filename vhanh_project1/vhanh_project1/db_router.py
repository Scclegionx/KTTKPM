class ECommerceDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'customer':
            return 'mysql_db'
        if model._meta.app_label == 'product':
            return 'ecommercedb'
        if model._meta.app_label == 'cart':
            return 'cartdb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'customer':
            return 'mysql_db'
        if model._meta.app_label == 'product':
            return 'ecommercedb'
        if model._meta.app_label == 'cart':
            return 'cartdb'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'customer':
            return db == 'mysql_db'
        if app_label == 'product':
            return db == 'ecommercedb'
        if app_label == 'cart':
            return 'cartdb'
        return db == 'default'