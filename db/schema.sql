DROP TABLE IF EXISTS Libraries;

CREATE TABLE Libraries (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    authors TEXT NOT NULL,
    publishedDate TEXT NOT NULL,
    ISBN TEXT NOT NULL,
    pagesCount TEXT NOT NULL,
    previewLink TEXT NOT NULL,
    languages TEXT NOT NULL
);