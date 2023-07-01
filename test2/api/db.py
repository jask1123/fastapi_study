from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

#DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
ASYNC_DB_URL = "mysql+aiomysql://sample_user:@db:3306/demo?charset=utf8"


async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

Base = declarative_base()

def get_db():
    with async_session() as session:
        yield session