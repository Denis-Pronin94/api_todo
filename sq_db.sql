CREATE TABLE IF NOT EXISTS tasks (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
status integer NOT NULL,
updated_at datetime NOT NULL
);