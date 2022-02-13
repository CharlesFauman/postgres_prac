# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
def init_schema():
    engine = create_engine("postgresql://postgres:password@localhost/postgres")
    with engine.connect() as conn:
        raw_conn = conn.connection
        cur = raw_conn.cursor()
        cur.exeecute("CREATE SCHEMA myschema")
        conn.commit()


init_schema()

# %%
def write_to_db(name, df):
    engine = create_engine(
        "postgresql://postgres:password@localhost/postgres",
        connect_args={"options": "-csearch_path=myschema"},
    )
    with engine.connect() as conn:
        df.to_sql(df_name, conn, if_exists="replace", index=False)
        conn.commit()


# %%
df = pd.DataFrame.from_records(
    [
        {"id": 5},
        {"name": "bobby"},
    ]
)
df_name = "dfname"

write_to_db(df_name, df)
