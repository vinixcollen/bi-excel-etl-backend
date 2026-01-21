from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Upload" ADD "file_url" VARCHAR(250) NOT NULL;
        ALTER TABLE "Upload" ALTER COLUMN "file_name" TYPE VARCHAR(100) USING "file_name"::VARCHAR(100);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Upload" DROP COLUMN "file_url";
        ALTER TABLE "Upload" ALTER COLUMN "file_name" TYPE VARCHAR(50) USING "file_name"::VARCHAR(50);"""


MODELS_STATE = (
    "eJztl2tvmzAUhv8K4lMrbVVL04uiaRJN6MqUJlUu29R1Qg6YxKoxKZi1Wdf/Ph8DAZyUJd"
    "MuqbQvKZyLfc4T+z3pox6EHqbxnokj4k71pvaoMxRg8aB4Xmk6ms0KOxg4GlMZioqYccwj"
    "5HJh9RGNsTB5OHYjMuMkZMLKEkrBGLoikLBJYUoYuUuww8MJ5lMcCcfnL8JMmIcfcJy/zm"
    "4dn2DqVUolHuwt7Q6fz6TNZvxcBsJuY8cNaRKwIng259OQLaIJ42CdYIYjxDEsz6MEyofq"
    "sj7zjtJKi5C0xFKOh32UUF5qd00GbsiAn6gmlg1OYJfXxkHjpHF6eNw4FSGykoXl5Cltr+"
    "g9TZQEukP9SfoRR2mExFhw+4qjGEpagteaomg1vVKKglAUriLMgdUxzA0FxOLg/CaKAXpw"
    "KGYTDgfcODqqYfbB7LcuzP6OiNqFbkJxmNMz3s1cRuoDsAVIuBobQMzCXybAg/39NQCKqG"
    "cBSl8VoNiR4/QOViG+H/S6qyGWUhSQHnG59l2jJF661NsBtIYf9AtFB3F8R8vYdi7NTyrR"
    "Vqd3JvsPYz6J5CpygTNBF8TSvy1dezCMkXt7jyLPWfKERvhc7LIrMALVghiaSFbQMfSXjY"
    "/RjIaoqtZVT+1gKcVszWAZjez2BpMlSYi3Bzm/chR/PmD0N37CXGCgyZ3go/FW/yNnUx7D"
    "w+Nd9cjJ7uonjU8oduTLBjJZSfovlguYMfm2guO5uCrP/OTJExSGPmRsJ8UaaO3e6KxjaV"
    "d9q2UP7Ewt55lapk4wCQPhss2+ZXYUgonUFew5aMXIaQsSnAR4NUslVR09We5e/rCdePUI"
    "I6/H6DyTlBrcQ/vSGgzNy6vKVGqbQws8RpV+Zt05Vo7zYhHtoz280OBVu+51LVVJFnHDax"
    "1qQgkPHRbeO8grqV9uzcFULwdHPIlXy4zFkkB+q7aggZiLl2/KIvvv6Y1+1e+1rMHA7r5b"
    "1m19MGqBs6llDzfs3LQ7VruppX9vWJHe1JSlNlartcSqRqtUqZISnkR0Y9nPcl6m6htH64"
    "AUUTX/Y0iU//RH3NMP9fAiOw=="
)
