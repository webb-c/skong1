import pynecone as pc


config = pc.Config(
    app_name="skong1",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
