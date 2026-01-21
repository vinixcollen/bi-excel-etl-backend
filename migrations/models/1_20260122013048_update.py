from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "Upload" (
    "id" UUID NOT NULL PRIMARY KEY,
    "file_name" VARCHAR(50) NOT NULL,
    "size" DOUBLE PRECISION NOT NULL,
    "uploaded_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "status" VARCHAR(10) NOT NULL DEFAULT 'PROCESSING'
);
COMMENT ON COLUMN "Upload"."status" IS 'SUCCESS: SUCCESS\nFAILED: FAILED\nPROCESSING: PROCESSING';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "Upload";"""


MODELS_STATE = (
    "eJzVlm1vmzAQx78K4lUrbVWbJm0VTZNoQlemNKnysE1dJ+SAIVbBpGDaZl2/+3wGApiEJd"
    "Me0jcN/O/OvvvVvuNZ9QMbe9GBhkNizdS28qxS5GP+IFneKCqaz3MdBIamnnBFuc80YiGy"
    "GFcd5EWYSzaOrJDMGQkoV2nseSAGFnck1M2lmJL7GJsscDGb4ZAbvn7jMqE2fsJR9jq/Mx"
    "2CPbuUKrFhb6GbbDEXmkHZhXCE3aamFXixT3Pn+YLNArr0JpSB6mKKQ8QwLM/CGNKH7NI6"
    "s4qSTHOXJMVCjI0dFHusUO6GDKyAAj+eTSQKdGGXt42j5mnz7PikecZdRCZL5fQlKS+vPQ"
    "kUBPpj9UXYEUOJh8CYc3vAYQQpVeB1ZihcTa8QIiHkicsIM2B1DDMhh5gfnD9E0UdPpoep"
    "y+CAN1qtGmaftGHnUhvuca99qCbghzk54/3U1EhsADYHCVdjC4ip++sEeHR4uAFA7rUWoL"
    "CVAfIdGU7uYBnix9GgvxpiIUQCaROLKT8Uj0SVS70bQGv4Qb2QtB9F914R296V9kUm2ukN"
    "zkX9QcTcUKwiFjjndKFZOneFaw/CFFl3jyi0zYolaATrfKsmv+HLCqLIFaygYqgvHR+TuR"
    "egcrcuW2oHS8FnZwbLZGJ0t5gscUzsA4j5naP46wGjvnNiagEDRewEf5rv1b9yNsUxPD7Z"
    "l4+cqK5+0jjEw6Z42aJNloJeZ7NsbdIrW+tbZavSKSPyfQXEC35P1nzvZAESQAcidhNhDb"
    "LuYHLe05Xrod4xRkbaKhdpq0yMIHGBMFHmUNd6EsFYNBVsm2jFvOlyEoz4eDVLKVSeO2ns"
    "Qfawm3jVECN7QL1F2k9qcI+NK3001q6uSyOpq411sDTK9FN170Q6zctFlM/G+FKBV+Vm0N"
    "flNrL0G9+okBOKWWDS4NFEdqH1ZWoGpnw5GGJxtLrH6DT2xX/V4DQQtXD1piyj/12zUa+H"
    "g44+Ghn9D9WmrY4mHTC2lfThll5oRk/vtpXk95bm4W1FWmrr77qNPutqvur2//dnx8tPn/"
    "W4VQ=="
)
