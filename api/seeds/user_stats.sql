CREATE TABLE IF NOT EXISTS user_stats(
    user_id int4 NOT NULL,
    user_level int4 NOT NULL,
    strength_level int4 NOT NULL,
    strength_experience int4 NOT NULL,
    intellect_level int4 NOT NULL,
    intellect_experience int4 NOT NULL,
    user_money int8 NOT NULL,
    CONSTRAINT fk_user_stat FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
)