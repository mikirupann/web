DROP TABLE IF EXISTS users;

--テーブルがなっかたら作成
CREATE TABLE IF NOT EXISTS  users(
    src TEXT,
    alt TEXT,
    title TEXT
);

--テストデータの挿入
INSERT INTO
    customers
VALUES
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs1-1536x1024.png', '貧困をなくそう', '貧困をなくそう'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs2-1536x1024.png', '飢餓をゼロに', '飢餓をゼロに'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs3-1536x1024.png', 'すべての人に健康と福祉を', 'すべての人に健康と福祉を'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs4-1536x1024.png', '質の高い教育をみんなに', '質の高い教育をみんなに'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs5-1536x1024.png', 'ジェンダー平等を実現しよう', 'ジェンダー平等を実現しよう'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs6-1536x1024.png', '安全な水とトイレを世界中に', '安全な水とトイレを世界中に'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs7-1536x1024.png', 'エネルギーをみんなに', 'エネルギーをみんなに'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs8-1536x1024.png', '働きがいも経済成長も', '働きがいも経済成長も'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs9-1536x1024.png', '産業と技術革新の基盤をつくろう', '産業と技術革新の基盤をつくろう'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs10-1536x1024.png', '人や国の不平等をなくそう', '人や国の不平等をなくそう'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs11-1536x1024.png', '住み続けられるまちづくりを', '住み続けられるまちづくりを'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs12-1536x1024.png', 'つくる責任つかう責任', 'つくる責任つかう責任'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs13-1536x1024.png', '気候変動に具体的な対策を', '気候変動に具体的な対策を'),
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs14-1536x1024.png', '海の豊かさを守ろう', '海の豊かさを守ろう')
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs15-1536x1024.png', '陸の豊かさを守ろう', '陸の豊かさを守ろう')
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs16-1536x1024.png', '平和と公正をすべての人に', '平和と公正をすべての人に')
    ('https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs17-1536x1024.png', 'パートナーシップで目標を達成しよう', 'パートナーシップで目標を達成しよう')
;