-- -------------------------------------------------------------
-- TablePlus 5.9.0(538)
--
-- https://tableplus.com/
--
-- Database: daily_grind
-- Generation Time: 2024-03-01 07:06:36.8550
-- -------------------------------------------------------------


DROP TABLE IF EXISTS "public"."stats";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS id_seq;

-- Table Definition
CREATE TABLE "public"."stats" (
    "id" int4 NOT NULL DEFAULT nextval('id_seq'::regclass),
    "user_id" int4 NOT NULL,
    "score" int8 NOT NULL,
    "game" varchar NOT NULL,
    "date" timestamp NOT NULL,
    PRIMARY KEY ("id")
);

INSERT INTO "public"."stats" ("id", "user_id", "score", "game", "date") VALUES
(1, 1, 1000, 'running', '2024-03-01 07:00:00'),
(2, 1, 500, 'quiz', '2024-02-29 07:00:00'),
(3, 2, 750, 'running', '2024-02-29 08:00:00'),
(4, 2, 200, 'quiz', '2024-02-29 08:30:00'),
(5, 3, 1100, 'running', '2024-02-29 07:00:00'),
(6, 3, 500, 'quiz', '2024-02-29 07:30:00');
