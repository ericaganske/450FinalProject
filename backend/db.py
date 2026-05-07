import psycopg

DATABASE_URL = "postgresql://neondb_owner:npg_cva6yD2GJUet@ep-snowy-rain-angzlv8w-pooler.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def get_connection():
    return psycopg.connect(DATABASE_URL)