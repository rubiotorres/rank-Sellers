from src.envs.get_env import get_env_value

# Database vars
DB_PASSWORD = get_env_value('DB_PASSWORD', 'tWbSGkZ9VkmmaSMM')
DB_HOST = get_env_value('DB_HOST', 'localhost')
DB_DATABASE = get_env_value('DB_DATABASE', 'sales')
DB_PORT = get_env_value('DB_PORT', 3306)
DB_USER = get_env_value('DB_USER', 'debian-sys-maint')
DB_CONN_STRING = get_env_value('DB_CONN_STRING', 'mysql+pymysql://{}:{}@{}:{}')
DB_CHARSET = get_env_value('DB_CHARSET', 'utf8')
DB_CONN_TIMEOUT_SEC = get_env_value('DB_CONN_TIMEOUT_SEC', 60)
POOLED_DB_MINCACHED = int(get_env_value('POOLED_DB_MINCACHED', 1))
POOLED_DB_MAXCACHED = int(get_env_value('POOLED_DB_MAXCACHED', 1))
POOLED_DB_MAXSHARED = int(get_env_value('POOLED_DB_MAXSHARED', 1))
POOLED_DB_MAXCONNECTIONS = int(get_env_value('POOLED_DB_MAXCONNECTIONS', 1))
POOLED_DB_BLOCKING = get_env_value('POOLED_DB_BLOCKING', False)
POOLED_DB_MAXUSAGE = int(get_env_value('POOLED_DB_MAXUSAGE', 0))
POOLED_DB_RESET = get_env_value('POOLED_DB_RESET', True)
POOLED_DB_PING = int(get_env_value('POOLED_DB_PING', 1))
