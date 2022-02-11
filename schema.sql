--テーブルが存在したら削除
DROP TABLE IF EXISTS customers;

--テーブルがなっかたら作成
CREATE TABLE IF NOT EXISTS customers (
    name TEXT,
    age INTEGER
);

--テストデータの挿入
INSERT INTO
    customers
VALUES
    ('Bob', 15),
    ('Tom', 57),
    ('Ken', 76)
;