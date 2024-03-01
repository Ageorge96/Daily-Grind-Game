-- -------------------------------------------------------------
-- TablePlus 5.9.0(538)
--
-- https://tableplus.com/
--
-- Database: daily_grind
-- Generation Time: 2024-03-01 06:54:08.4490
-- -------------------------------------------------------------


DROP TABLE IF EXISTS "public"."users";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS id_seq;

-- Table Definition
CREATE TABLE "public"."users" (
    "id" int4 NOT NULL DEFAULT nextval('id_seq'::regclass),
    "username" varchar NOT NULL DEFAULT ''::character varying,
    "password" varchar NOT NULL DEFAULT ''::character varying,
    "email" varchar NOT NULL,
    PRIMARY KEY ("id")
);

INSERT INTO "public"."users" ("id", "username", "password", "email") VALUES
(1, 'steve', 'steve', 'steve@email.com'),
(2, 'bob', 'bob', 'bob@email.com'),
(3, 'mike', 'mike', 'mike@email.com');
